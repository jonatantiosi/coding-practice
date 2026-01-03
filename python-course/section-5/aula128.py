# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:

    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # decorator    
    def metodo_de_classe(cls):
        print('lorem')
        
    @classmethod # decorator  
    # factory method  
    def criar_23_anos(cls, nome):
        return cls(nome, 23)
    
    @classmethod # decorator  
    # factory method  
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

pessoa_1 = Pessoa('Paulo', 34)
pessoa_2 = Pessoa.criar_23_anos('Jonatan')
pessoa_3 = Pessoa.criar_sem_nome(45)

print(Pessoa.ano)

Pessoa.metodo_de_classe()
# funciona sem parâmetros

print(pessoa_2.nome, pessoa_2.idade)
print(pessoa_3.nome, pessoa_3.idade)
