# classes decoradoras (Decorator classes)

# class Multiplicar:
#     def __init__(self, func):
#         print('init', func)
#         self.func = func
#         self._multiplicador = 10
        
#     def __call__(self, *args, **kwargs):
#         print(*args, **kwargs)
#         resultado = self.func(*args, **kwargs)
#         return resultado * self._multiplicador

# @Multiplicar
# def soma (x, y):
#     return x + y

# dois_mais_quatro = soma(2, 4)
# print(dois_mais_quatro)

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador
        
    def __call__(self, func):
        def inner(*args, **kwargs): 
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return inner

@Multiplicar(10)
def soma (x, y):
    return x + y

dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)