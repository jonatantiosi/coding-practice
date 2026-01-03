'''
101 — ArgumentParser básico
Tarefa: crie um script que defina um argumento -n (ou --nome) e imprima o valor
recebido.
Se nada for passado, exiba uma mensagem informando a ausência.
Conceitos: argparse.ArgumentParser, add_argument, parse_args.
'''
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-n', '--nome'
)

args = parser.parse_args()

if args.nome is None:
    print('Nenhum argumento passado')
else:
    print(args.nome)