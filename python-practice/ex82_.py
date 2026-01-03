'''
82 — Combinação JSON + CSV
Tarefa: leia um arquivo .json com informações de produtos e grave um .csv
contendo apenas nome e preço.
Conceitos: integração entre json e csv, extração seletiva de dados.
'''
import json
from pathlib import Path
import csv

CAMINHO_JSON = Path(__file__).parent / 'ex82.json'
CAMINHO_CSV = Path(__file__).parent / 'ex82.csv'

produtos = [
    {"Nome": "Camisa", "Preco": 40, "Tamanho": "G"},
    {"Nome": "Calca", "Preco": 30, "Tamanho": "M"}
]

with open(CAMINHO_JSON, 'w', encoding='utf8') as arquivo:
    # coloca lista de produtos em arquivo JSON (inicialmente)
    json.dump(produtos, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_JSON, 'r', encoding='utf8') as arquivo:
    # carrega lista de dicionarios de produtos
    lista_produtos = json.load(arquivo)

with open(CAMINHO_CSV, 'w', encoding='utf8', newline='') as arquivo:
    # escreve header e depois passa por cada item do dicionario pegando
    # comente nome e preco
    nome_campos = ["Nome", "Preco"]
    csv_writer = csv.DictWriter(arquivo, fieldnames=nome_campos)
    csv_writer.writeheader()
    for produto in lista_produtos:
        csv_writer.writerow({
            "Nome": produto["Nome"],
            "Preco": produto["Preco"]
        })
