import requests

# Define the OCR API endpoint URL
ocr_api_url = "https://api.cloudmersive.com/ocr/pdf/toText"

# Define your API key
api_key = "33e8ea08-a5cf-4cd5-bb80-549fe52e0b46"

# Define headers with API key
headers = {
    "Apikey": api_key
}

# Define the image file path
image_file_path = './price_list/1710482835.pdf'

# Open the image file in binary mode
with open(image_file_path, "rb") as file:
    # Prepare the payload
    files = {
        'imageFile': file
    }
    
    # Send POST request to OCR API endpoint
    try:
        response = requests.post(ocr_api_url, headers=headers, files=files, params={"language": "URD"})
        response.raise_for_status()  # Raise exception for any HTTP errors
        
        # Get the OCR result
        api_response = response.json()
        
        print("API Response:", api_response)
    except requests.exceptions.RequestException as e:
        print("Exception occurred:", e)
