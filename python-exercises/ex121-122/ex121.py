'''
121 — Redimensionar imagem mantendo proporção
Tarefa: abra uma imagem, calcule a nova altura proporcional a uma nova largura
fixa e salve a imagem redimensionada.
Conceitos: PIL.Image.open, Image.size, Image.resize, save.
'''
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
IMAGE_PATH = ROOT_FOLDER / 'original_picture.jpg'
NEW_IMAGE_PATH = ROOT_FOLDER / 'new_picture.jpg'

pillow_image = Image.open(IMAGE_PATH)
original_width, original_height = pillow_image.size

new_width = round(original_width * 0.5)
new_height = round(original_height * 0.5)
new_measure = (new_width, new_height)

new_image = pillow_image.resize(new_measure)  # !!
new_image.save(NEW_IMAGE_PATH)  # !!
