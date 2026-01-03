'''
18. Composição
Crie a classe Computador que compõe objetos das classes Processador e
MemoriaRAM:
Quando o Computador for deletado, exiba uma mensagem indicando que os
componentes também estão sendo apagados.
Dica: use __del__ para simular esse comportamento, como na aula de composição.
'''


class Processador:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self):
        print(f'Processador {self.nome} deletado.')


class MemoriaRam:
    def __init__(self, nome):
        self.nome = nome

    def __del__(self):
        print(f'Memória {self.nome} deletada.')


class Computador:
    def __init__(self, processador: str, memoria_ram: str):
        self.processador = Processador(processador)
        self.memoria_ram = MemoriaRam(memoria_ram)


computador_1 = Computador('AMD Ryzen 5 3400G', 'Corsair 16GB')

del computador_1
