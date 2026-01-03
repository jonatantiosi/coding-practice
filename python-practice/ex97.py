'''
97 — Listar conteúdo de um arquivo ZIP
Tarefa: abra um arquivo .zip existente e imprima todos os nomes de arquivos
armazenados nele usando namelist().
Conceitos: leitura de ZIP, ZipFile.namelist.
'''
from zipfile import ZipFile
from pathlib import Path

nome_pasta = 'ex96_folder.zip'
CAMINHO_ZIP = Path(__file__).parent / nome_pasta

with ZipFile(CAMINHO_ZIP, 'r') as zip:
    nomes_arquivos = zip.namelist()
    print(f'Arquivos de {nome_pasta}:')
    for nome_arquivo in nomes_arquivos:
        print(nome_arquivo)