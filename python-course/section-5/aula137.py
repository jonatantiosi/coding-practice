class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0


print(f'Nome: {fusca.nome}.\nFabricante: {fusca.fabricante.nome}.\nMotor: {fusca.motor.nome}')
print()

fiat_uno = Carro('Uno')
fiat = Fabricante('Volkswagen')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0

print(f'Nome: {fiat_uno.nome}.\nFabricante: {fiat_uno.fabricante.nome}.\nMotor: {fiat_uno.motor.nome}')
print()