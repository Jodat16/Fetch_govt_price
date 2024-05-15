import cv2
import numpy as np
from datetime import datetime
import os

def detect_tables(image_path, img_file, output_dir):
    # Read the image
    img = cv2.imread(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)
    # Find contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Find the contour with the largest area
    max_contour = max(contours, key=cv2.contourArea)
    # Get the bounding box of the largest contour
    x, y, w, h = cv2.boundingRect(max_contour)
    # Crop the image using the bounding box
    cropped_image = img[y:y+h, x:x+w]
    # Save the cropped image
    img_file = img_file.split('.')[0]
    output_path = f"{output_dir}/{img_file}_table.jpg"
    cv2.imwrite(output_path, cropped_image)
    print("Cropped image saved as:", output_path)

def get_img_files_with_today_date(directory):
    today_date = datetime.today().strftime('%d%b%Y')

    img_files_today = []

    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):
            file_date = filename.split('_')[-1].split('.')[0]
            if file_date == today_date:
                img_files_today.append(filename)

    return img_files_today

#driver code
dir = "./price_list_img"
try:
    img_files_today = get_img_files_with_today_date(dir)
except:
    print("No files for today found")
    exit()


for img_file in img_files_today:
    img_path = f"./price_list_img/{img_file}"
    output_path = f"./price_list_table"
    detect_tables(img_path, img_file, output_path)
