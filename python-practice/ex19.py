'''
19. Herança Simples

Implemente a classe Funcionario com atributos nome e salario. Crie uma subclasse Gerente que herda de Funcionario e adiciona o atributo departamento. Faça um método exibir_dados() na subclasse que exiba todos os dados.
'''

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = round(salario, 2)

class Gerente(Funcionario):

    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    
    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: R${self.salario}')
        print(f'Departamento: {self.departamento}')

funcionario_1 = Funcionario('Miriam', 3242.34)
funcionario_2 = Gerente('Jonatan', 6655.56, '02')

funcionario_2.exibir_dados()