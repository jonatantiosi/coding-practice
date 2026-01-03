'''
87 — Template Strings (substitute)
Tarefa: crie um texto com $nome e $valor e substitua usando Template.substitute.
Conceitos: string.Template, substitute, leitura de arquivo.
'''
import string
from pathlib import Path

CAMINHO = Path(__file__).parent / 'ex87.txt'

with open(CAMINHO, 'r', encoding='utf8') as arquivo:
    string_ = arquivo.read()

dados = dict(
    nome='Paulo',
    valor='R$1000'
)

template = string.Template(string_)
print(template.substitute(dados))