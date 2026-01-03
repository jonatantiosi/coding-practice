'''
Tarefa: implemente make_validator(min_len) que retorna uma função que valida
se uma string tem comprimento >= min_len. Use a closure para “fixar” min_len.
Conceitos: closures, funções que retornam funções.
'''


def make_validator(min_len):
    def inner(string):
        return len(string) >= min_len
    return inner


string_over_10 = make_validator(10)
string_over_6 = make_validator(6)

print(string_over_10('Lorem Ipsum'))
print(string_over_6('Lorem'))
