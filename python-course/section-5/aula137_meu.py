# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor_carro = 'Desconhecido'

    @property
    def motor_carro(self):
        return self._motor_carro

    @motor_carro.setter
    def motor_carro(self, motor):
        self._motor_carro = motor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.lista_carros = []
    
    def registrar_carros(self, *carros):
        for carro in carros:
            self.lista_carros.append(carro)

    def listar_carros(self):
        print(f'{self.nome}:')
        for carro in self.lista_carros:
            print(f'Carro: {carro.nome}. Motor: {carro._motor_carro}')

fabricate_1 = Fabricante('Chevrolet')
carro_1 = Carro('Corsa')
carro_2 = Carro('Prisma')
carro_3 = Carro('Onix')
motor_1 = '1.0 MPFI'
motor_2 = '1.0 SPE/4'

carro_1.motor_carro = motor_1
carro_2.motor_carro = motor_2
carro_3.motor_carro = motor_2

fabricate_1.registrar_carros(carro_1, carro_2, carro_3)

fabricate_1.listar_carros()