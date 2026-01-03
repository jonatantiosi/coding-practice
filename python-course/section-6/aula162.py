# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
from pytz import timezone


# data_str = '2025-10-10 18:28:15'
# data_format_str = '%Y-%m-%d %H:%M:%S'
data_br = datetime(
    2025, 10, 10, 18, 28, 15, tzinfo=timezone('America/Sao_Paulo')
)

# data = datetime.strptime(data_str, data_format_str)

data_jp = datetime.now(timezone('Asia/Tokyo'))

print(data_br)
print(data_jp)

print()

print(data_br.timestamp())  # e.g base de dados
print(datetime.fromtimestamp(1760132055))
