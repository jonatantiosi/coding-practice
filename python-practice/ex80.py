'''
80 — Escrita com csv.writer
Tarefa: grave um novo arquivo .csv com três colunas de dados
(ex: Nome, Idade, Cidade) usando csv.writer.
Conceitos: csv.writer, writerow, newline=''.
'''
import csv
from pathlib import Path

CAMINHO = Path(__file__).parent / 'ex80.csv'

with open(CAMINHO, 'w', encoding='utf8', newline='') as arquivo:
    csv_writer = csv.writer(arquivo)
    csv_writer.writerow(['Nome', 'Idade', 'Cidade'])
    csv_writer.writerow(['Jonatan', '24', 'Santo André'])
    csv_writer.writerow(['Maple', '6', 'Santo André'])
