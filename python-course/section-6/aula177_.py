from pathlib import Path
# from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)
# print(caminho_arquivo.parent)
# print(caminho_arquivo.parent.parent)
# print(caminho_arquivo.parent.parent.parent)

ideias = caminho_arquivo.parent / 'Ideias'
# print(ideias)
# print(ideias / 'arquivo.txt')

arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch()
# print(arquivo)
# arquivo.write_text('Lorem')
# arquivo.write_text('Ipsum')  # Só fica a última linha
# print(arquivo.read_text())
# arquivo.unlink()

caminho_arquivo_dois = Path.home() / 'Desktop' / 'arquivo.txt'
# with caminho_arquivo_dois.open('a+') as file:
#     file.write('Primeira linha\n')
#     file.write('Segunda linha\n')

# print(caminho_arquivo_dois.read_text())

# caminho_arquivo_dois.write_text('')

caminho_pasta = Path.home() / 'Desktop' / 'PastaExemplo'
caminho_pasta.mkdir(exist_ok=True)
caminho_subpasta = caminho_pasta / 'SubpastaExemplo'
caminho_subpasta.mkdir(exist_ok=True)
caminho_arquivo_tres = caminho_subpasta / 'arquivo.txt'
caminho_arquivo_tres.touch()
caminho_arquivo_tres.write_text('Amet')


# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    # if file.is_file()
    # if file.is_dir()
    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Lorem Ipsum')
        text_file.write(f'file_{i}.txt')

# rmtree(caminho_pasta)


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()
    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
