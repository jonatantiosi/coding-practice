import sys
# importa path para usar funcao da pasta funcoes uteis
sys.path.append(r'C:\\Users\\Jonatan\\Desktop\\python\\udemy_python')
from funcoes_uteis.main import print_iter
# importa funcao para dar print em iteraveis, desempacotando-os
import os
import json

def add_task(item, lista_tarefas):
    # recebe um input do usuario e adiciona na lista de tarefas
    lista_tarefas.append(item)
    os.system('cls')
    print('Item adicionado à lista\n')

def list_tasks(lista_tarefas):
    # printa lista se nao vazia
    if len(lista_tarefas) != 0:
        os.system('cls')
        print('Lista de tarefas:\n')
        print_iter(lista_tarefas)
    else:
        os.system('cls')
        print('Nada a listar\n')

def list_undo(lista_tarefas, tarefas_excluidas):
    # exclui ultimo item da lista de tarefas
    try:
        tarefa_excluida = lista_tarefas.pop()
        tarefas_excluidas.append(tarefa_excluida)
        os.system('cls')
        print('Tarefa excluída\n')
    except IndexError:
        # pop from empty list
        os.system('cls')
        print('Nada a desfazer\n')

def readd_task(lista_tarefas, lista_tarefas_excluidas):
     # restaura ultimo item da lista de excluidos
    try: 
        tarefa_restaurada = lista_tarefas_excluidas.pop()
        lista_tarefas.append(tarefa_restaurada)
        os.system('cls')
        print('Tarefa restaurada\n')
    except IndexError:
        # pop from empty list
        os.system('cls')
        print('Nada a refazer\n')

# def listastr_para_texto(lista):
#     return '\n'.join(lista)

CAMINHO = r'aulas111-120\\lista_tarefas.json'
# letra maiscula indica que nao é pra ser alterado (constante)

# definicao listas com comandos, tarefas a serem adicionadas e historico de tarefas excluidas

arquivo_inexistente_ou_vazio = (not os.path.exists(CAMINHO)) or (os.path.getsize(CAMINHO) == 0)

if arquivo_inexistente_ou_vazio:
    # se nao existir arquivo ou for vazio, cria um com lista vazia
    with open(CAMINHO, 'w', encoding='utf-8') as arquivo:
        json.dump([], arquivo)  

with open(CAMINHO, 'r', encoding='utf-8') as arquivo:
    lista_tarefas = json.load(arquivo)

lista_comandos = ['listar', 'desfazer', 'refazer', 'sair']
# lista_tarefas = []
lista_tarefas_excluidas = []

while True:

    input_comando = input('Comandos: listar, desfazer, refazer, sair\n'
                        'Digite uma tarefa ou comando:\n')
    

    if input_comando.lower() not in lista_comandos:
        add_task(input_comando, lista_tarefas)
       
    elif input_comando.lower() == 'listar':
        list_tasks(lista_tarefas)

    elif input_comando.lower() == 'desfazer':
        list_undo(lista_tarefas, lista_tarefas_excluidas)

    elif input_comando.lower() == 'refazer':
        readd_task(lista_tarefas, lista_tarefas_excluidas)

    else:
        # pela logica é acessado somente quando o usuário digita sair
        break


with open(CAMINHO, 'w+', encoding='utf-8') as arquivo:
    json.dump(
        lista_tarefas,
        arquivo
        )

