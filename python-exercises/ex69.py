'''
69 — Caminhando por diretórios
Tarefa: percorra o diretório C:/Users/SeuNome/Pictures com os.walk, mostrando o
nome de cada pasta e o caminho completo de cada arquivo encontrado.
Conceitos: os.walk, tupla (root, dirs, files), iteração recursiva.
'''
import os

CAMINHO = os.path.join('C:\\Users', 'Jonatan', 'Pictures')

for root, dirs, files in os.walk(CAMINHO):
    print('Pasta atual:', root)
    for dir in dirs:
        print(' ', dir)
    for file in files:
        caminho_completo_file = os.path.join(root, file)
        print('  ', caminho_completo_file)
      
