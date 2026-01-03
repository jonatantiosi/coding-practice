# mais inteligente

def create_multiplier(multiplier):
    def multiply(number):
        return (number * multiplier)
    return multiply

multiply_double = create_multiplier(2)
multiply_triple = create_multiplier(3)
multiply_quadruple = create_multiplier(4)



print(multiply_double(4))
print(multiply_triple(6))

