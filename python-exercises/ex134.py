'''
Tarefa: crie uma ação que possa ser marcada/desmarcada e imprima seu estado ao
alternar.
 Conceitos: QAction.setCheckable(True), QAction.toggled(bool).
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow


def slot_example_1(state: bool):
    if state:
        print('Connected')
        return
    print('Disconnected')


application = QApplication(sys.argv)
main_window = QMainWindow()
menu_bar = main_window.menuBar()
menu_1 = menu_bar.addMenu('Menu 1')
action_1 = menu_1.addAction('Action 1')
action_1.setCheckable(True)
action_1.toggled.connect(slot_example_1)

main_window.show()
application.exec()
