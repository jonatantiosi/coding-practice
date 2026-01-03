'''
Exclusão recursiva com Path
Tarefa: crie uma função remover_pasta(root: Path) que apague todos os arquivos
e subpastas dentro de um diretório, e por fim o próprio diretório.
Conceitos: recursão, Path.glob, Path.is_dir, Path.unlink, Path.rmdir.
'''
from pathlib import Path

caminho_root = Path.home() / 'Desktop' / 'PastaTeste'


def remover_pasta(root: Path):
    ...
