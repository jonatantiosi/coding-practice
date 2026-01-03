# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
import locale
from datetime import datetime
import string
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula183.txt'

locale.setlocale(locale.LC_ALL, '')
# padrao do sistema


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='Jonatan',
    valor=converte_para_brl(1_234_567),
    data=data.strftime('%d/%m/%Y'),
    empresa='J.P. Programming',
    telefone='55 (11) 912345678'
)

# import json
# print(json.dumps(dados, indent=2, ensure_ascii=False))

# texto = '''
# Prezado(a) $nome,

# Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.\
#  Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone\
#  $telefone.

# Atenciosamente,

# ${empresa},
# Abraços
# '''

# template = string.Template(texto)

# print(template.safe_substitute(dados))
# print(template.substitute(dados))

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))
 

# exemplo de customizacao do template
# class MyTemplate(string.Template):
#     delimiter = '%'
