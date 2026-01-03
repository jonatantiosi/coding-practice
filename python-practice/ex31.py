'''
31. Context Manager com Classe
Crie a classe ArquivoSeguro com os métodos __enter__ e __exit__, que:
 Abre um arquivo no modo especificado.
 Fecha o arquivo no __exit__.
 Se ocorrer um erro, ele deve mostrar a mensagem, mas não quebrar o código (retornar True).
Use com with ArquivoSeguro('teste.txt', 'w') as f: e teste escrita no arquivo.
'''

CAMINHO = r'C:\\Users\\Jonatan\\Desktop\\PythonCoding\\exercicios_extra\\chatgpt\\ex31_log.txt'

class SafeFile:
    def __init__(self, archive_path, mode):
        self.archive_path = archive_path
        self.mode = mode
        self._archive = None

    def __enter__(self):
        self._archive = open(self.archive_path, self.mode, encoding='utf8')
        return self._archive

    def __exit__(self, class_exception, exception_, traceback_):
        self._archive.close()
        if class_exception:
            print('An error occurred:', exception_)
            return True


with SafeFile(CAMINHO, 'w') as f:
    f.write('Line1\n')
    1/0