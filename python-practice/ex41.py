'''
Tarefa: escreva sum_safe(*args) que soma apenas números (ints/floats)
ignorando outros tipos e retorna a soma.
Conceitos: *args, isinstance, loop.
Dica: use isinstance(x, (int, float)).
'''
import random


def sum_safe(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (float, int)):
            total += arg
    return total


res = sum_safe(
    random.randint(0, 1000),
    random.randint(0, 1000),
    ['list', 0],
    'lorem',
    random.randint(0, 1000)
)

print(res)
