'''
Crie um novo dicionário onde:

    Todos os valores do tipo str devem estar em letras minúsculas.

    Os valores numéricos devem ser multiplicados por 2.

    O campo "categoria" não deve ser incluído no novo dicionário.
'''


produto = {
    'nome': 'Lápis Preto',
    'preco': 1.5,
    'categoria': 'Material Escolar',
    'estoque': 50
}

produto_novo = {

    chave: valor.lower() 
    if isinstance(valor, str) 
    else valor *2 if isinstance(valor, (int, float))
    else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
    

}

print(produto_novo)