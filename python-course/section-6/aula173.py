# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~')
PICTURES = os.path.join(HOME, 'Pictures')
PASTA_ORIGINAL = os.path.join(PICTURES, 'SolidColors')
NOVA_PASTA = os.path.join(PICTURES, 'SolidColorsCopy')

os.makedirs(NOVA_PASTA, exist_ok=True)

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file_ in files:
        caminho_arquivo = os.path.join(root, file_)
        # print(caminho_arquivo)
        # print(file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file_
            # sem isso não pegaria os diretórios
            )
        # print(caminho_novo_arquivo)
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
