import json

#12.1
def task1():
    with open("products.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for point in data ["products"]:
        product = point ['name']
        price = point ['price']
        ves = point ['weight']
        if point ['available'] == True:
            available = "В наличии"
        else: available = "Нет в наличии!"

    print(f"Название: {product} \nЦена: {price} \nВес: {ves} \n{available}")

#12.2
def task2():
    with open ('products.json', 'r', encoding='utf-8') as file:
        data = json.load (file)
    newprod = int (input ("Давайте дополним список. Сколько продуктов вам еще хотелось бы? - "))
    for i in range (newprod):
        name = input ("Введите название: ")
        price = int (input (f"Сколько {name} стоит? - "))
        weight = int (input ("Введите вес продукта: "))
        available = input ("А он вообще есть в наличии? (В наличии/Нет в наличии!) -").strip().lower()
        new_product = {"name": name, "price": price, "weight": weight, "available": available}
        data["products"].append(new_product)

    for point in data ["products"]:
        name = point ['name']
        price = point ['price']
        weight = point ['weight']
        print(f"Название: {name} \nЦена: {price} \nВес: {weight}")

    with open("updated_products.json", "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=2)


#12.3
def task3():
    clov = {}
    with open('en-ru.txt', "r", encoding="utf-8") as f:
        for i in f:
            if "-" in i:
                key, value = i.split("-", )
                clov[key.strip()] = value.strip()
    clov1 = {}
    for key in clov:
        if "," in clov[key]:
            tr = clov[key].split(", ")
            for i in tr:
                clov1[i] = key
        else:
            clov1[clov[key]] = key
    clov1 = dict(sorted(clov1.items()))
    with open("ru-en.txt", "w", encoding="utf-8") as f:
        for key, value in clov1.items():
            f.write(f"{key}: {value}\n")


a = int (input ("Введите номер задачи - "))
if a == 1:
    task1()
elif a == 2:
    task2()
elif a == 3:
    task3()