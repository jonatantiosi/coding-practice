'''
24. Property Abstrata

Crie uma classe abstrata ProdutoBase com uma property preco abstrata e um setter abstrato para preco.
Crie uma subclasse Produto que implemente esses métodos e valide que o preço seja sempre um número positivo.
Teste com objetos.
'''


from abc import ABC, abstractmethod

class ProdutoBase(ABC):
    def __init__(self, preco):
        self._preco = None
        self.preco = preco
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    @abstractmethod
    def preco(self, value):
        ...

class Produto(ProdutoBase):

    def __init__(self, preco):
        super().__init__(preco)

    @ProdutoBase.preco.setter
    def preco(self, preco): 
        if preco > 0:
            self._preco = preco
        else:
            raise ValueError('Preço deve ser um número positivo')


produto_1 = Produto(25.00)
print(produto_1.preco) 

produto_2 = Produto(-2)
print(produto_2.preco)