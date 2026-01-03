# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'
# print(CAMINHO_CSV)

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)
    # next(leitor)  # pula a primeira linha
    # print(next(leitor))
    for linha in leitor:
        print(linha)
        # poderia ser, por exemplo print(linha[1])
print()

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor_dict = csv.DictReader(arquivo)

    for dicionario in leitor_dict:
        print(dicionario['Nome'], dicionario['Idade'])
