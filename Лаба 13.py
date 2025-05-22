#13.1
def task1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print (f"Название ресторана - {self.restaurant_name} \nТип кухни - {self.cuisine_type}")
        def open_restaurant(self):
            print ("Ресторан открыт")

    newRestaurant = Restaurant("Шашлыки у Казумата", "шашлычная")

    print (newRestaurant.restaurant_name)
    print (newRestaurant.cuisine_type)
    print()
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

#13.2
def task2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name} \nТип кухни - {self.cuisine_type}")

        def open_restaurant(self):
            print("Ресторан открыт")

    newRestaurant1 = Restaurant("Шаурмечная у Артура", "фастфуд")
    newRestaurant2 = Restaurant("Блинная у Агафьи", "завтраки")
    newRestaurant3 = Restaurant("Кофейня Бурак", "кофейня")

    print(newRestaurant1.describe_restaurant (), newRestaurant2.describe_restaurant (), newRestaurant3.describe_restaurant ())

#13.3
def task3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print (f"Название ресторана - {self.restaurant_name} \nТип кухни - {self.cuisine_type}")
        def open_restaurant(self):
            print ("Ресторан открыт")

        def new_rating(self, new_rating):
            self.rating = new_rating
            print (f"Новый рейтинг {self.restaurant_name} - {self.rating}")

    newRestaurant = Restaurant("Шашлыки у Казумата", "шашлычная", 4.0)

    print(f"{newRestaurant.describe_restaurant()} \nИзначальный рейтинг {newRestaurant.rating}")
    print(newRestaurant.new_rating(4.9))


a = int (input ("Введите номер задачи - "))
if a == 1:
    task1()
elif a == 2:
    task2()
elif a == 3:
    task3()
