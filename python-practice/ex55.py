'''
Tarefa: escreva chain_generators(*gens) que usa yield from para encadear
geradores. Teste com 2 geradores simples.
Conceitos: yield from, composição.
'''


def gen1():
    yield '1'


def gen2():
    yield '2'


def gen3():
    yield '3'


def chain_generators(*gens):
    '''usa yield from para encadear geradores e retorna yield de cada'''
    for gen in gens:
        yield from gen()


generators = chain_generators(gen1, gen2, gen3)

for yield_ in generators:
    print(yield_)
