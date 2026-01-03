import importlib


import aula98_m # singleton, apenas uma instancia

for i in range(10):
    importlib.reload(aula98_m)
    # nao e muito comum
    print(i)
    # import aula98_m
