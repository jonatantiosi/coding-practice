'''
116 — Fila FIFO com deque
Tarefa: implemente uma fila, adicione elementos no final e remova
do início, imprimindo o estado da fila após cada operação.
Conceitos: collections.deque, append, popleft.
'''
from collections import deque

fila: deque[str] = deque(['a', 'b', 'c'])
print(fila)
fila.append('d')
fila.append('e')
fila.append('f')
print(fila)
fila.popleft()
fila.popleft()
fila.popleft()
print(fila)
