'''
92 — Leitura de HTML + Template
Tarefa: leia um arquivo HTML, carregue em um Template e substitua $nome por
outro nome qualquer.
Conceitos: I/O com arquivo HTML, Template.substitute.
'''
from string import Template
from pathlib import Path

CAMINHO_ARQUIVO_HTML = Path(__file__).parent / 'ex92.html'

with open(CAMINHO_ARQUIVO_HTML, 'r', encoding='utf8') as arquivo:
    string_html = arquivo.read()
    template = Template(string_html)
    mensagem = template.substitute(nome='Paulo')

print(mensagem)