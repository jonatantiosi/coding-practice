'''
138 — Reutilizar ação de menu existente
 Tarefa: utilize uma ação já criada anteriormente e conecte-a a uma função
 diferente, sem criar uma nova ação.
 Conceitos: QAction.triggered.connect (reutilização).
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot


@Slot()
def slot_example_1(status):
    print('Action is checked?', status)


@Slot()
def slot_example_2(action: QAction):
    def inner():
        print('Action is checked?', action.isChecked())
    return inner


application = QApplication(sys.argv)
main_window = QMainWindow()
menu_bar = main_window.menuBar()
menu_1 = menu_bar.addMenu('Menu 1')

action_1 = menu_1.addAction('Action 2')
action_1.setCheckable(True)

action_1.toggled.connect(slot_example_1)
action_1.hovered.connect(slot_example_2(action_1))

main_window.show()
application.exec()
