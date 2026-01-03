'''
96 — Compactar arquivos em ZIP

Tarefa: crie uma pasta, gere 5 arquivos .txt dentro dela e compacte tudo em um
único arquivo .zip usando ZipFile no modo "w".
Conceitos: zipfile.ZipFile, escrita em ZIP, criação de arquivos, Path.
'''
from zipfile import ZipFile
from pathlib import Path
import os

CAMINHO_PASTA = Path(__file__).parent / 'ex96_folder'
CAMINHO_PASTA.mkdir(exist_ok=True)
CAMINHO_ZIP = Path(__file__).parent / 'ex96_folder.zip'

def criar_arquivos(quantidade, caminho):
    for i in range(1, quantidade+1):
        texto = 'texto do arquivo %s' % i
        caminho_completo = caminho / f'{i}.txt'
        with open(caminho_completo, 'w', encoding='utf8') as arquivo:
            arquivo.write(texto)

criar_arquivos(5, CAMINHO_PASTA)

with ZipFile(CAMINHO_ZIP, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_PASTA):
        for file in files:
            zip.write(os.path.join(root, file), file)
