import sys

iterable = ['eu', 'tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# generator expression: basicamente, funcoes que sabem pausar

lista = [n for n in range(10000)]
generator = (n for n in range(10000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

for n in generator:
    print(n)