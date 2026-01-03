'''
Tarefa: abra um .zip e extraia todo o conteúdo para uma pasta usando extractall.
Conceitos: extração, ZipFile.extractall, manipulação de caminhos.
'''
from pathlib import Path
from zipfile import ZipFile

CAMINHO_ZIP = Path(__file__).parent / 'ex96_folder.zip'
CAMINHO_PASTA_EXTRAIDA = Path(__file__).parent / 'ex96_folder_extracted'
CAMINHO_PASTA_EXTRAIDA.mkdir(exist_ok=True)

with ZipFile(CAMINHO_ZIP, 'r') as zip:
    zip.extractall(CAMINHO_PASTA_EXTRAIDA)

