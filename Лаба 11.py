from PIL import Image, ImageFilter
import os
import csv

#11.1
'''new = "Обработанные фото - 11.1"
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
          newimg = img.filter (ImageFilter.FIND_EDGES)
          newname1 = ("Обработанные фото - 11.2/" + str (name))
          newimg.save (newname1)
    else:
      print ("Ошибка! В папке должны лежать только jpg и png") '''


#11.3
sum = 0
popupochki = []
file = open ('products.csv', encoding='utf-8')
reader = csv.DictReader(file)
for row in reader:
    product = row["Продукт"]
    kolvo = int (row ["Количество"])
    price = int (row ["Цена"])
    cost = kolvo * price
    sum += cost
    popupochki.append (f"{product} - {kolvo} шт. \nОбщая стоимость = {price}")
file.close ()
print ("Не забудь купить: ")
for i in popupochki:
    print (i)
print (f"Итоговая сумма = {sum}")

