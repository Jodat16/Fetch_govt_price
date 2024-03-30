import requests

url = 'https://app.nanonets.com/api/v2/OCR/Model/REPLACE_MODEL_ID/LabelFile/'

data = {'file': open('REPLACE_IMAGE_PATH.jpg', 'rb')}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth('REPLACE_API_KEY', ''), files=data)
# for base64 of file instead of file
# with open('REPLACE_IMAGE_PATH.jpg', 'rb') as file:
#   encoded_file = base64.b64encode(file.read())
# data = {'base64_data': encoded_file}
# response = requests.post(url, auth=requests.auth.HTTPBasicAuth('REPLACE_API_KEY', ''), data=data)

print(response.text)



import requests
import csv

# Replace with your Nanonets API key
api_key = "a8c6bc5c-e314-11ee-8cf9-e279c3a0324b"

# Endpoint for OCR with table extraction
endpoint = "https://app.nanonets.com/api/v2.1/workflows/"

# Image path (replace with your file path)
image_path = "price_list/page_1.jpg"

# Language code for Urdu
language = "ur"

# Load image data
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Set headers for API request
headers = {
    "Authorization": f"{api_key}"
}

# Send POST request with image data and language
response = requests.post(endpoint, headers=headers, files={"file": image_data}, data={"language": language})

# Check for successful response
if response.status_code == 200:
    csv_data = response.json()

    # Write CSV data to file
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for row in csv_data:
            writer.writerow(row)

    print("CSV file generated successfully!")
else:
    print("Error:", response.text)
