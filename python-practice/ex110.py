'''
110 — Usando subprocessos com diferentes sistemas operacionais
Tarefa: crie um script que, utilizando subprocess.run(), execute o comando ping
e trate a codificação do retorno de acordo com o sistema operacional
(Windows usa cp850, Linux usa utf_8).
Conceitos: subprocess, plataforma, codificação, execução de comandos
condicionais.
'''
import subprocess
import sys

if sys.platform == "win32":
    comando = ['ping', '127.0.0.1']
    encoding_ = 'cp850'
else:
    comando = ['ping', '127.0.0.1', 'c', '4']
    encoding_ = 'utf_8'

process = subprocess.run(
    comando,
    capture_output=True,
    text=True,
    encoding=encoding_
    )

print(process.stdout)
