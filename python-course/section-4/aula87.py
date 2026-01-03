lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]


for item in lista:
    if isinstance(item, set):
        print('set')
        item.add(99)
        # se nao fizesse a checagem podia quebrar o programa
        # e.g. tentar chamar add em uma str
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('str')
        print(item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)):
        print('num')
        # ou um tipo ou outro
        print(item, item * 2)

    else:
        print('outro')
        print(item)