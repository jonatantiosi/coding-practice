'''
Escreva um programa que percorra os elementos e:

    Se for um número, imprima o dobro do valor.

    Se for um set, adicione o número 99 ao conjunto e imprima.

    Se for uma str, imprima todas as letras em maiúsculas.

    Caso contrário, apenas imprima o valor original.
'''

itens = [True, 42, 'Python', 3.14, 
         {1, 2, 3}, (4, 5), {'chave': 'valor'}
]

for item in itens:
    
    if isinstance(item, bool):
        print(item)

    elif isinstance(item, (float, int)):
        print(item * 2)
    
    elif isinstance(item, set):
        item.add(99)
        print(item)

    elif isinstance(item, str):
        item_upper = item.upper()
        print(item_upper)
    
    else:
        print(f'{type(item).__name__}: {item}')
        # sugestao do chat 
