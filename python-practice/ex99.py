'''
99 — Ler argumentos simples com sys.argv
Tarefa: escreva um programa que, ao receber argumentos pelo terminal, exiba:

a lista completa de argumentos,
o primeiro argumento,
se nenhum argumento for passado, exiba uma mensagem apropriada.

Conceitos: sys.argv, contagem de argumentos, tratamento com try/except.
'''
import sys

quantidade_argumentos_recebidos = len(sys.argv)

if quantidade_argumentos_recebidos <= 1:
    print('Nenhum argumento recebido')
else:
    primeiro_argumento = sys.argv[1]
    lista_completa_argumentos = sys.argv
    print('Primeiro argumento:', primeiro_argumento)
    print('Lista completa de argumentos:', lista_completa_argumentos)
