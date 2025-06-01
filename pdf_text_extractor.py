from PyPDF2 import PdfReader
import os

def extract_text_from_pdf(input_pdf_path, output_txt_path):
    if not input_pdf_path.lower().endswith('.pdf'):
        input_pdf_path += '.pdf'
    if not os.path.exists(input_pdf_path):
        print("❌ PDF file not found.")
        return
    try:
        reader = PdfReader(input_pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        os.makedirs(os.path.dirname(output_txt_path), exist_ok=True)
        with open(output_txt_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"✅ Text extracted and saved to: {output_txt_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
