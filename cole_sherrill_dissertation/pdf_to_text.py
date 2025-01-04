import pdfplumber
import os
from pathlib import Path

def convert_pdf_to_text(pdf_path, output_dir='text_chapters'):
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(exist_ok=True)
    
    # Get the filename without extension
    base_name = os.path.basename(pdf_path)
    file_name = os.path.splitext(base_name)[0]
    
    # Create output text file path
    output_path = os.path.join(output_dir, f"{file_name}.txt")
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            with open(output_path, 'w', encoding='utf-8') as text_file:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        text_file.write(text + '\n\n')
        print(f"Successfully converted {base_name} to text")
        return True
    except Exception as e:
        print(f"Error converting {base_name}: {str(e)}")
        return False

def convert_all_pdfs():
    chapters_dir = "chapters"
    
    # Get all PDF files in the chapters directory
    pdf_files = [f for f in os.listdir(chapters_dir) if f.endswith('.pdf')]
    
    # Sort files to process them in order
    pdf_files.sort()
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(chapters_dir, pdf_file)
        convert_pdf_to_text(pdf_path)

if __name__ == "__main__":
    convert_all_pdfs() 