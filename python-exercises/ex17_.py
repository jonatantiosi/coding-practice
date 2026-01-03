'''
Crie um sistema de agregação com as classes Biblioteca e Livro:

    A biblioteca pode agregar vários livros.

    Os livros devem poder existir independentemente da biblioteca.

    Crie 2 livros, adicione à biblioteca, e mostre a lista de livros.
'''


class Livro():
    def __init__(self, titulo):
        self.titulo = titulo

    def __repr__(self):
        return f'{self.titulo}'


class Biblioteca():
    def __init__(self):
        self.lista_livros = []

    def adicionar_livro(self, livro: Livro):
        self.lista_livros.append(livro)

    def listar_livros(self):
        print('Livros:')
        for livro in self.lista_livros:
            print(f'"{livro}"')


biblioteca_1 = Biblioteca()
livro_1 = Livro('Sherlock Holmes')
livro_2 = Livro('Hunger Games')
livro_3 = Livro('The Witcher')


biblioteca_1.adicionar_livro(livro_1)
biblioteca_1.adicionar_livro(livro_2)
biblioteca_1.adicionar_livro(livro_3)

biblioteca_1.listar_livros()
