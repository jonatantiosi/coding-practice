# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime  # , timedelta
from dateutil.relativedelta import relativedelta

format = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', format)
data_fim = datetime.strptime('30/12/2022 08:20:20', format)

# print(data_fim > data_inicio)

# print(data_fim - data_inicio)
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.total_seconds())

# delta = timedelta(days=11, hours=1)
delta = relativedelta(data_fim, data_inicio)
print(delta)

print(data_fim)
# print(data_fim + delta)
print(data_fim + relativedelta(seconds=59, minutes=10))
