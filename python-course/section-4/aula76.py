'''
dicionarios
par de 'chave' e 'valor'
'''

pessoa = {
    'nome': 'Jonatan Paulo',
    'sobrenome': 'Tiosi Santana',
    'idade': 23,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}

# pessoa = dict(nome='jonatan', sobrenome='tiosi')
# menos usada

# print(pessoa, type(pessoa))

print(pessoa['endereços'][0]['rua'])

print()

for chave in pessoa:
    print(chave,':', pessoa[chave])