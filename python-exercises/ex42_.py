'''
Tarefa: crie build_person(**kwargs) que aceita nome, idade, altura e devolve
dicionário com apenas essas chaves (valide tipos: idade int >=0, altura
float >0). Lance ValueError para entradas inválidas.
Conceitos: **kwargs, validação de entrada, raise.
'''


def valida_idade(idade):
    '''idade: int >= 0 '''
    if isinstance(idade, int) and idade >= 0:
        return
    raise ValueError


def valida_altura(altura):
    '''altura: float(m) > 0'''
    if isinstance(altura, float) and altura > 0:
        return
    raise ValueError


def build_person(**kwargs):
    '''
    retorna dicionário com nome, idade e altura. argumentos devem ser nomeados
    '''
    pessoa = {
        'nome': None,
        'idade': None,
        'altura': None
        }
    for chave, value in kwargs.items():
        match chave:
            case 'nome':
                pessoa['nome'] = value
            case 'idade':
                valida_idade(value)
                pessoa['idade'] = value
            case 'altura':
                valida_altura(value)
                pessoa['altura'] = value
    return pessoa


''' Testes'''
person_1 = build_person(idade=24, altura=1.8, nome='Jonatan')
print(person_1)
try:
    person_2 = build_person(nome='Paulo', altura=0, idade=-60)
except ValueError:
    print('Idade ou altura inválida')
