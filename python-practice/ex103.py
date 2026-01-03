'''
103 — Receber vários valores em um argumento
Tarefa: crie um argumento -t que aceite múltiplos valores usando action="append"
e exiba a lista final.
Conceitos: action="append", múltiplos valores, parser de linha de comando.
'''
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-t',
    action='append'  
)

args = parser.parse_args()

print(args.t)