def soma(num1, num2):
    # soma
    return num1 + num2

def sub(num1, num2):
    # subtracao
    return num1 - num2

def mult(num1, num2):
    # multiplicacao
    return num1 * num2

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as error:
        return error.__class__.__name__