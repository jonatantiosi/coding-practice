'''
81 — Escrita com DictWriter
Tarefa: crie uma lista de dicionários e salve em um arquivo .csv com
csv.DictWriter. Escreva o cabeçalho e as linhas.
Conceitos: csv.DictWriter, writeheader, writerow.
'''
import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / 'ex81.csv'

lista_ = [
    {'Nome': 'Jonatan', 'Idade': 24, 'Cidade': 'Santo André'},
    {'Nome': 'Maple', 'Idade': 6, 'Cidade': 'Santo André'}
]

with open(CAMINHO, 'w', encoding='utf8', newline='') as arquivo:
    csv_writer = csv.DictWriter(
        arquivo, fieldnames=['Nome', 'Idade', 'Cidade']
        )
    csv_writer.writeheader()
    for dicionario in lista_:
        csv_writer.writerow(dicionario)
