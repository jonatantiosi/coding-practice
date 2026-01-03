s1 = set()

s1.add('lorem') # aceita apenas um valor
s1.add(1)
s1.update('ipsum') # adiciona iterado
s1.update(('jonatan', 99)) # resolve apenas um valor com tupla
# s1.clear()
s1.discard(99)

print(s1)


# Operadores úteis:
 
# união | união (union) - Une
 
# intersecção & (intersection) - Itens presentes em ambos
 
# diferença - Itens presentes apenas no set da esquerda
 
# diferença simétrica ^ - Itens que não estão em ambos

s2 = {1, 2, 3}
s3 = {2, 3, 4}
uniao = s2 | s3
intereccao = s2 & s3
diferenca = s2 - s3
diferenca2 = s3 - s2
dif_sim = s2 ^ s3 # apenas em um e apenas no outro


print(uniao)
print(intereccao)
print(diferenca)
print(diferenca2)
print(dif_sim)