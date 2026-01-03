# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python
from PIL import Image
from pathlib import Path


ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(ORIGINAL)

# print(pil_image.size)
width, height = pil_image.size
# metadados/informacoes da imagem
# try:
#     exif = pil_image.info['exif']
# except KeyError:
#     print('Imagem sem exif')
exif = pil_image.info.get('exif')
if exif is None:
    print('Imagem sem exif')


# width     new_width
# height    ??
new_width = 640
# regra de 3
new_height = round(height * new_width / width)
print(width, height)
print(new_width, new_height)

new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,
)
