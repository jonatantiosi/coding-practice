'''
metodos dict
'''

p1 = {
    'nome': 'Jonatan Paulo',
    'sobrenome': 'Tiosi Santana',
    'idade' : 23,
}

# apaga um item com a chave especificada igual del
# mas tambem serve para coletar o valor antes de deletar

log_idade = p1.pop('idade')

print(p1.get('idade'))
# retorna chave se existe, else None
print('chave removida:', log_idade)

ultima_chave = p1.popitem()
print(p1)
print('chave removida:', ultima_chave)

p1.update({
    'nome': 'paulo',
    'altura': 1.8,
})

p1.update(peso = 60)

tupla = ('cor', 'laranja'), # precisa da virgula
p1.update(tupla)

print(p1)