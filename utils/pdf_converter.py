import zipfile
from PIL import Image
from PyPDF2 import PdfWriter

def convert_cbz_to_pdf(cbz_file):
    """Converts a CBZ file to a PDF."""
    with zipfile.ZipFile(cbz_file, 'r') as zip_ref:
        zip_ref.extractall()

    image_files = [f for f in os.listdir('.') if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    image_files.sort()

    pdf_writer = PdfWriter()

    for image_file in image_files:
        img = Image.open(image_file)
        width, height = img.size
        pdf_writer.add_page(img, pagesize=(width, height))

    pdf_path = 'output.pdf'
    with open(pdf_path, 'wb') as pdf_file:
        pdf_writer.write(pdf_file)

    # Clean up extracted images
    for image_file in image_files:
        os.remove(image_file)

    return pdf_path
