# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html


from datetime import datetime

format = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-12 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data)
print(data.strftime(format))

print(data.strftime('%m/%Y %H:%m'))
print()

print(data.strftime('%H'))
print(type(data.strftime('%H')))  # string
print(data.hour)
print(type(data.hour))  # int
