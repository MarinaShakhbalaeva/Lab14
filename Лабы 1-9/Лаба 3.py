#3.1
def task1():
    r = int (input("Введите радиус - "))
    pi = 3.14159
    S = pi * r**2
    print ("Площадь круга =", S)

#3.2
def task2():
   a = int (input ("Введите a = "))
   b = int (input ("Введите b ="))
   if a == 0:
     print ("Нет корней")
   else:
      x = -b/a
   print ("x=", x)

#3.3
def task3():
    C = int (input("Введите температуру по Цельсию = "))
    F = 95 * C + 32
    print ("Температура по Фаренгейту =", F)


#3.4
def task4():
     m = int (input ("Введите первое число = "))
     n = int (input ("Введите второе число = "))
     l = int (input ("Введите третье число = "))
     срариф = (m+n+l)/3
     print ("Среднее арифметическое = ", срариф)

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
    print ("Такой задачи в 3й лабораторной нет")
