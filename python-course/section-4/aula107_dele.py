def zipper(lista1, lista2):
    intervalo_max = min(len(lista1), len(lista2))
    return [
        (lista1[i], lista2[i]) for i in range(intervalo_max)
    ]




 
l1 = ['BA', 'SP', 'MG', 'RJ']
l2 = ['Salvador', 'Ubatuba', 'Belo Horizonte']  

print(zipper(l1, l2))