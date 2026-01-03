'''
Tarefa: Computador que cria internamente Processador e Ram (composição).
Ao deletar Computador mostre via __del__ que componentes também são apagados.
(Observação: comportamento do __del__ pode variar, é didático).
 Conceitos: composição, ciclo de vida, __del__.
 '''


class Computador:

    def __init__(self, processador: 'Processador', ram: 'Ram'):
        self.processador = processador
        self.ram = ram

    def __del__(self):
        print(f'Registro de {self.processador.nome} apagado')
        print(f'Registro de {self.ram.nome} apagado')


class Processador:

    def __init__(self, nome):
        self.nome = nome


class Ram:

    def __init__(self, nome):
        self.nome = nome


computador1 = Computador(Processador('intel core i7'), Ram('DDR4 16GB'))
computador2 = Computador(Processador('ryzen 5 5600g'), Ram('DDR4 8GB'))

del computador1
del computador2
