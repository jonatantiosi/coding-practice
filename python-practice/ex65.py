'''
65 — Locale e tradução de formatos
Tarefa: defina o locale para 'pt_BR.utf8' e mostre o idioma atual configurado.
Em seguida, volte para 'en_US.utf8' e confirme a alteração.
Conceitos: locale.setlocale, locale.getlocale, internacionalização.
'''
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print(locale.getlocale())

locale.setlocale(locale.LC_ALL, 'en_US.utf8')

print(locale.getlocale())
