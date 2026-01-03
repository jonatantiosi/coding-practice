'''
70 — Tamanho legível dos arquivos
Tarefa: usando os.stat e math.log, crie função formata_tamanho(bytes) que
converte o tamanho em B, KB, MB, etc. Depois, percorra uma pasta e mostre o
nome e o tamanho formatado de cada arquivo.
Conceitos: os.stat, os.path.getsize, logaritmo, formatação de texto.
'''
import math
import os


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    if tamanho_em_bytes <= 0:
        return '0B'
    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    potencia = base ** indice_abreviacao_tamanhos
    tamanho_final = round(tamanho_em_bytes/potencia, 2)
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'


CAMINHO = os.path.join(r'C:\Users', 'Jonatan', 'Pictures', 'SolidColors')

for root, dirs_, files_ in os.walk(CAMINHO):
    print(root)
    for dir_ in dirs_:
        print(' ', dir_)
    for file_ in files_:
        file_path = os.path.join(root, file_)
        file_size = formata_tamanho(os.path.getsize(file_path))
        print(f'{file_} {file_size}')
