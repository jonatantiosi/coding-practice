# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Car:
    def __init__(self, nome):
        # self.nome = 'Fusca' # hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} acelerando...')

fusca = Car('fusca')
celta = Car(nome='celta')

# print(celta.nome)
# print(fusca.nome)

fusca.acelerar()
celta.acelerar()