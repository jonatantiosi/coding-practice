def multiply(*args):
    total = 1
    for number in args:
        total *= number
    return total


def even_odd(num):
    mult_de_2 = num % 2 == 0

    if mult_de_2:
        return f'{num} é par'
    return f'{num} é ímpar'



print(even_odd(2))
print(even_odd(3))


multiplication = multiply(1,2,3,4,5)
print(multiplication)
