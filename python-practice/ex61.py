'''
61 — Diferenças e operações com datas
Tarefa: calcule o tempo entre "20/04/1987 09:30:30" e "30/12/2022 08:20:20"
usando relativedelta. Depois, some 1 mês e 10 dias à data atual e mostre
formatada.
Conceitos: dateutil.relativedelta, aritmética de datas, formatação.
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta

# data_inicio = datetime.strptime('20/04/1987 09:30:30', format)

data1_string = '20/04/1987 09:30:30'
data2_string = '30/12/2022 08:20:20'
format_ = '%d/%m/%Y %H:%M:%S'
novo_format_ = '%d/%m/%Y'

data1 = datetime.strptime(data1_string, format_)
data2 = datetime.strptime(data2_string, format_)

diferenca = relativedelta(data2, data1)

print(diferenca)

data_atual = datetime.now()
data_nova = data_atual + relativedelta(months=1, days=10)

print()
print(data_nova.strftime(novo_format_))
