from time import sleep
from threading import Thread

'''
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


# se for apenas um arg: args=(arg1,)
thread_1 = Thread(target=vai_demorar, args=('Lorem', 2))
thread_1.start()

thread_2 = Thread(target=vai_demorar, args=('Ipsum', 3))
thread_2.start()

thread_3 = Thread(target=vai_demorar, args=('Dolor', 5))
thread_3.start()

for i in range(15):
    print(i)
    sleep(.5)
'''


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


# se for apenas um arg: args=(arg1,)
thread_1 = Thread(target=vai_demorar, args=('Lorem', 10))
thread_1.start()
# thread_1.join()

while thread_1.is_alive():
    print('Esperando a thread...')
    sleep(2)
print('Thread acabou.')
