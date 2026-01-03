'''
137 — Definir título da janela
 Tarefa: configure a janela principal para exibir um título personalizado na
 barra superior.
 Conceitos: QMainWindow.setWindowTitle.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

application = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setWindowTitle('Title')

main_window.show()
application.exec()
