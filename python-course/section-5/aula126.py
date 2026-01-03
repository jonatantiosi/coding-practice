# __dict__ e vars para atributos de instância

class Pessoa:
    atributo = 'value'
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birth_year(self):
        return Pessoa.ano_atual - self.idade
    
dados = {'nome': 'Paulo', 'idade': 23}
pessoa_1 = Pessoa(**dados)
print(pessoa_1.__dict__)


# del pessoa_1.nome
# print(pessoa_1.nome)

pessoa_1.__dict__['nome'] = 'Jonatan'
print(vars(pessoa_1))
# chama o dicionario
