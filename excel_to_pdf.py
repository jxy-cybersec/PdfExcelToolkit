import os
import pandas as pd
from fpdf import FPDF

def convert_excel_to_pdf(input_excel_path, sheet_name, output_pdf_path):
    if not os.path.exists(input_excel_path):
        print("❌ Excel file not found.")
        return

    try:
        df = pd.read_excel(input_excel_path, sheet_name=sheet_name)

        if df.empty:
            print("⚠️ Sheet is empty.")
            return

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        col_width = pdf.w / (len(df.columns) + 1)
        row_height = pdf.font_size + 2

        # Header
        pdf.set_fill_color(200, 220, 255)
        for col in df.columns:
            pdf.cell(col_width, row_height, str(col), border=1, fill=True)
        pdf.ln(row_height)

        # Rows
        for _, row in df.iterrows():
            for item in row:
                pdf.cell(col_width, row_height, str(item), border=1)
            pdf.ln(row_height)

        pdf.output(output_pdf_path)
        print(f"✅ PDF saved at: {output_pdf_path}")

    except Exception as e:
        print(f"❌ Error: {e}")
