'''
Tarefa: implemente ArquivoSeguro(path, modo) com __enter__/__exit__ que
abre/fecha arquivo; no __exit__, se houve exceção, escreva uma linha no console
e suprima a exceção (retorne True). Teste com um with que provoca erro dentro.
Conceitos: context manager, gerenciamento de recursos, controle de exceções.
'''

CAMINHO = (
    r'C:\Users\Jonatan\Desktop\PythonCoding\exercicios_extra\chatgpt'
    r'\text.txt'
)


class ArquivoSeguro():

    def __init__(self, path, modo):
        self.path = path
        self.modo = modo

    def __enter__(self):
        print('Abrindo...')
        self.arquivo = open(self.path, self.modo, encoding='utf-8')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Erro: {exc_val}')
        print('Fechando')
        self.arquivo.close()
        return True


with ArquivoSeguro(CAMINHO, 'r') as arquivo:
    a = 1/0
