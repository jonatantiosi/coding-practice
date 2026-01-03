'''
128 — Widget central obrigatório
 Tarefa: defina um widget central para a janela principal e exiba a interface.
 Conceitos: QMainWindow.setCentralWidget.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()
main_window.setCentralWidget(central_widget)

main_window.show()
application.exec()
