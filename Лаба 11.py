from PIL import Image, ImageFilter
import os

#11.1
new = "Обработанные фото - 11.1"
os.makedirs (new)
for n in range (1, 6):
    name = "Исходники/" + str (n) + ".jpg"
    img = Image.open (name)
    new1 = img.filter (ImageFilter.EMBOSS)
    name1 = ("Обработанные фото - 11.1/" + str (n) + ".jpg")
    new1.save (name1)

#11.2
new = "Обработанные фото - 11.2"
os.makedirs (new)

for name in os.listdir ("Исходники"):
    if name.lower().endswith(('.jpg', '.png')):
          newname = "Исходники/" + name
          img = Image.open (newname)
          newimg = img.filter (ImageFilter.UnsharpMask)
          newname1 = ("Обработанные фото - 11.2/" + str (name))
          newimg.save (newname1)
    else:
      print ("Ошибка! В папке должны лежать только jpg и png")
