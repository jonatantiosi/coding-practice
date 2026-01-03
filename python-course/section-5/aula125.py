# Atributos de classe

# ANO_ATUAL = 2025

class Pessoa:
    atributo = 'value'
    ano_atual = 2025

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birth_year(self):
        return Pessoa.ano_atual - self.idade
        # cuidado com uso de self.ano atual, pode buscar nas instancias
        # antes de buscar na classe
    
pessoa_1 = Pessoa('Jonatan', 23)
pessoa_2 = Pessoa('Miriam', 45)

# Pessoa.ano_atual = 1
# Atributo atrelado a classe, muda todas as instancias

print('Ano atual:', Pessoa.ano_atual)
print(pessoa_1.get_birth_year())
print(pessoa_2.get_birth_year())