'''
Crie um sistema de agregação com as classes Biblioteca e Livro:

    A biblioteca pode agregar vários livros.

    Os livros devem poder existir independentemente da biblioteca.

    Crie 2 livros, adicione à biblioteca, e mostre a lista de livros.
'''

class Biblioteca:

    lista_livros = []

    def __init__(self):
        pass

    def nome_classe(self):
        print(self.__class__.__name__)

    def mostrar_lista(self):
        for i, item in enumerate(self.lista_livros):
            print(f'{i+1}. {item}')


class Livro(Biblioteca):
    def __init__(self, nome):
        self.nome = nome
        self.lista_livros.append(self.nome)
               

Biblioteca_1 = Biblioteca()
livro_1 = Livro('O Conde de Monte Cristo')
livro_2 = Livro('Don Juan')

livro_2.mostrar_lista()