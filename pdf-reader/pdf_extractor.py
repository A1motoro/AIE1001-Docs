import os
import PyPDF2

# Directory paths
docs_dir = '../docs'
extracted_dir = 'extracted'

# Create extracted directory if it doesn't exist
os.makedirs(extracted_dir, exist_ok=True)

# List of PDFs to process
pdf_files = [f'week{i}.pdf' for i in range(1, 7)]

for pdf_name in pdf_files:
    pdf_path = os.path.join(docs_dir, pdf_name)
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
        
        # Save extracted text
        txt_name = pdf_name.replace('.pdf', '.txt')
        txt_path = os.path.join(extracted_dir, txt_name)
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
        print(f'Extracted text from {pdf_name} to {txt_name}')
    else:
        print(f'{pdf_name} not found')
