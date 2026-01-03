try:
    a =  18
    b = 0
    # print(b[0])
    # print('linha 1'[1000])
    c = a/b
    print('linha 2')
    # se nao tratar direito vira erro silenciado

except ZeroDivisionError as e:
    print(e.__class__.__name__)

except NameError:
    print('name error')

except (TypeError, IndexError) as error:
    # melhor fazer dividido
    print('type/index error')
    print('msg:', error)
    print('name:', error.__class__.__name__)

except Exception:
    # mais abrangente classe de erros no python, trata qualquer erro
    print('erro desconhecido')


print('continuacao')