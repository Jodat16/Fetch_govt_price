from __future__ import print_function
import time
import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os
import json

# Configure API key authorization: Apikey
configuration = cloudmersive_ocr_api_client.Configuration()
configuration.api_key['Apikey'] = '0d1d50c8-3c1b-4453-bf87-27b556c29169' # stolen key from try page
#my_key = '33e8ea08-a5cf-4cd5-bb80-549fe52e0b46'



# create an instance of the API class
api_instance = cloudmersive_ocr_api_client.PdfOcrApi(cloudmersive_ocr_api_client.ApiClient(configuration))
image_file_path = './price_list/1710482835_apple_golden.pdf' # file | PDF file to perform OCR on.
# Replace the file extension with a new one
new_file_extension = '.txt'
txt_file_path = os.path.splitext(image_file_path)[0] + '.txt'
json_file_path = os.path.splitext(image_file_path)[0] + '.json'
print("New image file path:", txt_file_path)

#recognition_mode = 'recognition_mode_example' # str | Optional; possible values are 'Basic' which provides basic recognition and is not resillient to page rotation, skew or low quality images uses 1-2 API calls per page; 'Normal' which provides highly fault tolerant OCR recognition uses 26-30 API calls per page; and 'Advanced' which provides the highest quality and most fault-tolerant recognition uses 28-30 API calls per page.  Default recognition mode is 'Basic' (optional)
language = 'URD' # str | Optional, language of the input document, default is English (ENG).  Possible values are ENG (English), ARA (Arabic), ZHO (Chinese - Simplified), ZHO-HANT (Chinese - Traditional), ASM (Assamese), AFR (Afrikaans), AMH (Amharic), AZE (Azerbaijani), AZE-CYRL (Azerbaijani - Cyrillic), BEL (Belarusian), BEN (Bengali), BOD (Tibetan), BOS (Bosnian), BUL (Bulgarian), CAT (Catalan; Valencian), CEB (Cebuano), CES (Czech), CHR (Cherokee), CYM (Welsh), DAN (Danish), DEU (German), DZO (Dzongkha), ELL (Greek), ENM (Archaic/Middle English), EPO (Esperanto), EST (Estonian), EUS (Basque), FAS (Persian), FIN (Finnish), FRA (French), FRK (Frankish), FRM (Middle-French), GLE (Irish), GLG (Galician), GRC (Ancient Greek), HAT (Hatian), HEB (Hebrew), HIN (Hindi), HRV (Croatian), HUN (Hungarian), IKU (Inuktitut), IND (Indonesian), ISL (Icelandic), ITA (Italian), ITA-OLD (Old - Italian), JAV (Javanese), JPN (Japanese), KAN (Kannada), KAT (Georgian), KAT-OLD (Old-Georgian), KAZ (Kazakh), KHM (Central Khmer), KIR (Kirghiz), KOR (Korean), KUR (Kurdish), LAO (Lao), LAT (Latin), LAV (Latvian), LIT (Lithuanian), MAL (Malayalam), MAR (Marathi), MKD (Macedonian), MLT (Maltese), MSA (Malay), MYA (Burmese), NEP (Nepali), NLD (Dutch), NOR (Norwegian), ORI (Oriya), PAN (Panjabi), POL (Polish), POR (Portuguese), PUS (Pushto), RON (Romanian), RUS (Russian), SAN (Sanskrit), SIN (Sinhala), SLK (Slovak), SLV (Slovenian), SPA (Spanish), SPA-OLD (Old Spanish), SQI (Albanian), SRP (Serbian), SRP-LAT (Latin Serbian), SWA (Swahili), SWE (Swedish), SYR (Syriac), TAM (Tamil), TEL (Telugu), TGK (Tajik), TGL (Tagalog), THA (Thai), TIR (Tigrinya), TUR (Turkish), UIG (Uighur), UKR (Ukrainian), URD (Urdu), UZB (Uzbek), UZB-CYR (Cyrillic Uzbek), VIE (Vietnamese), YID (Yiddish) (optional)
#preprocessing = 'preprocessing_example' # str | Optional, preprocessing mode, default is 'Auto'.  Possible values are None (no preprocessing of the image), and Auto (automatic image enhancement of the image before OCR is applied; this is recommended). (optional)

try:
    # Converts an uploaded PDF file into text via Optical Character Recognition.
    api_response = api_instance.pdf_ocr_post(image_file_path, language=language)
    json_dic = api_response.to_dict()
    # pprint(api_response)
    with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(str(api_response))
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_dic, json_file, ensure_ascii=False, indent=4)
except ApiException as e:
    print("Exception when calling PdfOcrApi->pdf_ocr_post: %s\n" % e)