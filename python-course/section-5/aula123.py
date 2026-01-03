# Escopo da classe e de métodos da classe
# Namespace


class Animal:
    # nome = 'Leao'

    def __init__(self, nome):
        self.nome = nome
        var = 'valor'

    def comendo(self, alimento):
        # print(var)
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

# print(Animal.nome)
leao = Animal(nome='Leão')

print(leao.nome)

print(leao.executar('carne'))