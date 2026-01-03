
string = input('Digite um texto: ')
metodo = input("Digite um método de string para executar: "
               "(upper, lower or replace)\n"
)  # Ex: upper, lower, replace

def replace(string):
      
      while True:
        letter_replace = input("Qual letra gostaria de modificar?\n")
        
        if letter_replace in string:
            letter_replacement = input('Qual letra gostaria de colocar no lugar?\n')
            new_string = string.replace(letter_replace, letter_replacement)
        
        else:
            print('Digite uma letra que esteja na frase')
            return None
        
        return new_string

if hasattr(string, metodo):
    if metodo == 'replace': 
        new_string = replace(string)
        if new_string is not None:
            print(new_string)
        else:
            ...
    else: 
        print(getattr(string, metodo)())
   
else:
    print('Metodo inválido')