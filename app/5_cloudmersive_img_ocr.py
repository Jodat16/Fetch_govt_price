import cloudmersive_ocr_api_client
from cloudmersive_ocr_api_client.rest import ApiException
import os
import json
from datetime import datetime

def get_img_files_with_today_date(directory):
    today_date = datetime.today().strftime('%d%b%Y')

    img_files_today = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            file_date = filename.split('_')[-1].split('.')[0]
            if file_date == today_date:
                img_files_today.append(filename)

    return img_files_today

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '0d1d50c8-3c1b-4453-bf87-27b556c29169'
#my key: 33e8ea08-a5cf-4cd5-bb80-549fe52e0b46
#default key: 808e8f25-b614-4047-b1e8-c5fd8f6cd8c9

source_dir = "./price_rows"
row_images = get_img_files_with_today_date(source_dir)

for row_img in row_images:
        #txt_file_path = os.path.splitext(image_file_path)[0] + '.txt'
        image_file_path = source_dir + "/" + row_img
        json_file_path = "./price_json/" + os.path.splitext(row_img)[0] + '.json'
        print("New json file path:", json_file_path)

        try:
            # Converts an uploaded image in common formats such as JPEG, PNG into text via Optical Character Recognition.
            api_response = api_instance.image_ocr_post(image_file_path, language= 'URD')
            json_dic = api_response.to_dict()
            # pprint(api_response)
            # with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            #     txt_file.write(str(api_response))
            with open(json_file_path, 'w', encoding='utf-8') as json_file:
                json.dump(json_dic, json_file, ensure_ascii=False, indent=4)
        except ApiException as e:
            print("Exception when calling ImageOcrApi->image_ocr_post: %s\n" % e)