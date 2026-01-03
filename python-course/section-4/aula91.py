# generator funcions


def generator(n=0, maximum = 10):
    while True:
        yield n

        n += 1

        if n > maximum:
            return
        
        


    # yield 1 # pausa a execucao da funcao
    # print('continuando...')
    # yield 2 # pause
    # print('one more...')
    # yield 3
    # print('terminando...')
    # return 'acabou' # levanta uma execao
               

gen = generator(n=5, maximum=8)
print(hasattr(gen, '__iter__'))

# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
