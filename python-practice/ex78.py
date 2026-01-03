'''
Tarefa: leia um arquivo .csv e imprima cada linha como lista (csv.reader).
Pule o cabeçalho com next().
Conceitos: csv.reader, next, leitura linha a linha.
'''
import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / 'ex78.csv'

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(linha)
