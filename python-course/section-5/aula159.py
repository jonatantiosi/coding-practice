# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass


@dataclass(order=True, repr=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome:  str

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     print('Init')
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    # def __post_init__(self):
    #     print('Pós init')
    # self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True)
    # Sem o order precisaria ser algo do tipo
    # ordenadas = sorted(lista, reverse=True, key=lambda p:p.nome)

    print(ordenadas)
    # pessoa_1 = Pessoa('Luiz', 'Otavio')
    # pessoa_1.nome = 'Maria'
    # pessoa_2 = Pessoa('Luiz', 30)
    # print(pessoa_1)
    # pessoa_1.nome_completo = 'Maria Helena Figueiredo'
    # print(pessoa_1 == pessoa_2)
    # print(pessoa_1.nome_completo)
