'''
60 — Trabalhando com datas e fusos
Tarefa: crie um objeto datetime para "2025-12-31 23:00:00" no fuso
"America/Sao_Paulo" e mostre o mesmo instante em "Asia/Tokyo".
Conceitos: datetime, pytz.timezone, conversão de fuso horário.
'''
from datetime import datetime
from pytz import timezone

data1 = datetime(2025, 10, 16, 19, 55, 40,
                 tzinfo=timezone('America/Sao_Paulo'))

print(data1)

data_2 = data1.astimezone(timezone('Asia/Tokyo'))

print(data_2)
