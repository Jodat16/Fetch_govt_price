import fitz     #it is from PyMuPDF
import os

def crop_pdf(input_pdf_path, output_pdf_path, crop_box):
    
    # Open the input PDF
    pdf_document = fitz.open(input_pdf_path)
    page = pdf_document.load_page(0)  # Load the first page (page numbering starts from 0)
    page.set_cropbox(crop_box)

    # Save the modified PDF to a new file
    pdf_document.save(output_pdf_path)
    pdf_document.close()

# Driver code
input_pdf_path = "./price_list/1710916263.pdf"  # Path to the input PDF file

pdf_document = fitz.open(input_pdf_path)
page = pdf_document.load_page(0)  # Load the first page (page numbering starts from 0)
media_box = page.mediabox  # Get the MediaBox of the page
print("MediaBox:", media_box)

# Define the crop box (left, top, right, bottom) in PDF points
# Define the crop box for banana
banana_pdf_path = os.path.splitext(input_pdf_path)[0] + "_banana.pdf"
banana_crop_box = (media_box[2]-295, media_box[3]-780, media_box[2]-100, media_box[3]-759)
crop_pdf(input_pdf_path, banana_pdf_path, banana_crop_box)

# Define the crop box for apple
apple_pdf_path = os.path.splitext(input_pdf_path)[0] + "_apple.pdf"
apple_crop_box = (media_box[2]-295, media_box[3]-645, media_box[2]-100, media_box[3]-624)
crop_pdf(input_pdf_path, apple_pdf_path, apple_crop_box)

# Define the crop box for apple golden
apple_golden_pdf_path = os.path.splitext(input_pdf_path)[0] + "_apple_golden.pdf"
apple_golden_crop_box = (media_box[2]-295, media_box[3]-677, media_box[2]-100, media_box[3]-656)
crop_pdf(input_pdf_path, apple_golden_pdf_path, apple_golden_crop_box)