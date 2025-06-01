from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_pdf_path, output_folder):
    if not input_pdf_path.lower().endswith('.pdf'):
        input_pdf_path += '.pdf'
    if not os.path.exists(input_pdf_path):
        print("❌ PDF file not found.")
        return
    os.makedirs(output_folder, exist_ok=True)

    reader = PdfReader(input_pdf_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_path = os.path.join(output_folder, f"page_{i + 1}.pdf")
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"✅ Saved: {output_path}")
