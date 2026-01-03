# interpolacao basica de strings
# x e X hexadecimal (ABCDEF0123456789)

nome = 'jonatan'
preco = 1000.95897643
variavel = '%s, o preco e R$%.2f, %s' % (nome, preco, nome)
print(variavel)
print('o hexadecimal de %d e %04x' % (15, 15))
print('o hexadecimal de %d e %08X' % (15, 15))