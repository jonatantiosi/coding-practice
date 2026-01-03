'''
metodos dict
'''

pessoa = {
    'nome': 'Jonatan Paulo',
    'sobrenome': 'Tiosi Santana',
    # 'idade' : 23,
}

# print(pessoa.__len__())
# # metodo, pouco usado

print(len(pessoa))
# funcao, mais usado, retorna quantas chaves

print(tuple(pessoa.keys()))
# retorna as chaves

print(tuple(pessoa.values()))
# retorna os valores

print(list(pessoa.items()))
# volta as chaves e os valores
for chave, valor in pessoa.items():
    print(chave, valor)

pessoa.setdefault('idade', None)
print(pessoa['idade'])



