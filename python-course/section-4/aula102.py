# variaveis livres + nonlocal (locals, globals)

# y = 1
# print(globals())

# def fora(x):
#     a = x 
#     def dentro():
#         print(locals())
#         return a # variavel livre, nao esta definida dentro do escopo da funcao 'dentro'
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    # funcao lembra o valor de uma variavel
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        # gera erro sem nonlocal, nao pode alterar a variavel nesse escopo
        return valor_final 
    return interna

a = concatenar('a')

print(a('b'))
print(a('c'))
print(a('d'))
