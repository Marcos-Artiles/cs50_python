#PILLOW LIBRARY FOR IMAGE MANIPULATION
from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        #ROTATING THE IMAGE
        img.rotate(180)

        #BLURING THE IMAGE
        img.filter(ImageFilter.BLUR)

        #FINDING THE EDGES OF THE IMAGE
        img.filter(ImageFilter.FIND_EDGES)

        #SAVING THE IMAGE
        img.save("out.jpeg")

main()