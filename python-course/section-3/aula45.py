# funcionamento do for
# for letra in texto
#   print(letra)

# iteravel
texto = 'jonatan' 

# iterador
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break