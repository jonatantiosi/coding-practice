'''
27. Dunder Methods — Comparações
Crie a classe Pessoa, com atributos nome e idade.
Implemente:
 __repr__ para mostrar o nome e idade.
 __lt__ para comparar pessoas pela idade.
 __eq__ para comparar se duas pessoas têm a mesma idade.
Teste com objetos diferentes e use operadores como < e ==.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}: {self.nome}, {self.idade} anos.'
    
    def __lt__(self, other: 'Pessoa'):
        return self.idade < other.idade
    
    def __eq__(self, other: 'Pessoa'):
        return self.idade == other.idade
    


pessoa_1 = Pessoa('Jonatan', 23)
pessoa_2 = Pessoa('Miriam', 46)
pessoa_3 = Pessoa('Nathalia', 23)

print(pessoa_1.__repr__())
print(pessoa_2.__repr__())
print(pessoa_3.__repr__())


print(pessoa_1 < pessoa_2)
print(pessoa_1 == pessoa_3)