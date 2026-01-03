# # from sys import path

# from aula99_package.modulo import soma_do_modulo
# # 1
# import aula99_package.modulo
# # 2
# from aula99_package import modulo
# # 3
# # tbm tem como importar all com "*" mas e ma pratica de prog
# # __all__ = [] no modulo em si limita o import

# # print(*path, sep='\n')
# # # lista desenpacotada dos paths

# print(aula99_package.modulo.soma_do_modulo(4, 5))
# # 1
# print(soma_do_modulo(4, 5))
# # 2
# print(modulo.soma_do_modulo(4, 5))
# # 3

# from aula99_package.modulo import soma_do_modulo

from aula99_package import soma_do_modulo

print(soma_do_modulo(2, 3))


