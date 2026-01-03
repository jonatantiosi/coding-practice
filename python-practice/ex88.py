'''
88 — Template seguro
Tarefa: carregue um texto contendo uma variável inexistente e substitua usando
safe_substitute sem gerar erro.
Conceitos: safe_substitute, tratamento seguro de variáveis faltantes.
'''
import string
from pathlib import Path

CAMINHO = Path(__file__).parent / 'ex88.txt'

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    string_ = arquivo.read()

dados = dict(
    nome='Paulo',
    valor='R$1000'
)

template = string.Template(string_)
print(template.safe_substitute(dados))