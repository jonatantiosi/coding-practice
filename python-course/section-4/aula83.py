a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
} 

# a, b = pessoa # chaves
# c, d = pessoa.values() # valores
# (e, f), (g, h) = pessoa.items() # tupla com os dois
# print(a, b)
# print(c, d)
# print(f'{e}: {f}')

dados_completos_pessoa = {**pessoa, **dados_pessoa}
# print(dados_completos_pessoa)

#kwargs

def mostro_argumentos_nomeados(*args, **kwargs):
    print('nao nomeados:\n', args)
    print()

    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

# mostro_argumentos_nomeados(1, 99, nome='jonatan', qlq=123)

mostro_argumentos_nomeados(**dados_completos_pessoa)

configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,

}

mostro_argumentos_nomeados(**configs)