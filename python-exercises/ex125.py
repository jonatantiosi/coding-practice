'''
125 — Exibir botão simples
 Tarefa: crie uma aplicação com um único botão, defina um texto e exiba-o na
 tela.
 Conceitos: QPushButton.
'''
import sys
from PySide6.QtWidgets import QApplication, QPushButton

application = QApplication(sys.argv)

button_1 = QPushButton('button 1')
button_1.show()

application.exec()
