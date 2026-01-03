'''
113 — Aguardar término de thread
Tarefa: execute uma thread longa e, enquanto ela estiver ativa, imprima
periodicamente uma mensagem no loop principal. Ao finalizar, exiba “Thread
acabou”.
Conceitos: Thread.is_alive, sleep, loop de espera.
'''
from time import sleep
from threading import Thread


def thread_function(text, time):
    sleep(time)
    print(text)


thread_1 = Thread(target=thread_function, args=('Random text', 5))
thread_1.start()

while thread_1.is_alive():
    sleep(1)
    print('Waiting for thread_1 to finish...')
print('thread_1 ended.')
