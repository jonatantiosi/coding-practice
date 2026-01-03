'''
124 — Criar aplicação Qt mínima
 Tarefa: crie uma aplicação que abra uma janela vazia e mantenha o loop ativo.
 Conceitos: QApplication(sys.argv), QWidget, show(), exec().
'''
import sys
from PySide6.QtWidgets import QApplication, QWidget

application = QApplication(sys.argv)
widget = QWidget()
widget.show()
application.exec()
