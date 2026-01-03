'''
os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
'''
import math
import os
from itertools import count

# Original:
# https://stackoverflow.com/questions/5194057/
# better-way-to-convert-file-sizes-in-python


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    '''formata um tamanho de bytes para o tamanho apropriado'''
    '''da pra trocar base para 1000'''
    # se o tamanho for menor ou igual a 0, 0B
    if tamanho_em_bytes <= 0:
        return 'OB'
    # tupla com os tamanhos
    # (B = 0, KB = 1, MB = 2, GB = 3, TB = 4, PB = 5)
    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'

    # math.log vai retornar o logaritmo do tamanho_em_bytes
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))

    potencia = base ** indice_abreviacao_tamanhos

    tamanho_final = round(tamanho_em_bytes/potencia, 2)
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao_tamanho}'


caminho = os.path.join('C:\\Users', 'Jonatan', 'Pictures', 'Maple')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # maneira mais facil:
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'File:', file_, formata_tamanho(tamanho))
