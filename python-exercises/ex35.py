'''
Implemente uma classe MultiplicaPorCinco, que pode ser usada como decorator
para multiplicar o resultado da função por 5:

@MultiplicaPorCinco
def dobro(x):
    return x * 2

Teste com diferentes entradas.
'''


class MultiplicaPorCinco:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs) * 5


@MultiplicaPorCinco
def dobro(num):
    return num * 2


print(dobro(10))
