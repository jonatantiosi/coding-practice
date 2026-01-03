'''
Tarefa: faça @log(prefix) que imprime "[prefix] Chamando func" antes da chamada
e "[prefix] Retornou: X" após, retornando o resultado normalmente.
Conceitos: decorator factory, functools.wraps (opcional).
'''


def decorator_factory(prefix):
    def function_factory(func):

        def inner(*args, **kwargs):
            print(f'{prefix} chamando func')
            res = func(*args, **kwargs)
            print(f'{prefix} Retornou: {res}')
            return res
        return inner
    return function_factory


@decorator_factory('Loading...')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print('Resultado', dez_mais_cinco)
