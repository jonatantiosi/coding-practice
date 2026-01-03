'''
89 — Localização e formatação BRL
Tarefa: formate um número como moeda BRL usando o locale do sistema e inclua no
template.
Conceitos: locale.setlocale, locale.currency, formatação regional.
'''
import locale
import string
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')

CAMINHO = Path(__file__).parent / 'ex89.txt'

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    string_ = arquivo.read()

dados = dict(
    nome='Paulo',
    valor=locale.currency(1000)
)

template = string.Template(string_)
print(template.safe_substitute(dados))