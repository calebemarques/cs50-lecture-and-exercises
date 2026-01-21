import sys
from PIL import Image

image = []

for arg in sys.argv:
    image = Image.open(arg)
    image.append(image)

image[0].save(
    "costume.gif",save_all=True, append_images=image[1:], loop=0
)