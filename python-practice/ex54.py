'''
Tarefa: crie read_lines(path) generator que lê um arquivo linha a linha (yield)
e aplica strip(). Em outro lugar, consuma apenas as 5 primeiras linhas (não
leia tudo).
Conceitos: generators, yield, I/O eficiente.
'''

PATH = 'C:/Users/Jonatan/Desktop/PythonCoding/exercicios_extra/chatgpt/text.txt'


def read_lines(path):
    with open(path, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            yield linha.strip()


for i, linha in enumerate(read_lines(PATH)):
    if i == 5:
        break
    print(linha)
