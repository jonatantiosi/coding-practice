'''
114 — Extraindo páginas de um PDF
Tarefa: abra um PDF existente e salve cada página em um novo arquivo PDF
separado, numerando os arquivos.
Conceitos: pypdf.PdfReader, PdfWriter, pages, add_page, write.
'''
from pypdf import PdfReader, PdfWriter
from pathlib import Path


ROOT_PATH = Path(__file__).parent
ORIGINAL_PDF_FOLDER_PATH = ROOT_PATH / 'PdfOriginais'
ORIGINAL_PDF_FILE_PATH = ORIGINAL_PDF_FOLDER_PATH / 'R20230210.pdf'
NEW_PDF_FILE_PATH = ROOT_PATH / 'PdfCopias'

pdf_reader = PdfReader(ORIGINAL_PDF_FILE_PATH)


for i, page in enumerate(pdf_reader.pages, start=1):
    pdf_writer = PdfWriter()
    with open(NEW_PDF_FILE_PATH / f'page{i}.pdf', 'wb') as file:
        pdf_writer.add_page(page)
        pdf_writer.write(file)
