from pdf_merger import merge_pdfs
from pdf_splitter import split_pdf
from pdf_text_extractor import extract_text_from_pdf
from excel_formatter import format_excel_with_highlights

def main():
    print("🛠️ PDF & Excel Toolkit")
    print("1️⃣ Merge PDFs")
    print("2️⃣ Split PDF")
    print("3️⃣ Extract text from PDF")
    print("4️⃣ Format Excel with highlights")
    choice = input("👉 Choose an option (1 or 2 or 3 or 4): ").strip()

    if choice == "1":
        print("\n📎 PDF Merger Utility")
        files = input("🔹 Enter PDF file paths (comma separated): ").split(",")
        files = [f.strip() for f in files]
        output = input("💾 Enter output path (e.g., merged/merged.pdf): ").strip()
        merge_pdfs(files, output)

    elif choice == "2":
        print("\n✂️ PDF Splitter Utility")
        input_pdf = input("📄 Enter full path to PDF to split: ").strip()
        output_folder = input("📂 Enter folder to save split pages: ").strip()
        split_pdf(input_pdf, output_folder)

    elif choice == "3":
        print("\n📝 PDF Text Extractor")
        input_pdf = input("📄 Enter full path to PDF: ").strip()
        output_txt = input("💾 Enter output text file path: ").strip()
        extract_text_from_pdf(input_pdf, output_txt)

    elif choice == "4":
        print("\n📊 Excel Formatter")
        excel_file = input("📁 Enter path to Excel file: ").strip()
        sheet_name = input("📄 Enter sheet name: ").strip()
        column_letter = input("🔠 Enter column letter to check values (e.g., C): ").strip().upper()
        threshold = int(input("🔢 Enter threshold (e.g., 40): ").strip())
        format_excel_with_highlights(excel_file, sheet_name, column_letter, threshold)

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
