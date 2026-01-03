# Mantendo estador dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return 
            
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return 
            
        print(f'{self.nome} parando filmagem...')
        self.filmando = False
    

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar ' \
                  'pois está filmando...')
            return
            
        print('Fotografando...')

    

camera_1 = Camera('Canon')
camera_2 = Camera('Sony')

camera_1.filmar()
camera_1.fotografar()
print()

print('Canon filmando?', camera_1.filmando)
print('Sony Filmando?', camera_2.filmando)
print()

camera_1.filmar()
camera_1.parar_filmagem()
camera_1.fotografar()

print()

camera_2.filmar()
camera_2.parar_filmagem()
camera_2.fotografar()
