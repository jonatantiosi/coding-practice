from itertools import combinations

pessoas = ['João', 'Maria', 'Carlos', 'Ana']

grupos_pessoas = combinations(pessoas, 2)

print('pessoas:')
print(*pessoas, sep=', ')
print('pares possíveis:')
for par in grupos_pessoas:
    print(f'{par[0]} e {par[1]}')