'''
Pathlib + criação de estrutura de pastas
Tarefa: use pathlib.Path para criar a estrutura

/PastaTeste/Subpasta1/Subpasta2

Crie também um arquivo info.txt dentro da última subpasta e escreva o texto
"Teste concluído".
Conceitos: Path.mkdir, Path.touch, Path.write_text.
'''
from pathlib import Path

# criacao dos caminhos dos diretorios
CAMINHO_PASTA = Path.home() / 'Desktop' / 'PastaTeste'
CAMINHO_SUBPASTA_1 = CAMINHO_PASTA / 'Subpasta1'
CAMINHO_SUBPASTA_2 = CAMINHO_SUBPASTA_1 / 'Subpasta2'

# criacao dos diretorios
Path.mkdir(CAMINHO_PASTA, exist_ok=True)
Path.mkdir(CAMINHO_SUBPASTA_1, exist_ok=True)
Path.mkdir(CAMINHO_SUBPASTA_2, exist_ok=True)

# criacao do caminho do arquivo mais criacao do arquivo arquivo
CAMINHO_ARQUIVO = CAMINHO_SUBPASTA_2 / 'info.txt'
Path.touch(CAMINHO_ARQUIVO, exist_ok=True)

# escrita no arquivo
Path.write_text(CAMINHO_ARQUIVO, 'Teste concluído')
