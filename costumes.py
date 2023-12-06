import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "modes.gif", save_all=True, append_image=[images[1]], duration=1000,loop=0
)
