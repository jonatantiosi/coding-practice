def mult (*args):
    resultado = 1    
    for num in args:
        if num == 0:
            return 0
        else:
            resultado = resultado * num
    return resultado


def par_impar(num):
    if (num % 2 == 0):
        return 'Par'
    else:
        # else desnecessario, redundante
        return 'Ímpar'
    
resultado = mult(5, 5)
print(resultado)

classificacao_num = par_impar(resultado)
print(classificacao_num)
