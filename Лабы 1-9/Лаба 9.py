from PIL import Image, ImageFilter
import os

#9.1
def task1():
    image = Image.open('Кот.jpg')
    image.show()

    print(f"Имя файла:{image.mode}")
    print(f"Формат: {image.format}")
    print(f"Ширина x высота: {image.size}")

#9.2
def task2():
    image = Image.open('Кот.jpg')
    image.show()
    little = image.resize((image.width // 3, image.height // 3))
    hor = image.transpose (Image.FLIP_LEFT_RIGHT)
    ver = image.transpose (Image.FLIP_TOP_BOTTOM)
    little.save ("Маленький кот.jpg")
    hor.save("Отраженный кот.jpg")
    ver.save("Перевернутый кот.jpg")


#9.3
def task3():
        new = 'Картинки с фильтром'
        os.makedirs (new)
        for i in range (1,6):
            first = "Картинки без фильтра/" + str (i) + ".jpg"
            image = Image.open (first)
            image = image.filter (ImageFilter.EMBOSS)
            new1= "Картинки с фильтром/" + str (i) + ".jpg"
            image.save(new1)

#9.4
def task4():
    image = Image.open ('Кот.jpg')
    watermark = Image.open ('Watermark.png')
    image.paste (watermark,(9,1),watermark)
    image.save ('Кот с водным знаком.png')


a = int (input("Введите номер задачи - "))
if a == 1:
    task1()
elif a == 2:
    task2()
elif a == 3:
    task3()
elif a == 4:
    task4()
else:
    print ("Такой задачи в 9й лабораторной нет")