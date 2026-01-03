'''
Tarefa: função first_duplicate(nums) que retorna o primeiro número cujo segunda
ocorrência aparece primeiro (mesmo enunciado que tem no merged). Escreva testes
para 4 listas (incluindo sem duplicados).
Conceitos: sets, ordem, testes simples.
'''
lista_1 = [5, 3, 4, 6, 7, 3, 4, 7, 9, 0]  # primeiro duplicado 3
lista_2 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]  # primeiro duplicado 0
lista_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # sem duplicado
lista_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]  # primeiro duplicado 1


def first_duplicate(nums):
    duplicados = set()
    for num in nums:
        if num in duplicados:
            return num
        duplicados.add(num)

    return -1


print(first_duplicate(lista_1))
print(first_duplicate(lista_2))
print(first_duplicate(lista_3))
print(first_duplicate(lista_4))
