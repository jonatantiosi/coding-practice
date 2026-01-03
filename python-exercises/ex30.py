'''
30. Context Manager com Função

Implemente um context manager com @contextmanager chamado abrir_log(), que abre um arquivo de log para escrita.
Dentro do with, escreva duas mensagens.
Garanta que o arquivo é fechado corretamente mesmo se ocorrer um erro.
'''

from contextlib import contextmanager

@contextmanager
def open_log(caminho_arquivo, modo):
    try:
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as error_:
        print('ocorreu erro:', error_)
    finally:
        arquivo.close()

with open_log(r'C:\\Users\\Jonatan\\Desktop\\PythonCoding\\exercicios_extra\\chatgpt\\ex30_log.txt', 'a') as arquivo:
    arquivo.write('line1\n')
    arquivo.write('line2\n')
