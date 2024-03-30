import cloudmersive_ocr_api_client 
import TextExtractionApi, Configuration from cloudmersive_ocr_api_client
import csv

api_instance = cloudmersive_ocr_api_client.ImageOcrApi()
# Replace with your Cloudmersive API key
api_key = "33e8ea08-a5cf-4cd5-bb80-549fe52e0b46"

# Configure API client
api_instance.api_client.configuration = Configuration(api_key={"ApiKey": api_key})
text_extraction_api = TextExtractionApi(api_client=configuration)

# Replace with your Urdu image file path
image_path = "./price_list/page_1.jpg"

# Set language to Urdu (if supported by cloudmersive)
language = "URD"  # Check cloudmersive documentation for supported languages

# Read image data
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Send OCR request with image data and language (optional)
try:
    response = text_extraction_api.extract_text_from_image_with_language(
        image_data=image_data, language=language
    )
    extracted_text = response.text_content  # Might be in JSON format

    # Process the extracted text (potentially convert to CSV)
    # This part depends on the structure of your tables and desired output format
    # Here's a simple example assuming a basic table structure:
    lines = extracted_text.splitlines()
    csv_data = [line.split("\t") for line in lines]  # Assuming tab-delimited tables

    # Write CSV data to file (replace with your desired filename)
    with open("output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)

    print("CSV file generated successfully!")
except Exception as e:
    print("Error:", e)
