from pdf2image import convert_from_path
import os
from datetime import datetime

def get_pdf_files_with_today_date(directory):
    today_date = datetime.today().strftime('%d%b%Y')

    pdf_files_today = []

    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            file_date = filename.split('_')[-1].split('.')[0]
            if file_date == today_date:
                pdf_files_today.append(filename)

    return pdf_files_today

def pdf_to_jpeg(pdf_path, pdf_file, output_folder):
    # Convert PDF to JPEG images
    images = convert_from_path(pdf_path)

    # Save each image as a JPEG file
    for i, image in enumerate(images):
        image_path = f"{output_folder}/{pdf_file}.jpg"
        image.save(image_path, 'JPEG')
        print(f"{pdf_path} saved as {image_path}")

#driver code        
directory = "./price_list_pdf"
output_folder = "./price_list_img"

try:
    pdf_files_today = get_pdf_files_with_today_date(directory)
except:
    print("No files for today found")
    exit()

for pdf_file in pdf_files_today:
    #print(pdf_file)
    pdf_path = f"./price_list_pdf/{pdf_file}"
    pdf_to_jpeg(pdf_path, pdf_file, output_folder)







