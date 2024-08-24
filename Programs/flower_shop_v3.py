import random as r
import os 
import sys
import pyfiglet
from datetime import datetime
import time

# variables
version = "1.0" # software version

class Flower:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - {self.quantity} шт. на складе ({self.price} руб. за 1 шт.)"
        
    def reduce_quantity(self, amount):
        self.quantity -= amount
    
    def increase_quantity(self, amount):
        self.quantity += amount

class Bouquet:
    def __init__(self, name):
        self.name = name
        self.flowers = {}
    
    def add_flower(self, flower: Flower, quantity):
        flower.reduce_quantity(quantity)
        if flower.name in self.flowers:
            self.flowers[flower.name]['quantity'] += quantity
        else:
            self.flowers[flower.name] = {'flower': flower, 'quantity': quantity}       
    
    def calculate_price(self):
        total_price = 0
        for flower_info in self.flowers.values():
            total_price += flower_info['flower'].price * flower_info['quantity']
        return total_price
    
    def __str__(self):
        bouquet_details = [f"{flower_info['quantity']} x {flower_info['flower'].name}" for flower_info in self.flowers.values()]
        return f"{self.name}: " + ', '.join(bouquet_details) + f" = {self.calculate_price()} руб."

class OrderManager:
    def __init__(self):
        self.flowers = []
        self.bouquets = []
    
    def add_flower(self, name, price, quantity):
        flower = Flower(name, price, quantity)
        self.flowers.append(flower)
    
    def add_bouquet(self, bouquet: Bouquet):
        self.bouquets.append(bouquet)
    
    def restock_flower(self, flower_name, quantity):
        for flower in self.flowers:
            if flower.name == flower_name:
                flower.increase_quantity(quantity)
                break
    
    def list_flowers(self):
        for flower in self.flowers:
            print(flower)
    
    def list_bouquets(self):
        if self.bouquets != []:
            print("\nСоставленные букеты:")
            for bouquet in self.bouquets:
                print(bouquet)
        else:
            print("\nСоставленных букетов нет")        

    def main_menu(self):
        print("\nВыберите действие:\n(1) Показать список цветов\n(2) Пополнить склад\n(3) Составить букет\n(4) Показать список букетов\n(5) Вывести итоговый заказ\n(0) Выход\n(Нужно ввести цифру)")        

    def error(self):
        print("\nВведено некорректное значение, повторите попытку")

    def order_calculation(self):
        total_price = 0
        for bouquet in manager.bouquets:
            total_price += bouquet.calculate_price()  
        manager.list_bouquets()  
        print(f"\nОбщая стоимость заказа: {total_price} руб.")

    def num_check_false(self, num):
        if num == '' or not (num.isdigit()) or int(num) <= 0:
            return True
        return False
    
    def start_database(self, lst_flowers, lst_quantity, lst_price):    
        for el in lst_flowers:
            quan, price = r.choice(lst_quantity), r.choice(lst_price)
            manager.add_flower(el, price, quan)

    def generate_pseudographics_text(self, text):
        ascii_art = pyfiglet.figlet_format(text)
        print(ascii_art)
        print(f"Software version: {version}", f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M')}", sep="\t")

    def type_restock1(self):
        while True:
            cnt = input("\nВведите количество цветов для пополнения склада\n: ")
            if manager.num_check_false(cnt):
                manager.error()
                continue
            break                
        for el in self.flowers:
            manager.restock_flower(el.name, int(cnt))

    def type_restock2(self):
        lst_type = []
        while True:
                num = input("\nКоличество видов цветов для пополнения\n(Всего имеется 5 видов цветов)\n: ")
                if manager.num_check_false(num):
                    manager.error()
                    continue
                if not (1 <= int(num) <= 5):
                    print(f"\nНужно выбрать число в диапазоне от 1 до 5\nПовторите попытку")
                    continue
                break
        for _ in range(int(num)):
            while True:    
                flower_cname = input("\nВыберите номер вида цветка: \n(1) Роза\n(2) Тюльпан\n(3) Лилия\n(4) Хризантема\n(5) Гвоздика\n: ")
                if flower_cname not in '12345' or flower_cname == '':
                    manager.error()
                    continue
                if self.flowers[int(flower_cname)-1].name in lst_type:
                    print("\nДанный вид цветка уже выбран для пополнения\nВыберите другой вид цветка")
                    continue
                break
            lst_type.append(self.flowers[int(flower_cname)-1].name)
            while True:
                cnt = input(f"\nВведите количество цветов для пополнения склада (Текущий цветок - {self.flowers[int(flower_cname)-1].name})\n: ")
                if manager.num_check_false(cnt):
                    manager.error()
                    continue
                break
            manager.restock_flower(self.flowers[int(flower_cname)-1].name, int(cnt))

    def type_bouquet1(self, name):
        n = Bouquet(name)
        while True:
            flower_index = input('\nВыберите букет цветов:\n(1) Букет роз\n(2) Букет тюльпанов\n(3) Букет лилий\n(4) Букет хризантем\n(5) Букет гвоздик\n: ')
            if flower_index not in '12345' or flower_index == '':
                manager.error()
                continue
            if self.flowers[int(flower_index)-1].quantity == 0:
                print("Цветов для выбранного букета нет в наличии, нужно заказать цветы этого вида\nВыберите другой букет")
                continue
            break
        while True:
            num_of_flower = input(f'\nВведите количество цветов для букета\n(Имеется в наличии {self.flowers[int(flower_index)-1].quantity} цветов)\n: ')
            if manager.num_check_false(num_of_flower):
                manager.error()
                continue
            if int(num_of_flower) > self.flowers[int(flower_index)-1].quantity:
                print("\nТакого количетсва цветов нет в наличии\nВыберите меньшее количество цветов")
                continue
            break
        n.add_flower(self.flowers[int(flower_index)-1], int(num_of_flower))
        self.add_bouquet(n)

    def type_bouquet2(self, name):
        n = Bouquet(name)
        lst_type = []
        type_flowers = sum([0 if el.quantity == 0 else 1 for el in self.flowers])     
        while True:
            num = input(f'\nВведите количество видов цветов для букета\n(На складе имеется {type_flowers} видов цветов)\n: ')
            if manager.num_check_false(num):
                manager.error()
                continue
            if not (1 <= int(num) <= type_flowers):
                print(f"\nНужно выбрать число в диапазоне от 1 до {type_flowers}\nПовторите попытку")
                continue
            break
        for _ in range(int(num)):
            while True:
                flower_index = input("\nВыберите вид цветка: \n(1) Роза\n(2) Тюльпан\n(3) Лилия\n(4) Хризантема\n(5) Гвоздика\n: ")
                if flower_index not in '12345' or flower_index == '':
                    manager.error()
                    continue
                if self.flowers[int(flower_index)-1].quantity == 0:
                    print("\nВыбранного вида цветка нет в наличии\nВыберите другой цветок")
                    continue
                if self.flowers[int(flower_index)-1].name in lst_type:
                    print("\nЦветок уже есть в букете\nВыберите другой цветок")
                    continue
                break
            lst_type.append(self.flowers[int(flower_index)-1].name)
            while True:
                num_of_flower = input(f'\nВведите количество цветов для букета\n(Выбранный цветок - {self.flowers[int(flower_index)-1].name}, имеется в наличии {self.flowers[int(flower_index)-1].quantity} цветов)\n: ')
                if manager.num_check_false(num_of_flower):
                    manager.error()
                    continue
                if int(num_of_flower) > self.flowers[int(flower_index)-1].quantity:
                    print("\nТакого количетсва цветов нет в наличии\nВыберите меньшее количество цветов")
                    continue
                break
            n.add_flower(self.flowers[int(flower_index)-1], int(num_of_flower))
        self.add_bouquet(n)

    def extra_restock(self):
        ex_restock = [el.name for el in self.flowers if el.quantity == 0]
        ex_restock = ', '.join(ex_restock)
        if len(ex_restock) != 0: 
            print(f'\nВ наличии нет цветов: {ex_restock}\nНеобходимо пополнить склад')
                             

manager = OrderManager()
lst_flowers = ["Роза", "Тюльпан", "Лилия", "Хризантема", "Гвоздика"]
lst_quantity = [50, 60, 70, 80, 40]
lst_price = [100, 150, 75, 120, 80]
cnt_bouquet, cnt_custom_bouquet = 0, 0
manager.start_database(lst_flowers, lst_quantity, lst_price)


if __name__ == "__main__":
    manager.generate_pseudographics_text("Flowers Inc.")
    while True:
        manager.main_menu()
        action = input(": ")        
        if action not in '012345' or action == '':
            manager.error()
            continue
        else:
            action = int(action)

        if action == 1:
            print("\nЦветы на складе:")
            manager.list_flowers()

        if action == 2:
            while True:
                type_restock = input("\nВыберите тип пополнения:\n(1) Пополнить все виды цветов\n(2) Пополнить выбранные виды цветов\n: ")
                if type_restock not in "12" or type_restock == '':
                    manager.error()
                    continue
                break
            type_restock = int(type_restock)

            if type_restock == 1:
                manager.type_restock1()

            if type_restock == 2:        
                manager.type_restock2()

        if action == 3:
            if  not all(map(lambda x: True if x.quantity == 0 else False, manager.flowers)):
                manager.extra_restock()
                while True:
                    type_bouquet = input("\nВыберите тип букета: \n(1) Стандартный букет\n(2) Произвольный букет\n: ")
                    if type_bouquet not in '12' or type_bouquet == '':
                        manager.error()
                        continue
                    break
                type_bouquet = int(type_bouquet)

                if type_bouquet == 1:
                    cnt_bouquet += 1
                    name = f'Стандартный букет {cnt_bouquet}'
                    manager.type_bouquet1(name)

                if type_bouquet == 2:
                    cnt_custom_bouquet += 1
                    name = f'Произвольный букет {cnt_custom_bouquet}'
                    manager.type_bouquet2(name)
            else:
                print("\nВсе цветы на складе кончились!\nНеобходимо пополнить склад!")    

        if action == 4:
            manager.list_bouquets()

        if action == 5:
            manager.order_calculation()

        if action == 0:
            break    

    print("Программа завершена")
    time.sleep(5)
    if sys.platform.startswith('linux'):
        os.system("clear")
    elif sys.platform.startswith('win32'):
        os.system("cls")
