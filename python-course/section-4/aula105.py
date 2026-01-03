'''
decoradora com parametros
'''

def decorator_fabric(a=None, b=None, c=None):
    def function_fabric(func):
        print('decoradora1')
        
        def aninhada(*args, **kwargs):
            print('parametros do decorador', a, b, c)
            print('aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return function_fabric

@decorator_fabric(1, 2, 3) 
def soma(x, y):
    return x + y


decoradora = decorator_fabric()
multiplica = decoradora(lambda x,y: x*y)

dez_vezes_cinco = multiplica(10,5)

print(dez_vezes_cinco)

# dez_mais_cinco = soma(10, 5)
# print(dez_mais_cinco)