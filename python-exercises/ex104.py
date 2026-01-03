''' 
104 — Script com chave/valor
Tarefa: crie um script que receba um argumento -m seguido de uma string e
imprima:
Mensagem recebida: <valor>
Caso nada seja passado, avise o usuário.
Conceitos: argumentos posicionais x opcionais, metavar.
'''

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-m', '--string',
    metavar='STRING'
)

args = parser.parse_args()

if args.string is None:
    print('Nenhum argumento passado')
else:
    print('Mensagem recebida:', args.string)