'''
decoradores "syntax sugar"
'''


def criar_funcao(func):
    # funcao decoradora
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna
    # retornada sem execucao

@criar_funcao
def inverte_string(string):
    # mesmo funcionamento mas a funcao muda pra interna
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('parametro deve ser string')


invertida = inverte_string('lorem ipsum')
print(invertida)