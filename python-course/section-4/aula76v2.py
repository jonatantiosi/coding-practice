pessoa = {}


chave = 'nome completo'

pessoa[chave] = 'jonatan paulo'
# pessoa['nome'] = 'jonatan paulo'
# criando chave


pessoa['sobrenome'] = 'tiosi santana'
del pessoa['sobrenome']

print(chave,':', pessoa[chave])

if pessoa.get('sobrenome') is None:
    # o metodo tenta obter a chave deletada 'sobrenome'
    # retorna none se a chave nao existir
    print('n existe')
else:
    print(pessoa['sobrenome'])