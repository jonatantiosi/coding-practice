'''
18. Composição

Crie a classe Computador que compõe objetos das classes Processador e MemoriaRAM:

    Quando o Computador for deletado, exiba uma mensagem indicando que os componentes também estão sendo apagados.

    Dica: use __del__ para simular esse comportamento, como na aula de composição.
'''

class Computador:
    def __init__(self, nome):
        self.nome = nome
        self.processador = []
        self.memoria_ram = []

    def registrar_processador(self, modelo_processador):
        self.processador.append(Processador(modelo_processador))

    def registrar_memoria_ram(self, modelo_memoria_ram):
        self.memoria_ram.append(MemoriaRAM(modelo_memoria_ram))

    def __del__(self):
        print(f'Apagando {self.nome}...')
    

class Processador:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self):
        print(f'Apagando {self.nome}...')

class MemoriaRAM:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self):
        print(f'Apagando {self.nome}...')


computador_1 = Computador('Computador 1')
computador_1.registrar_memoria_ram('DDR4')
computador_1.registrar_processador('Intel Core i7')

del computador_1

