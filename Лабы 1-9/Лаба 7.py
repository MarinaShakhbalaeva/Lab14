import random

#7.1
def task1():
    a = []
    for i in range (5):
        a.append (random.randint (1,100))
    s = int (input ("Введите число - "))
    if s in a:
        print ("Поздравляю, Вы угадали число")
    else:
        print ("Нет такого числа!")
    print ("Исходный список", a)

#7.2
def task2():
    a = []
    for i in range (10):
        a.append (random.randint (1,100))
    a1 = []
    print ("Первоначальный список", a)
    for i in a:
        if a.count(i) > 1 and i not in a1:
            a1.append (i)
    if len (a1)>0:
        print ("Повторяющиеся элементы ", a1)
    else:
        print ("Повторяющихся элементов нет")

#7.3
def task3():
    a = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    a1 = int (input ("Введите количество желаемых выходных - "))
    if 0 <= a1 <=7:
        print ("Ваши выходные дни: ", a [7-a1:7])
        print("Ваши выходные дни: ", a [:7-a1])
    else:
        print ("Хэй, ты чего? В неделе 7 дней")


#7.4
def task4 ():
    my = ["Лукьянчикова", "Оржаховская", "Сухопар", "Огородникова", "Шахбалаева", "Малахов", "Тарасова", "Сажнев", "Добров", "Ершов"]
    notmy = ["Петров", "Иванов", "Васильева", "Кукушкина", "Пупушкина", "Сапожкин", "Сырков", "Белый", "Запорожкина", "Володин"]
    t1 = tuple (random.sample (my, 5))
    t2 = tuple(random.sample(notmy, 5))
    team = t1 + t2
    print (f"Наша группа {my} \nДругая группа {notmy} \nСостав команды {team} \nДлина кортежа = {len (team)} \n")

    sort = sorted (team)
    if team.count ("Иванов") > 0:
        c = team.count ("Иванов")
        print (f"Количество Ивановых = {c}")
    else:
        print ("Ивановых в команде нет")

    print (f"Сортировка по алфавиту {sort}")




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
    print ("Такой задачи в 7й лабораторной нет")