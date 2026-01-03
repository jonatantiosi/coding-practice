# 12:50
# 01234
#-43210

str_hora = input('horas: ') 

hora = int(str_hora[:2])
segundos = int(str_hora[-2:])

dia = 0 <= hora < 12
tarde = 12 <= hora < 18
noite = 18 <= hora < 24
segundos_corretos = 0 <= segundos <= 60

if segundos_corretos:
    if dia:
        print('bom dia')
    elif tarde:
        print('boa tarde')
    elif noite:
        print('boa noite')
    else:
        print('erro, tente digitar um horario de 00:00 a 23:59')
else:
    print('digite os segundos corretamente')