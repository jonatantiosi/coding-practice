"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""


frase = "     Lorem ipsum dolor sit amet   , consectetuer adipiscing elit.    "

lista_separada = frase.split(',') 
# retorna lista

lista_separada_corrigida = []
 
for i, frase in enumerate(lista_separada):
    print(lista_separada[i].strip())
    # strip corta os espacos em branco do comeco e do final
    # rstrip e lstrip cortam somente right/left
    lista_separada_corrigida.append(lista_separada[i].strip())




# print(lista_separada_corrigida)

jonatan = '-'.join('jonatan')
frases_unidas = ' '.join(lista_separada_corrigida)


print(jonatan)
print(frases_unidas)



