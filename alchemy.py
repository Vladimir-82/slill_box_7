# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код
# elements = 'Вода Воздух Огонь Земля Шторм Пар Грязь Молния Пыль Лава'.split()
class Water:
    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return self.name

    def __add__(self, other):
        result = Water()
        if other.name == 'Воздух':
            result = self.name + ' + ' + other.name + ' = ' + 'шторм'
            return result
        elif other.name == 'Огонь':
            result = self.name + ' + ' + other.name + ' = ' + 'пар'
            return result
        elif other.name == 'земля':
            result = self.name + ' + ' + other.name + ' = ' + 'грязь'
            return result
        else:
            return 'Nothing'




class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return self.name

    def __add__(self, other):
        result = Water()
        if other.name == 'Огонь':
            result = self.name + ' + ' + other.name + ' = ' + 'молния'
            return result
        elif other.name == 'земля':
            result = self.name + ' + ' + other.name + ' = ' + 'пыль'
            return result
        else:
            return 'Nothing'


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return self.name

    def __add__(self, other):
        result = Water()
        if other.name == 'земля':
            result = self.name + ' + ' + other.name + ' = ' + 'лава'
            return result

        else:
            return 'Nothing'

class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return self.name


class Steam:
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return self.name

class Soil:
    def __init__(self):
        self.name = 'земля'

    def __str__(self):
        return self.name

class Mud:
    def __init__(self):
        self.name = 'грязь'

    def __str__(self):
        return self.name


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return self.name


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return self.name


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return self.name


my_water = Water()
my_air = Air()
my_storm = Storm()
my_fire = Fire()
my_soil = Soil()
my_mud = Mud()


print(my_water + my_air)
print(my_water + my_fire)
print(my_water + my_soil)
print(my_air + my_fire)
print(my_air + my_soil)
print(my_fire + my_soil)

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
