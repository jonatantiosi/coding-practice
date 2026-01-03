'''
Tarefa: salve um dicionário em um arquivo .json usando json.dump() e depois
leia de volta com json.load(), imprimindo um dos valores.
Conceitos: json.dump, json.load, I/O de arquivo
'''
import json
from pathlib import Path

dicionario = {
    "Nome": "Jonatan",
    "Idade": 23
}

CAMINHO_ARQUIVO = Path(__file__).parent / 'ex75.json'

with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(dicionario, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    dicionario_2 = json.load(arquivo)

print(dicionario_2["Nome"])
