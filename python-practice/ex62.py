'''
Tarefa: transforme '2022-12-12 07:59:23' em datetime, formate como '12/12/2022'
extraia a hora e mostre diferença entre tipos str e int.
Conceitos: strftime, strptime, tipos de dados, formatação.
'''
from datetime import datetime

string_ = '2022-12-12 07:59:23'
format_ = '%Y-%m-%d %H:%M:%S'

data = datetime.strptime(string_, format_)
data_formatada = data.strftime('%d/%m/%Y')
hora_extraida_int = data.hour
hora_extraida_str = data.strftime('%H')


print(data_formatada)
print(hora_extraida_int, type(hora_extraida_int))
print(hora_extraida_str, type(hora_extraida_str))
