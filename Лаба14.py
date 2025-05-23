from tkinter import *
import tkinter as tk
from tkinter import font, ttk, messagebox, simpledialog
from PIL import Image, ImageTk, ImageDraw

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, rating, location, time):
        super().__init__(restaurant_name, "мороженое", rating)
        self.location = location
        self.time = time
        self.taste = {"Фруктовый лед": ["Манго-маракуйя", "Апельсин", "Клубника"], "Эскимо": ["Шоколадное"], "Мороженое в рожке": ["Клубника", "Кофе", "Крем-брюле"]}

    def display_flavors(self):
        return "\n".join(
            f"{ice_type.capitalize()}: {', '.join(flavors)}"
            for ice_type, flavors in self.taste.items()
        )

    def add_flavor_to_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if flavor in self.taste[ice_type]:
            return "Такое мороженое уже есть в списке"
        else:
            self.taste[ice_type].append(flavor)
            return "Здорово, новый вкус успешно добавлен!"

    def delete_flavor_from_type(self, ice_type, flavor):
        flavor = flavor.lower()
        if ice_type in self.taste and flavor in self.taste[ice_type]:
            self.taste[ice_type].remove(flavor)
            return "Мороженое успешно удалено"
        else:
            return "Упс, а такого мороженого нет в списке"

    def find_flavor_in_types(self, flavor):
        flavor = flavor.lower()
        for ice_type, flavors in self.taste.items():
            if flavor in flavors:
                return f"Мороженое '{flavor}' есть в '{ice_type}'."
        return "Упс, а такого мороженого нет в списке"

    def add_new_type(self, ice_type):
        if ice_type in self.taste:
            return "Такое мороженое уже есть в списке"
        else:
            self.taste[ice_type] = []
            return "Здорово, новое мороженое успешно добавлен!"


stand = IceCreamStand("Мороженое у Алешки", 5.0, "Геленджик, Набережная, 23", "9-21")
root = tk.Tk()
root.title("Кафе-мороженое — Мороженое у Алешки")
root.geometry("800x600")
img = Image.open("ai-generated-beautuful-ice-cream-background-with-copy-space-free-photo.jpg")
bcg = ImageTk.PhotoImage(img)
background_label = Label(root, image=bcg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

roof_canvas = tk.Canvas(root, width=600, height=200, bg="#f5d5e4", highlightthickness=0)
roof_canvas.pack()
roof_canvas.create_polygon(0, 200, 300, 0, 600, 200, fill="#081073")
roof_canvas.create_rectangle(100, 750, 500, 140, fill="#fff3e0", outline="#6d4c41", width=2)
roof_canvas.create_text(300, 170, text="Мороженое у Алешки", font=(20), fill="#000000")

frame_display = tk.LabelFrame(root, width=700, text="Выбирай мороженку скорее", bg="#FFD073", fg="#880e4f", font=(14))
frame_display.pack(fill="y")

text_display = tk.Text(frame_display, width=50, height=10, bg="#fff", fg="#000000", font=(10))
text_display.pack(padx=10, pady=10)

frame_buttons = tk.Frame(root, bg="#6C8CD5")
frame_buttons.pack(pady=10)

def update_display():
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, stand.display_flavors())

def add_flavor():
    taste = simpledialog.askstring("Добавить новый тип мороженки", "Введите тип мороженого:")
    flavor = simpledialog.askstring("Добавить новый вкус мороженки", "Введите вкус:")
    if taste and flavor:
        msg = stand.add_flavor_to_type(taste.lower(), flavor.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def delete_flavor():
    taste = simpledialog.askstring("Добавить тип мороженки", "Введите тип мороженого:")
    flavor = simpledialog.askstring("Удалить вкус мороженки", "Введите вкус:")
    if taste and flavor:
        msg = stand.delete_flavor_from_type(taste.lower(), flavor.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def add_type():
    taste = simpledialog.askstring("Добавить новый тип мороженки", "Введите новый тип мороженого:")
    if taste:
        msg = stand.add_new_type(taste.lower())
        messagebox.showinfo("Результат", msg)
        update_display()

def find_flavor():
    flavor = simpledialog.askstring("Поиск вкуса", "Введите вкус:")
    if flavor:
        msg = stand.find_flavor_in_types(flavor.lower())
        messagebox.showinfo("Результат", msg)

tk.Button(frame_buttons, text="Добавить новый вкус мороженки", fg="#FFFFFF", command=add_flavor, bg="#200772").grid(row=0, column=0, padx=10, pady=10)
tk.Button(frame_buttons, text="Удалить вкус мороженки",fg="#FFFFFF", command=delete_flavor, bg="#FF0000").grid(row=0, column=1, padx=10, pady=10)
tk.Button(frame_buttons, text="Добавить новый тип мороженки", fg="#FFFFFF", command=add_type, bg="#200772").grid(row=0, column=2, padx=10, pady=10)
tk.Button(frame_buttons, text="Найти вкус мороженки", fg="#FFFFFF", command=find_flavor, bg="#200772").grid(row=0, column=3, padx=5, pady=5)

update_display()
root.mainloop()