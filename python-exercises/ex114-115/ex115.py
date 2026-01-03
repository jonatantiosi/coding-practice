'''
115 — Mesclar PDFs em ordem específica
Tarefa: receba dois arquivos PDF (já existentes) e gere um novo PDF unindo-os
em uma ordem definida por você.
Conceitos: PdfWriter.append, write.
'''
from pypdf import PdfWriter
from pathlib import Path


ROOT_PATH = Path(__file__).parent
ORIGINAL_PDF_FOLDER_PATH = ROOT_PATH / 'PdfOriginais'
ORIGINAL_PDF_FILE_PATH = ORIGINAL_PDF_FOLDER_PATH / 'R20230210.pdf'
NEW_PDF_FILE_PATH = ROOT_PATH / 'PdfCopias'

pdf_merger = PdfWriter()

files = [
    NEW_PDF_FILE_PATH / 'page1.pdf',
    NEW_PDF_FILE_PATH / 'page2.pdf'
]

for file_ in files:
    pdf_merger.append(file_)

with open(NEW_PDF_FILE_PATH / 'merged.pdf', 'wb') as file:
    pdf_merger.write(file)
