# 📦 PDF & Excel Toolkit

A powerful and beginner-friendly Python toolkit to automate common PDF and Excel tasks — built using `PyPDF2` and `openpyxl`.

---

## 🚀 Features

✅ **PDF Merger**  
Combine multiple PDF files into a single file.

✅ **PDF Splitter**  
Split a PDF into individual pages.

✅ **PDF Text Extractor**  
Extract all text from a PDF file.

✅ **Excel Highlighter**  
Highlight cells in Excel based on threshold values (e.g., marks < 40 turn red).

---

## 🛠️ Technologies Used

- Python 3.x
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [openpyxl](https://pypi.org/project/openpyxl/)

---

## 📁 Project Structure

PdfExcelToolkit/
├── main.py
├── pdf_merger.py
├── pdf_splitter.py
├── pdf_text_extractor.py
├── excel_formatter.py
└── README.md


---

## ▶️ How to Run

1. **Install dependencies**  

   pip install PyPDF2 openpyxl


Run the toolkit
python main.py


Choose an option
The CLI interface will guide you through merging, splitting, extracting text, or formatting Excel files.

📦 Input Format Notes
1. You can skip file extensions like .pdf or .xlsx while entering paths.

2. For Excel, ensure you're using .xlsx format and correct sheet name.

📌 Example Use Case
🔹 Merge Resumes:
Combine multiple resumes into one PDF using the merger.

🔹 Highlight Failures:
Highlight students who scored less than 40 in column C of a marks Excel sheet.

👨‍💻 Author
Jxy-CyberSec
