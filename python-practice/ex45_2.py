'''
Tarefa: implemente make_validator(min_len) que retorna uma função que valida
se uma string tem comprimento >= min_len. Use a closure para “fixar” min_len.
Conceitos: closures, funções que retornam funções.
'''
import random

def make_validator(min_len: int):
    def inner(string_: str):
        return len(string_) >= min_len
    return inner

str_maior_10 = make_validator(10)
string_list = ['Lorem Ipsum', 'Dolor', 'Amet']
string_ = random.choice(string_list)

if str_maior_10(string_):
    print(f'A string "{string_}" tem pelo menos 10 caracteres')
else:
    print(f'A string "{string_}" tem menos de 10 caracteres')
