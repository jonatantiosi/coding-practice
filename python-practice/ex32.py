'''
Crie uma classe Produto com nome e preco, e use o decorator @add_repr para que
o print(produto) retorne algo como:

Produto({'nome': 'Teclado', 'preco': 99.90})
'''


def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return f'{class_name}({class_dict})'
    cls.__repr__ = my_repr
    return cls


@add_repr
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto = Produto('lorem', 50.00)

print(produto)
