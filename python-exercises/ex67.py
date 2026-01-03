'''
67 — Manipulando caminhos de arquivos
Tarefa: crie um caminho 'Documentos/Projetos/teste.txt' com os.path.join,
depois exiba:
o diretório e o arquivo separadamente, a extensão, e o caminho absoluto.
Conceitos: os.path.join, os.path.split, os.path.splitext, os.path.abspath.
'''
import os

caminho = os.path.join('Documentos', 'Projetos', 'teste.txt')

diretorio, arquivo = os.path.split(caminho)
print(diretorio)
print(arquivo)

_, extension = os.path.splitext(caminho)
print(extension)

caminho_absoluto = os.path.abspath(caminho)
print(caminho_absoluto)
