'''
117 — Pilha LIFO com lista
Tarefa: use uma lista como pilha, adicionando elementos com append e removendo
com pop. Imprima o último elemento removido.
Conceitos: list.append, list.pop.
'''
list_: list[str] = list()

list_.append('a')
list_.append('b')
list_.append('c')
list_.pop()
list_.pop()
last_element = list_.pop()
print('Last removed from list:', last_element)
