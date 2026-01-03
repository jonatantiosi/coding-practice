# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2022 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


def imprime_parcelas(
        data_atual: datetime, data_ultima_parcela: datetime,
        preco_parcela
        ):
    '''
    recebe duas datetime
    while loop com incrimento nos meses imprimindo cada parcela
    '''
    indice = 0
    while data_atual <= data_ultima_parcela:
        indice += 1
        print(
            f'Parcela {indice}: {preco_parcela:.2f} '
            f"({data_atual.strftime('%d/%m/%Y')})"
        )
        data_atual = data_atual + relativedelta(months=1)


preco_emprestimo = 1000000

# settando primeira e ultima parcelas
format_ = '%d/%m/%Y'
data_primeira_parcela = datetime.strptime('20/12/2022', format_)
data_ultima_parcela = data_primeira_parcela + relativedelta(years=5)

# calculo quantidade de meses e preco da parcela individual
diferenca = relativedelta(data_ultima_parcela, data_primeira_parcela)
total_meses = diferenca.years * 12 + diferenca.months
preco_parcela = preco_emprestimo/total_meses


imprime_parcelas(data_primeira_parcela, data_ultima_parcela, preco_parcela)
