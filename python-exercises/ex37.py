'''
Implemente uma classe MultiplicadorDinamico que funcione assim:

@MultiplicadorDinamico(3)
def quadrado(n):
    return n * n

E multiplique o resultado pelo número passado no decorator.
'''
from functools import wraps


class MultiplicadorDinamico:
    def __init__(self, multiplicador):
        self.multiplicador = multiplicador

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * self.multiplicador
        return wrapper


@MultiplicadorDinamico(3)
def quadrado(n):
    return n * n


print(quadrado(4))
