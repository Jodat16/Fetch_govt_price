import cv2
import os
from PIL import Image
from datetime import datetime

def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def crop_image(input_image_path, output_image_path, crop_box):
    # Read the image
    img = cv2.imread(input_image_path)

    # Crop the image using the crop box
    cropped_image = img[crop_box[1]:crop_box[3], crop_box[0]:crop_box[2]]

    # Save the cropped image
    cv2.imwrite(output_image_path, cropped_image)
    print("Cropped image saved as:", output_image_path)

def get_img_files_with_today_date(directory):
    today_date = datetime.today().strftime('%d%b%Y')

    img_files_today = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            file_date = filename.split('_')[-2].split('.')[0]
            if file_date == today_date:
                img_files_today.append(filename)

    return img_files_today

# Driver code
#input_image_path = "./price_list/1710916263_table.jpg"  # Path to the input image file

# width, height = get_image_dimensions(input_image_path)
# print("Image dimensions - Width:", width, "Height:", height)


directory = "./price_list_table"
table_images = get_img_files_with_today_date(directory)
for table_img in table_images:
    input_image_path = f"{directory}/{table_img}"
    date = table_img.split('_')[1]
    output_image_path = "./price_rows/"
    category = table_img.split('_')[0]
    if category == 'fruits':
        # Define the crop box for banana
        # crop_box[col_start,row_start, col_end, row_end]
        banana_image_path = os.path.splitext(output_image_path)[0] + "banana_" + date + ".jpg"
        banana_crop_box = [600, 40, 1110, 90]  # Example crop box coordinates (left, top, right, bottom)
        print(banana_crop_box[0])
        crop_image(input_image_path, banana_image_path, banana_crop_box)

        # Define the crop box for apple golden
        apple_golden_image_path = os.path.splitext(output_image_path)[0] + "applegolden_" +  date + ".jpg"
        apple_golden_crop_box = [600, 325, 1110, 380]  # Example crop box coordinates (left, top, right, bottom)
        crop_image(input_image_path, apple_golden_image_path, apple_golden_crop_box)

        # Define the crop box for apple
        apple_image_path = os.path.splitext(output_image_path)[0] + "apple_" +  date + ".jpg"
        apple_crop_box = [600, 410, 1110, 460]  # Example crop box coordinates (left, top, right, bottom)
        crop_image(input_image_path, apple_image_path, apple_crop_box)