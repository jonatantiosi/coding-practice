'''
64 — Calendário e último dia do mês
Tarefa: usando o módulo calendar, mostre o último dia de fevereiro de 2024 e
diga em que dia da semana ele cai (0 = segunda, 6 = domingo).
Conceitos: calendar.monthrange, calendar.weekday, datas e calendários.
'''
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

primeiro_dia, ultimo_dia = calendar.monthrange(2024, 2)
# pega número no dia da semana do último dia (0 = segunda, 6 = domingo)
indice_ultimo_dia = calendar.weekday(2024, 2, ultimo_dia)

print(f'{ultimo_dia} é o último dia de feveiro de 2024,',
      f'ele cai em um(a) {calendar.day_name[indice_ultimo_dia]}')
