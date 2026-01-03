from itertools import product


cores = ['azul', 'vermelho']
tamanhos = ['P', 'M', 'G']
materiais = ['algodão', 'poliéster']

opcoes = [
    cores, 
    tamanhos, 
    materiais
]

combinacoes_possiveis = list(product(*opcoes))

print(*combinacoes_possiveis, sep='\n')

