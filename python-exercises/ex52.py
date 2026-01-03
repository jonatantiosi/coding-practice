'''
Tarefa: modele Biblioteca (agregadora) e Livro. A biblioteca mantém lista de
Livro (objetos). Implemente adicionar(livro), remover_por_titulo(titulo) e
listar(). Mostre que Livro existe independente.
Conceitos: relações entre classes (associação/agregação).
'''


class Biblioteca():

    def __init__(self):
        self.lista_livros = []

    def adicionar(self, livro: 'Livro'):
        '''permite adicionar apenas um livro a biblioteca'''
        self.lista_livros.append(livro)

    def remover_por_titulo(self, titulo):
        '''procura livro na lista de livros e remove, imprimindo mensagem'''
        # i = 0 (legacy, substituido por enumerate)
        for indice, livro in enumerate(self.lista_livros):
            if titulo == livro.titulo:
                removed = self.lista_livros.pop(indice)
                # i += 1
                print(f'Livro "{removed.titulo}" removido\n')

    def listar(self):
        '''itera e imprime lista_livros'''
        for indice, livro in enumerate(self.lista_livros):
            print(f'{indice + 1}. {livro.titulo}')
        print()


class Livro():

    def __init__(self, titulo):
        self.titulo = titulo


biblioteca1 = Biblioteca()

livro1 = Livro('Lorem')
livro2 = Livro('Ipsum')
livro3 = Livro('Dolor')
livro4 = Livro('Amet')

biblioteca1.adicionar(livro1)
biblioteca1.adicionar(livro2)
biblioteca1.adicionar(livro3)

biblioteca1.listar()
biblioteca1.remover_por_titulo('Ipsum')
biblioteca1.listar()

# mostrado que livro existe independente de biblioteca
print(f'"{livro4.titulo}" não está em nenhuma biblioteca')
print(f'"{livro1.titulo}" está em biblioteca1')
