#6.1
def task1():
    def del3(x):
       if x % 3 == 0:
          print (f"{x} кратно 3")
       else:
           print (f"{x} не кратно 3")
    b = int (input("Введите число - "))
    del3(b)

#6.2
def task2():
    def del100():
       try:
           x = int(input("Введите число, на которое хотите поделить - "))
           b = 100/x
           print (f"Результат деления 100 на {x} равен {b}")
       except ValueError:
           print("Ошибка! Введенное значение - не число!")
       except ZeroDivisionError:
           print("Ошибка! Деление на ноль!")

    print (del100())

#6.3
def task3():
    from datetime import datetime
    def mg(date):
         x = datetime.strptime(date, "%d.%m.%Y")
         if x.day * x.month == int(str(x.year)[-2:]):
             return True, "Магическая дата"
         return False, "Немагическая дата"

    date = input ("Введите дату в формате DD.MM.ГГГГ (Прим. 02.02.2222) - ")
    print (mg(date))

#6.4
def task4():
    def num (x):
        if len (x) % 2 == 0:
           first = len (x) / 2
           sum1 = 0
           sum2 = 0
           for n in range (len (x)):
               if n < first:
                   sum1 += int (x[n])
               else:
                   sum2 += int (x[n])
           if sum1 == sum2:
               print ("Билет счастливый")
           else:
               print ("Билет несчастливый")
        else:
            print ("Ошибка, номер билета должен содержать четное количество цифр")

    c = input ("Введите номер билета - ")
    print (num(c))


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
    print ("Такой задачи в 6й лабораторной нет")






