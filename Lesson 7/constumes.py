import sys

#library for processing images
from PIL import Image

images = []

#opening and appending the images
for arg in sys.argv:
  image = Image.open(arg)
  images.append(image)

#saving the images and creating and running the .gif file
images[0].save(
  "constumes.gif", save_all = True, append_images = [images[1]], duration = 200, loop = 0
)