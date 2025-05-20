#8.1
def task1():
    cnts = {"Россия": "Москва", "Канада": "Оттава", "США": "Вашингтон", "Китай": "Пекин", "Бразилия": "Бразилиа"}
    for key in cnts:
        print(key, "-", cnts[key])

    a = input ("Введите название страны, столицу которой хотите узнать - ")
    if a.title () in cnts:
        print (f"Столица введенной страны - {cnts[a.title ()]}")
    else:
        print ("К сожалению, в представленном списке такой страны нет")


    sort = sorted (cnts)
    print (f"Словарь по алфавиту - {sort}")

#8.2
def task2 ():
    bukv = {1:"АВЕИНОРСТ", 2:"ДКЛМПУ", 3:"БГЁЬЯ", 4:"ЙЫ", 5: "ЖЗЧЦХ", 8:"ШЭЮ", 10: "ФЩЪ"}
    a = input ("Введите слово - ").upper ()
    sum = 0
    for i in a:
        for key, value in bukv.items ():
            if i in value:
                sum += key
                break
    print (f"Ваше слово - {a} \nСтоимость вашего слова = {sum}")



a = int (input("Введите номер задачи - "))
if a == 1:
    task1()
elif a == 2:
    task2()
else:
    print ("Такой задачи в 8й лабораторной нет")
