from PIL import Image, ImageFont, ImageDraw
import os

#10.1
def task1():
    img = Image.open ("Открытка.jpg")
    img = img.crop((50, 350, 740, 950))
    img.save("Вырезанная открытка.jpg")

#10.2
def task2():
    holiday = {"Всемирный день китов": "10.2 Открытки/Всемирный день китов.jpg", "Всемирный день лени": "10.2 Открытки/Всемирный день лени.jpg", "День пельменей": "10.2 Открытки/День пельменей.jpg","День рождения шампанского": "10.2 Открытки/День рождения шампанского.jpg","День ананасов": "10.2 Открытки/День ананасов.jpg"}
    print ("Ознакомьтесь со списком праздников:")
    for key in holiday:
        print ("-", key)
    n = input ("Выберите праздник из списка и напишите полное название - ")
    if n in holiday:
        img = Image.open (holiday [n])
        img.show ()
    else:
        print ("Такого праздника в списке нет, попробуйте снова")

#10.3
def task3():
    new = 'Открытки с надписями'
    os.makedirs(new)
    holiday = {"Всемирный день китов": "10.2 Открытки/Всемирный день китов.jpg", "Всемирный день лени": "10.2 Открытки/Всемирный день лени.jpg", "День пельменей": "10.2 Открытки/День пельменей.jpg", "День рождения шампанского": "10.2 Открытки/День рождения шампанского.jpg", "День ананасов": "10.2 Открытки/День ананасов.jpg"}
    print ("Ознакомьтесь со списком праздников: ")
    for key in holiday:
        print ("-", key)
    n = input("Выберите праздник из списка и напишите полное название - ")

    #создаем надпись
    if n in holiday:
        img = Image.open(holiday[n])
        draw = ImageDraw.Draw (img)
        text = input ("Введите имя того, кого хотите поздравить - ") + ", поздравляю!"
        if n == "Всемирный день китов":
            font = ImageFont.truetype("tf2secondary_0.ttf", 65)
            draw.text ((30, 50), text, font=font, fill=(0, 0, 255))
            img.save ("Открытки с надписями/Всемирный день китов с именем.png")
            img.show()
        elif n == "Всемирный день лени":
            font = ImageFont.truetype("tf2secondary_0.ttf", 50)
            draw.text ((15, 600), text, font=font, fill=(0, 70, 70))
            img.save ("Открытки с надписями/Всемирный день лени с именем.png")
            img.show()
        elif n == "День пельменей":
            font = ImageFont.truetype("tf2secondary_0.ttf", 65)
            draw.text ((55, 680), text, font=font, fill=(0, 60, 30))
            img.save ("Открытки с надписями/День пельменей с именем.png")
            img.show()
        elif n == "День рождения шампанского":
            font = ImageFont.truetype("tf2secondary_0.ttf", 50)
            draw.text ((55, 45), text, font=font, fill=(50, 0, 0))
            img.save ("Открытки с надписями/День рождения шампанского с именем.png")
            img.show()
        elif n == "День ананасов":
            font = ImageFont.truetype("tf2secondary_0.ttf", 50)
            draw.text ((65, 690), text, font=font, fill=(0, 150, 30))
            img.save ("Открытки с надписями/День ананасов с именем.png")
            img.show()
    else:
        print ("Такого праздника в списке нет, попробуйте снова")


a = int (input("Введите номер задачи - "))
if a == 1:
    task1()
elif a == 2:
    task2()
elif a == 3:
    task3()
else:
    print ("Такой задачи в 10й лабораторной нет")