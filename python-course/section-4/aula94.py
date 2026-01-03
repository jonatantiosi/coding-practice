try:
    print('abrir arquivo')
    8/0
except ZeroDivisionError as e:
    print(e)
else:
    print('nao deu erro')
finally:
    # sempre é executado
    print('fechar arquivo')