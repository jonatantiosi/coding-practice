'''
100 — Verificar quantidade de argumentos
Tarefa: exiba “Faltam argumentos” caso o usuário passe menos de dois argumentos.
Caso passe dois ou mais, imprima ambos.
Conceitos: len(sys.argv), fatiamento, IndexError.
'''
import sys

quantidade_de_argumentos = len(sys.argv)

if quantidade_de_argumentos < 3:
    print('Faltam argumentos')
else:
    i = 1
    for arg in sys.argv[1::]:
        print(f'Argumento {i}: {arg}')
        i += 1