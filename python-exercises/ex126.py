'''
126 — Dois botões em janelas separadas
 Tarefa: crie dois botões distintos, cada um sendo exibido em sua própria
 janela.
 Conceitos: múltiplos widgets.
'''
import sys
from PySide6.QtWidgets import QApplication, QPushButton

application = QApplication(sys.argv)
button_1 = QPushButton('1')
button_2 = QPushButton('2')

button_1.show()
button_2.show()

application.exec()
