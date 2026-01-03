'''
136 — Comparação entre dois tipos de ação
 Tarefa: crie duas ações de menu:
    uma que apenas executa uma função
    outra que alterna estado e envia um valor booleano
 Conceitos: assinatura de slots, triggered vs toggled.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


def slot_example_1():
    print('Hardcoded message')


def slot_example_2(status: bool):
    print('Status:', status)


application = QApplication(sys.argv)
main_window = QMainWindow()
menu_bar = main_window.menuBar()
menu_1 = menu_bar.addMenu('Menu 1')
action_1 = menu_1.addAction('Action 1')
action_2 = menu_1.addAction('Action 2')
action_2.setCheckable(True)

action_1.triggered.connect(slot_example_1)
action_2.toggled.connect(slot_example_2)

main_window.show()
application.exec()
