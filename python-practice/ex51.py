'''
51 — Properties e validação
Tarefa: classe Produto com atributo privado _preco. Use @property e
@preco.setter para garantir que preço >= 0 (senão ValueError).
Teste leitura/escrita.
Conceitos: encapsulamento, properties.
'''


class Produto():

    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError('Preço deve ser um número positivo')
        self._preco = novo_preco


produto_1 = Produto(213)
print(produto_1.preco)

produto_1.preco = produto_1.preco * 1.1
print(produto_1.preco)

produto_1.preco = -5
print(produto_1.preco)
