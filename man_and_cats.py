# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код
class Cat:
    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullness = 5

    def __str__(self):
        return f'Я {self.name}, сытность:{self.fullness}'

    def take_cat(self, house):
        self.house = house


    def eat_cat(self):
        if self.house.food > 15:
            self.fullness+=30
            self.house.food-=10
            print(f'{self.name} поела')
    def sleep(self):
        self.fullness -=10
        print(f'{self.name} поспала')

    def pay_cat_food(self):
        if self.house.money > 40:
            self.house.food += 50
            self.house.money -= 30
            print('Хозяин пощел в магазин за едой')
        else:
            print('Нет денег')

    def crush(self):
        self.house.mud += 30
        self.fullness -=10
        print(f'{self.name} подрала обои')

    def act_cat(self):
        dice = randint(1, 6)
        if self.fullness <= 0:
            print(f'{self.name} умерла....')
            return

        if self.fullness <= 35:
            self.eat_cat()
        elif self.house.food < 20:
            self.pay_cat_food()
        elif dice == 1:
            self.sleep()
        else:
            self.crush()

class Man:
    def __init__(self, name):
        self.name = name
        self.man_fullness = 100
    def __str__(self):
        return f'{self.name}, сытость: {self.man_fullness}'

    def take_cat(self, house, cat):
        self.house = house
        self.house.mud += 30
        print(f'В дом въехал {cat.name}')
    def work(self):
        self.house.money += 100
        self.man_fullness -= 25
        self.house.mud += 5
        print(f'{self.name} пошел на работу')

    def eat_human(self):
        if self.house.human_food > 15:
            self.house.human_food -= 10
            self.man_fullness += 40
            self.house.mud += 5
            print(f'{self.name} поел')
        else:
            print('Нет еды!!!')

    def pay_food(self):
        if self.house.money > 31:
            self.house.human_food += 100
            self.house.money -= 30
            self.man_fullness -= 20
            self.house.mud += 5
            print(f'{self.name} купил еды')
        else:
            print('Нет денег')

    def clienning(self):
        self.house.mud -= 20
        self.man_fullness -= 20
        print(f'{self.name} делает уборку')

    def play_DOTA(self):
        self.man_fullness -= 20
        self.house.mud += 5
        print(f'{self.name} играет Дота')

    def act_human(self):
        dice = randint(1, 6)
        if self.man_fullness <= 0:
            print(f'{self.name} умер....')
            return

        if self.man_fullness <= 35:
            self.eat_human()
        elif self.house.money <= 40:
            self.work()
        elif self.house.human_food < 20:
            self.pay_food()
        elif self.house.mud > 100:
            self.clienning()

        elif dice == 1:
            self.work()
        else:
            self.play_DOTA()



class House:
    def __init__(self, house):
        self.house = house
        self.human_food = 40
        self.food = 50
        self.money = 0
        self.mud = 0
    def __str__(self):
        return f'В доме еды:{self.human_food}, кошачей еды: {self.food}, денег:{self.money} и грязи:{self.mud}'

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)

Vasia = Man('Вассилий')
my_house = House(house='My_sweet_house')
citty = Cat('Kittyy', house='My_sweet_house')

Vasia.take_cat(house=my_house, cat=citty)
citty.take_cat(house=my_house)

for day in range(1, 366):
    print(Vasia)
    print(citty)
    print(my_house)
    print(f'-------Day:{day}----------')
    Vasia.act_human()
    citty.act_cat()

