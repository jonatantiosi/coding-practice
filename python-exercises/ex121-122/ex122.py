'''
122 — Tratar ausência de EXIF em imagem
Tarefa: ao abrir uma imagem, tente obter os dados EXIF e avise o usuário caso
não existam, sem gerar erro.
Conceitos: Image.info.get, dicionários, None.
'''
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'original_picture.jpg'

pillow_image = Image.open(IMAGE_PATH)
try:
    image_exif = pillow_image.info.get('exif')
    if image_exif is not None:
        print(image_exif)
    print('Imagem não contém exif')
except Exception as e:
    print('Erro ao tentar obter os dados exif:', e)
