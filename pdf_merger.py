from PyPDF2 import PdfMerger
import os

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        pdf = pdf.strip()
        if not pdf.lower().endswith('.pdf'):
            pdf += '.pdf'
        if os.path.exists(pdf):
            merger.append(pdf)
        else:
            print(f"❌ Skipped (Not found or invalid): {pdf}")
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        merger.write(output_path)
        merger.close()
        print(f"✅ Merged PDF saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error saving merged PDF: {e}")
