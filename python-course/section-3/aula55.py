# imprecisao pontos flutuantes e como contornar
import decimal


numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)


print(f'{numero_3:.1f}') # retorna string
print(round(numero_3, 2)) # retorna float


numero_4 = decimal.Decimal('0.1') # converte string
numero_5 = decimal.Decimal('0.7')

print(type(numero_4 + numero_5))
print(numero_4 + numero_5)