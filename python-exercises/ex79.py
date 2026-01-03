'''
79 — CSV com DictReader
Tarefa: leia o mesmo arquivo .csv usando csv.DictReader e imprima apenas os
valores de duas colunas específicas (ex: Nome e Idade).
Conceitos: csv.DictReader, iteração sobre dicionários.
'''
import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / 'ex78.csv'

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        print(linha["Nome"], linha["Idade"])
