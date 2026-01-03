# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
from pypdf import PdfReader, PdfWriter

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))

# for page in reader.pages:
#     print(page, '\n')

page1 = reader.pages[0]
imagem1 = page1.images[0]

# print(page1.extract_text())
# # write bytes
# with open(PASTA_NOVOS / imagem1.name, 'wb') as fp:
#     fp.write(imagem1.data)

# writer = PdfWriter()
# writer.add_page(page1)

# with open(PASTA_NOVOS / 'page1.pdf', 'wb') as arquivo:
#     writer.write(arquivo)

# writer = PdfWriter()

# with open(PASTA_NOVOS / 'novo_pdf.pdf', 'wb') as arquivo:
#     for page in reader.pages:
#         writer.add_page(page)
#     writer.write(arquivo)


for i, page in enumerate(reader.pages, start=1):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

merger = PdfWriter()

files = [
    PASTA_NOVA / 'page2.pdf',
    PASTA_NOVA / 'page1.pdf',
]

for file in files:
    merger.append(file)

with open(PASTA_NOVA / 'merged.pdf', 'wb') as arquivo:
    merger.write(arquivo)
