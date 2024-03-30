from __future__ import print_function
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_ocr_api_client.Configuration()
configuration.api_key['Apikey'] = '33e8ea08-a5cf-4cd5-bb80-549fe52e0b46'



# create an instance of the API class
api_instance = cloudmersive_ocr_api_client.ImageOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
image_file = './price_list/apple1_1.png' # file | Image file to perform OCR on.  Common file formats such as PNG, JPEG are supported.
#recognition_mode = 'Basic' # str | Optional; possible values are 'Basic' which provides basic recognition and is not resillient to page rotation, skew or low quality images uses 1-2 API calls; 'Normal' which provides highly fault tolerant OCR recognition uses 26-30 API calls; and 'Advanced' which provides the highest quality and most fault-tolerant recognition uses 28-30 API calls.  Default recognition mode is 'Advanced' (optional)
language = "URD" # str | Optional, language of the input document, default is English (ENG).  Possible values are ENG (English), ARA (Arabic), ZHO (Chinese - Simplified), ZHO-HANT (Chinese - Traditional), ASM (Assamese), AFR (Afrikaans), AMH (Amharic), AZE (Azerbaijani), AZE-CYRL (Azerbaijani - Cyrillic), BEL (Belarusian), BEN (Bengali), BOD (Tibetan), BOS (Bosnian), BUL (Bulgarian), CAT (Catalan; Valencian), CEB (Cebuano), CES (Czech), CHR (Cherokee), CYM (Welsh), DAN (Danish), DEU (German), DZO (Dzongkha), ELL (Greek), ENM (Archaic/Middle English), EPO (Esperanto), EST (Estonian), EUS (Basque), FAS (Persian), FIN (Finnish), FRA (French), FRK (Frankish), FRM (Middle-French), GLE (Irish), GLG (Galician), GRC (Ancient Greek), HAT (Hatian), HEB (Hebrew), HIN (Hindi), HRV (Croatian), HUN (Hungarian), IKU (Inuktitut), IND (Indonesian), ISL (Icelandic), ITA (Italian), ITA-OLD (Old - Italian), JAV (Javanese), JPN (Japanese), KAN (Kannada), KAT (Georgian), KAT-OLD (Old-Georgian), KAZ (Kazakh), KHM (Central Khmer), KIR (Kirghiz), KOR (Korean), KUR (Kurdish), LAO (Lao), LAT (Latin), LAV (Latvian), LIT (Lithuanian), MAL (Malayalam), MAR (Marathi), MKD (Macedonian), MLT (Maltese), MSA (Malay), MYA (Burmese), NEP (Nepali), NLD (Dutch), NOR (Norwegian), ORI (Oriya), PAN (Panjabi), POL (Polish), POR (Portuguese), PUS (Pushto), RON (Romanian), RUS (Russian), SAN (Sanskrit), SIN (Sinhala), SLK (Slovak), SLV (Slovenian), SPA (Spanish), SPA-OLD (Old Spanish), SQI (Albanian), SRP (Serbian), SRP-LAT (Latin Serbian), SWA (Swahili), SWE (Swedish), SYR (Syriac), TAM (Tamil), TEL (Telugu), TGK (Tajik), TGL (Tagalog), THA (Thai), TIR (Tigrinya), TUR (Turkish), UIG (Uighur), UKR (Ukrainian), URD (Urdu), UZB (Uzbek), UZB-CYR (Cyrillic Uzbek), VIE (Vietnamese), YID (Yiddish) (optional)
#preprocessing = 'Auto' # str | Optional, preprocessing mode, default is 'Auto'.  Possible values are None (no preprocessing of the image), and Auto (automatic image enhancement of the image before OCR is applied; this is recommended). (optional)

output_file = './price_list/apple1_1.txt'
try:
    # Convert a scanned image into text
    with open(image_file, 'r') as f:
        api_response = api_instance.image_ocr_photo_to_text
        print(type(api_response))
        pprint(api_response)
        # Write API response to text file
        text_result = ''
    if isinstance(api_response, bytes):
        # Decode binary response assuming UTF-8 encoding
        text_result = api_response.decode('utf-8')
    else:
        # API response is already text
        text_result = api_response

    # Write API response to text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_result)
except ApiException as e:
    print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)