def gen1():
    print('comeco gen1')
    yield 1
    yield 2
    yield 3
    print('fim gen1')

def gen2(gen):
    print('comeco gen2')
    if gen is not None: 
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('fim gen2')

def gen3():
    print('comeco gen3')
    yield 10
    yield 20
    yield 30
    print('fim gen3')

g1 = gen2(gen1)
g2 = gen2(gen3)

for numero in g1:
    print(numero)

for numero in g2:
    print(numero)   