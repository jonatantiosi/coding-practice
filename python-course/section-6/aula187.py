# sys.argv - Executando arquivos com argumentos no sistema

# e.g. terminal: python .\AulasUdemy\aula187.py -a
import sys

argumentos = sys.argv
quantidade_argumentos = len(argumentos)
# print(f'{quantidade_argumentos} argumentos: {sys.argv}')

if quantidade_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1::]}')
        print(f'Argumento 1: {argumentos[1]}')
        print(f'Argumento 2: {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')