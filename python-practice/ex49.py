'''
Tarefa: crie Pessoa(nome, idade). Implemente __repr__ elegante e __lt__ por
idade. Depois ordene uma lista de pessoas e imprima.
 Conceitos: dunder methods __repr__, __lt__, sorted().
'''


class Pessoa:

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.nome}, {self.idade} anos'

    def __lt__(self, other: 'Pessoa'):
        return self.idade < other.idade


pessoa_1 = Pessoa('Jonatan', 24)
pessoa_2 = Pessoa('Marcio', 46)
pessoa_3 = Pessoa('Miriam', 45)
pessoa_4 = Pessoa('Paulo', 34)

lista_pessoas = [pessoa_1, pessoa_2, pessoa_3, pessoa_4]
lista_pessoas_ordenada = sorted(
    lista_pessoas,  # key=lambda pessoa: pessoa.idade (nao necessario)
)

print(lista_pessoas_ordenada)
