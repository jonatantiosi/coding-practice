# problema dos parâmetros mutáveis em funções Python

# def adiciona_clientes(nome, lista=[]):
#     # NAO usar parametros mutaveis em parametros padroes da funcao
#     lista.append(nome)
#     return lista

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
        # cria dentro da funcao, se nao for informado
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('joana', cliente1)

cliente2 = adiciona_clientes('helena')
adiciona_clientes('maria', cliente2)


print(cliente1)
print(cliente2)