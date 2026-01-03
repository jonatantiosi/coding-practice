'''
Crie uma classe Livro com os seguintes comportamentos:
 Um atributo privado _titulo.
 Uma @property chamada titulo que retorna o título.
 Um setter para titulo que imprime "Título alterado para: ..." sempre que o valor for modificado.
 Instancie um objeto e altere o título.
'''

class Livro: 
    def __init__(self, titulo=None):
        self._titulo = titulo
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, novo_titulo):
        print(f'Título alterado para: "{novo_titulo}"')
        self._titulo = novo_titulo

livro_1 = Livro('Don Juan')

print(livro_1.titulo)

livro_1.titulo = 'O conde de Monte Cristo'

print(livro_1.titulo)