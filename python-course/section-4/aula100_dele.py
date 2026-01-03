import copy

from dados import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.1, 2)}
    # desempacota e modifica
    for p in copy.deepcopy(produtos)

]
# print(*produtos, sep='\n') 
# print()
# print(*novos_produtos, sep='\n') 

produtos_ordenados_por_nome = sorted (
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)


produtos_ordenados_por_preco = sorted (
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print(*produtos, sep='\n') 
print()
print(*novos_produtos, sep='\n') 
print()
print(*produtos_ordenados_por_nome, sep='\n') 
print()
print(*produtos_ordenados_por_preco, sep='\n') 