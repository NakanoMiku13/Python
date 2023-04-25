from PIL import Image
import os
DIR = "/home/miku/Pictures/Anime/"
elementList = os.listdir(DIR)
j = 0
for i in elementList:
    image = Image.open(DIR+i).convert('RGB')
    s = image.save("/home/miku/Pictures/Anime2/Image{0}.jpg".format(j))
    print(j)
    j += 1