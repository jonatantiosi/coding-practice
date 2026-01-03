'''
111 — Thread básica com função alvo
Tarefa: crie uma função que receba um texto e um tempo, durma pelo tempo
informado e depois imprima o texto. Execute essa função em uma Thread.
Conceitos: threading.Thread, target, args, start.
'''
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

    def print_text(self):
        sleep(self.time)
        print(self.text)


thread_1 = MyThread('Lorem', 1)
thread_1.print_text()
