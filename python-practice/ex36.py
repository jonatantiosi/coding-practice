'''
Crie uma classe ContadorDeChamadas com atributo contador.
Implemente __call__() para que toda vez que o objeto for chamado, ele aumente o
contador e imprima o número de chamadas.
'''


class ContadorDeChamadas:
    def __init__(self):
        self.contador = 0

    def __call__(self):
        '''Aumenta em 1 o contador toda vez que chamando'''
        self.contador += 1
        str_contador = str(self.contador)
        print(str_contador)


contador = ContadorDeChamadas()

for i in range(10):
    contador()
