'''
102 — Flag booleana com argparse
Tarefa: adicione ao programa anterior uma flag -v/--verbose que imprime “Modo
verboso ON” somente quando presente.
Conceitos: action="store_true", flags booleanas, combinação de argumentos.
'''
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-n', '--nome'
)

parser.add_argument(
    '-v', '--verbose',
    action='store_true'
)

args = parser.parse_args()

if args.nome is None:
    print('Nenhum argumento passado')
else:
    print(args.nome)

if args.verbose:
    print('Modo verboso ON')