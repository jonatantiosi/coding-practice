'''
Tarefa: reimplemente MultiplicaPorCinco como classe decoradora (igual ao
exercício anterior) mas opcionalmente permita passar o multiplicador no
construtor: @Multiplicador(7).
 Conceitos: __init__, __call__, decoradores parametrizados por classe.
'''


def multiplicador(num=1):
    def function_factory(func):

        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return res * num
        return inner
    return function_factory


@multiplicador(7)
def multiplica(x, y):
    return x * y


multiplica_10_mais_5 = multiplica(10, 5)
print('Resultado', multiplica)
