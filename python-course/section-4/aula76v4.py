'''
metodos dict
'''

import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}

d2 = d1.copy() #shallow copy, sem o import
# copia rasa, copia tudo *imutavel* 
# mutaveis vao apontar para o mesmo local na memoria

# com import
d2 = copy.copy(d1) # shalow
d2 = copy. deepcopy(d1) # deep

d2['c1'] = 1000
d2['l1'][1] = 9999


print(d1)
print(d2)