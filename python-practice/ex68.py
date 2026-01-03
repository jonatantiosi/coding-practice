'''
68 — Listando pastas e arquivos
Tarefa: percorra o diretório 'C:/Users/SeuNome/Pictures', mostrando apenas as
pastas e os arquivos dentro de cada uma, com indentação.
Conceitos: os.listdir, os.path.isdir, os.path.join, laços aninhados.
'''
import os

caminho_pictures = os.path.join('C:', r'\Users', 'jonatan', 'Pictures')
# eu acho que nao era pra fazer assim
if os.path.isdir(caminho_pictures):
    pastas = os.listdir(caminho_pictures)

    for pasta in pastas:
        print(pasta)
        caminho_pasta = os.path.join(caminho_pictures, pasta)
        if os.path.isdir(caminho_pasta):
            pasta_arquivos = os.listdir(caminho_pasta)
            for arquivo in pasta_arquivos:
                print('  ', arquivo)
else:
    print('Caminho incorreto')
