'''
Tarefa: crie build_person(**kwargs) que aceita nome, idade, altura e devolve 
dicionário com apenas essas chaves (valide tipos: idade int >=0, altura 
float >0). Lance ValueError para entradas inválidas.
Conceitos: **kwargs, validação de entrada, raise.
'''

def build_person(**kwargs)
    for value in kwargs:
        if isinstance(value, int) and value > 0:
            idade = value
        elif isinstance(value, float) and value > 0:
            altura = value
        elif isinstance(value, str):
            nome = value
        else:
            raise ValueError('Entrada inválida')
    return {"P"}
