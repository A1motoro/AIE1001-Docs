import os
import sys
import PyPDF2

# Directory paths
docs_dir = '../docs'
extracted_dir = 'extracted'

# Create extracted directory if it doesn't exist
os.makedirs(extracted_dir, exist_ok=True)

def extract_pdf(pdf_name):
    """Extract text from a single PDF file"""
    pdf_path = os.path.join(docs_dir, pdf_name)
    if os.path.exists(pdf_path):
        try:
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
            print(f'✓ 成功提取 {pdf_name} -> {txt_name}')
            return True
        except Exception as e:
            print(f'✗ 提取 {pdf_name} 时出错: {e}')
            return False
    else:
        print(f'✗ 文件不存在: {pdf_name}')
        return False

def list_available_pdfs():
    """List all PDF files in the docs directory"""
    if os.path.exists(docs_dir):
        pdf_files = [f for f in os.listdir(docs_dir) if f.endswith('.pdf')]
        return sorted(pdf_files)
    return []

if __name__ == '__main__':
    # Check if PDF files are provided as command line arguments
    if len(sys.argv) > 1:
        # Extract PDFs from command line arguments
        pdf_files = sys.argv[1:]
        for pdf_name in pdf_files:
            if not pdf_name.endswith('.pdf'):
                pdf_name += '.pdf'
            extract_pdf(pdf_name)
    else:
        # Interactive mode: list available PDFs and let user choose
        available_pdfs = list_available_pdfs()
        
        if not available_pdfs:
            print('未找到PDF文件！')
            sys.exit(1)
        
        print('\n可用的PDF文件：')
        for i, pdf in enumerate(available_pdfs, 1):
            print(f'  {i}. {pdf}')
        
        print('\n选择操作：')
        print('  1. 输入PDF文件名（多个文件用空格分隔）')
        print('  2. 输入序号（多个序号用空格分隔）')
        print('  3. 提取所有PDF文件')
        
        choice = input('\n请选择 (1/2/3): ').strip()
        
        if choice == '1':
            pdf_input = input('请输入PDF文件名（多个用空格分隔）: ').strip()
            pdf_names = pdf_input.split()
            for pdf_name in pdf_names:
                if not pdf_name.endswith('.pdf'):
                    pdf_name += '.pdf'
                extract_pdf(pdf_name)
        
        elif choice == '2':
            indices_input = input('请输入序号（多个用空格分隔）: ').strip()
            try:
                indices = [int(i) - 1 for i in indices_input.split()]
                for idx in indices:
                    if 0 <= idx < len(available_pdfs):
                        extract_pdf(available_pdfs[idx])
                    else:
                        print(f'✗ 无效序号: {idx + 1}')
            except ValueError:
                print('✗ 输入格式错误，请输入数字')
        
        elif choice == '3':
            print('\n提取所有PDF文件...')
            for pdf_name in available_pdfs:
                extract_pdf(pdf_name)
        else:
            print('✗ 无效选择')

