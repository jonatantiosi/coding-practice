'''
131 — Barra de status com mensagem
 Tarefa: adicione uma barra de status à janela e exiba uma mensagem inicial.
 Conceitos: QMainWindow.statusBar(), QStatusBar.showMessage.
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

application = QApplication(sys.argv)
main_window = QMainWindow()
central_widget = QWidget()

main_window.setCentralWidget(central_widget)
status_bar = main_window.statusBar()
status_bar.showMessage('Mensagem inicial')

main_window.show()
application.exec()
