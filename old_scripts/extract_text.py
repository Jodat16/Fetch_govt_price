import fitz # PyMuPDF

def extract_text_from_scanned_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)  # Open the PDF file
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return text

# Example usage
pdf_path = ".\\price_list\\page_1.jpg"
extracted_text = extract_text_from_scanned_pdf(pdf_path)
print(extracted_text)
