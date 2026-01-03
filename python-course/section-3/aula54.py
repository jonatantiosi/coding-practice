import os

lista_compras = []
existe_indice = False

while True:


    opcao_selecionada = input('Selecione uma opção\n'
                        '[i]nserir\n'
                        '[a]pagar\n'
                        '[l]istar:\n'
                        '')
    
    

    if opcao_selecionada.lower() not in 'ial':
        os.system('cls')
        print('Selecione uma opção existente (i, a ou l)')
        continue
    else:
        if opcao_selecionada.lower() == 'i':
            os.system('cls')
            dado_inserir = input('Item a inserir: ')
            lista_compras.append(dado_inserir)
        
        elif opcao_selecionada.lower() == 'a':
            os.system('cls')
            indice_apagar = input('Índice para apagar: ')

            # correcao usa Try e Except
            ##

            try:
                int_indice_apagar = int(indice_apagar)
            except ValueError:
                print('Valor inválido')
                continue

            for indice, item in enumerate(lista_compras):
                if int_indice_apagar == indice:
                    existe_indice = True
                    break 
                else:
                    existe_indice = False
            
            if existe_indice:
                lista_compras.pop(int_indice_apagar)
                # poderia usar o del lista_compras[int_indice_apagar]
            else:
                print("Não existe item com esse índice")
                continue

            ##

        elif opcao_selecionada.lower() == 'l':
            os.system('cls')

            # parte da correcao

            if len(lista_compras) == 0:
                print('Lista vazia')

            for indice, item in enumerate(lista_compras):
                print(f'{indice}. {item}')