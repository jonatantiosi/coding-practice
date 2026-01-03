'''
Tarefa: crie um script que utilize subprocess.run() para executar o comando
ping 127.0.0.1 (no seu sistema operacional) e imprima a saída do comando.
Conceitos: subprocess, execução de comandos, captura de saída
'''
import subprocess

comando = ['ping', '127.0.0.1']
process = subprocess.run(
    comando,
    capture_output=True,
    text=True,
    encoding='cp850'
    )

print(process.stdout)
