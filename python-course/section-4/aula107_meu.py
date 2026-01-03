''' unir listas'''

def zipper(lista1, lista2):

    lista_zipper = []
    
    for i, item in enumerate(lista1):
            
        uniao_itens = (item, lista2[i])
        lista_zipper.append(uniao_itens)

    return lista_zipper


lista_estados = ['BA', 'SP', 'MG', 'RJ']
lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']

print(zipper(lista_cidades, lista_estados))