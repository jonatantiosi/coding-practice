'''
funcoes decoradoras
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

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('parametro deve ser string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('lorem ipsum')
print(invertida)