'''
Tarefa: crie decorator @validate_strings que verifica se todos os argumentos
posicionais são strings; caso contrário TypeError. Use-o numa função que
concatena strings.
Conceitos: decorators, *args, isinstance.
'''


def validate_strings(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError("Not string")
        for value in kwargs.values():
            if not isinstance(value, str):
                raise TypeError("Not string")

        return func(*args, **kwargs)
    return wrapper


@validate_strings
def concatenate_strings(*args, **kwargs):
    string_ = ' '.join(args)
    for key, value in kwargs.items():
        string_ += ' ' + value
    return string_


print(concatenate_strings('Lorem', 'Ipsum', 'Dolor', kwarg1='Amet'))
# concatenate_strings('Lorem', 'Ipsum', 11, kwarg1='Amet')  # generates error
