# Entendendo self em classes Python
# Convenção de referência à própria instância
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Car:
    def __init__(self, nome):
        # self.nome = 'Fusca' # hard coded
        self.nome = nome

    def accelerate(self):
        print(f'{self.nome} acelerando...')

fusca = Car('fusca')
celta = Car(nome='celta')

# print(celta.nome)
# print(fusca.nome)

# fusca.accelerate()
celta.accelerate()
Car.accelerate(fusca) # incomum