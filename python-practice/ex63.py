'''
63 — Parcelas de empréstimo
Tarefa: simule empréstimo de R$ 100 000 com início em 20/12/2020 e duração de 3
anos. Gere todas as datas mensais e o valor de cada parcela, usando
relativedelta e strftime.
Conceitos: loops, datetime, relativedelta, cálculo e formatação.
'''
from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_emprestimo = 100_000
data_inicio = datetime(2020, 12, 20)
data_fim = data_inicio + relativedelta(years=3)
diferenca = relativedelta(data_fim, data_inicio)
numero_parcelas = diferenca.years*12 + diferenca.months
data_atual = data_inicio
i = 1
valor_parcela = valor_emprestimo / numero_parcelas

while data_atual < data_fim:
    print(
        f'Parcela {i}: {valor_parcela:.2f}R$ '
        f'({data_atual.strftime("%d/%m/%Y")})')
    i += 1
    data_atual += relativedelta(months=1)
