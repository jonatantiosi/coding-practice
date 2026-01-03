'''
21. Herança Múltipla

Crie três classes:

    DispositivoEletronico com método ligar()

    ConectadoRede com método conectar()

    Smartphone que herda das duas e implementa método usar()

    Instancie Smartphone e chame os métodos ligar, conectar e usar.
'''
class DispositivoEletronico():

    def __init__(self):
        self.status = 0

    def ligar(self):
        print(f'{self.nome} ligado')
        self.status = 1

class ConectadoRede():

    def __init__(self):
        self.status = 0

    def conectar(self):
        print(f'{self.nome} conectado')
        self.status = 1
    
class Smartphone(DispositivoEletronico, ConectadoRede):

    def __init__(self, nome):
        self.nome = nome
    
    def usar(self):
        print(f'{self.nome} está em uso')

smartphone_1 = Smartphone('S23')

smartphone_1.ligar()
smartphone_1.conectar()
smartphone_1.usar()