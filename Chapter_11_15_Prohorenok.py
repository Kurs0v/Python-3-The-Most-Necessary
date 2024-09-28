#Пользовательские функции
from os import name
from webbrowser import get

def func1(): return
print("Первая функция — ", func1())
def func2(x2):
    return x2
print("Вторая функция — ", func2(2))
def func3(x3, y3, z3):
    return x3 + y3 + z3
print("Третья функция — ", func3(3, 15, 22)) 
def conсlist(х4, у4):
    return х4 + у4
print("Четвертая функция — ", conсlist("Конкатенация ", "строк"))
def func5(f5, x5, y5, z5):
    return f5(x5, y5, z5)
print("Пятая функция — ", func5(func3, 21, 47, 101))

#Определение функции в зависимости от условия
x6 = 1
if x6 == 1:
    def func6():
        return print("Шестая функция — это 1") 
else:
    def func6():
        return print("Шестая функция — это не 1")
print(func6())

#Сопоставление по ключам 
def func7(x7 = 121, y7 = 373):
    return x7 + y7
print("Седьмая функция — ", func7())

#Передача функции произвольного количества параметров
def func8(*x8):
    res = 0
    for i in x8: 
        res += i
    return res
print("Восьмая функция — ", func8(10, 81, 621, 2819))

#Анонимные функции
anonfunc1 = lambda: 10 + 20
anonfunc2 = lambda х, у: х + у
anonfunc3 = lambda х1, у1, z1 = 1912: х1 + у1 + z1
print("Анонимная функция 1 — ", anonfunc1()) 
print("Анонимная функция 2 — ", anonfunc2(15, 101))
print("Анонимная функция 3 — ", anonfunc3(25, 210, 1992)) 

#Функции-генераторы
def func9(x9, у9):
    for i in range(1, x9+1) :
        yield i ** у9
print("Девятая функция — квадрат")
for n in func9(10, 2):
    print(n, end=" ") 
print("\nДесятая функция — куб")
for n in func9(10, 3):
    print(n, end=" " )
print()

#Вложенные функции
def vlofunc1(x):
    def vlofunc2():
        print(x)
    return vlofunc2
avf1 = vlofunc1(10)
avf2 = vlofunc1(99)
print("Вложенные функция 1 — ", avf1())
print("Вложенные функция 2 — ", avf2())

#Модули и пакеты
print(__name__)  
#Импорт модулей
import time, math
print("Функция getattr() — ", getattr(math, "pi"))
import math as m 
print("Псевноним модуля — ", m.pi)

#Инструкция from
from math import pi, floor as f
print("Инструкция from — ", pi)
aa, bb, cc, xx, yy, zz, ss =  10, 20, 30, 40 ,50, 60, 70
__all__ = ['aa', 'ss']
print('Атрибут __all__ — ',sorted(vars().keys()))

#Пути поиска модулей
import sys 
print('Модули sys — ')
sys.path

#Объектно-ориентированное программирование
#Создание атрибута и метода класса
class MyClass:
    def __init__(self): 
        self.x = 10 
    def print_x(self): 
        print(self.x) 
c = MyClass() 
print('Вызов атрибута и метода 1 — ', c.print_x())
print('Вызов атрибута и метода 2 — ', c.x)

#Методы__init_() и __del__()
class MyClass2:
    def __init__(self, value1, value2):
        self.x = value1
        self.у = value2
c = MyClass2(100, 300)
print('Метод __init__  ', c.x, c.у) 
class MyClass3:
    def __init__(self): 
        print ("Вызван метод __init__О")
    def __del__(self): 
        print("Вызван метод del ()")
cl = MyClass3()
del cl 
с2 = MyClass3()
сЗ = с2 
del с2 
del сЗ

#Обработка исключений
try: 
    х14 = 1 / 0
except ZeroDivisionError:
    print('Обработали деление на 0')
    х14 = 0
print('В результате — ', х14)

#Блоки else и finally
try:
    х15 = 10 / 0
except ZeroDivisionError:
    print("Деление на 0")
else:
    print('Блок else')
finally:
    print("Елок finally")

#Итераторы
class ReverseString:
    def __init__(self, s16):
        self.__s = s16
    def __iter__(self):
        self.__i = 0
        return self
    def __next__(self):
        if self.__i > len(self.__s) - 1:
            raise StopIteration
        else:
            a = self.__s[-self.__i - 1]
            self.__i = self.__i + 1
            return a
s16 = ReverseString('Презентация')
print('Класс-итератор — ', end="")
for a in s16:
    print(a, end="")
    
#Перечисление
from enum import Enum
class Versions(Enum):
    V2_7 = "2.7"
    V3_6 = "3.6"
from enum import IntEnum
print('\nПеречисление 1 — ', Versions("2.7"))
class Colors(IntEnum):
    Red = 1
    Green = 2
    Blue = 3
print('Перечисление 2 — ', Colors(1))
from enum import Enum
class Versions2(Enum):
    V2_7 = "2.7"
    V3_6 = "3.6"
    MostFresh = "3.6"
print('Перечисление 3 — ', Versions2("3.6"))
    