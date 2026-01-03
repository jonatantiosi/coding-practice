a = 'A'
b = 'B'
c = 1.1
formato = 'a={0} b={1} c={nome3:.2f} a={0}'.format(
    a, b, nome3=c # parametro nomeado
    )

formato_2 = 'a={} b={} c={:.2f}'.format(a, b, c)

print(formato)
print(formato_2)
print('a'+1)