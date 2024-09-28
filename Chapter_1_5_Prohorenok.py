#Самое начало
print('Привет мир! \n')

#В одну строку
x = 1; y = 2; print('В одну строку — ', x + y, "\n")

#Перенос значений
qwe = 1 + 2 + 3 + 4 + \
    5 + 6 + 7 + 8
print('Перенос значений — ', qwe, "\n")

#Комментарий
"""
Тут много текста 
Всем привет
Кого не видел
"""
print('Сверху комментарий \n')

#Убрать пробел sep
print('Без пробела sep="" - ') 
print('Кален', 'Дарь', sep="")
print("\n")

#name = input('Введите ваше имя: ')
#print("Ваше имя: ", name)
#print("\n")

#Список
for i in [1, 2, 3]:
    print("Элемент списка — ", i)
for i in "Презентация":
    print(i + "-", end="")
print("\n")

#Равенство чисел
decade1 = decade2 = 5; decade3 = 10
print('Равенство чисел — ', decade1, decade2, decade3, 
      decade1 is decade2, decade2 is decade3, "\n")

#Позиционное присваивание
p, o, s = 20, 40, 60
print("Позиционное присваивание — ", p,o,s, "=", p + o + s, "\n")

#num24_x = int(input('num24_x = '))
#num24_y = int(input('num24_y = '))
#print('Сложение вручных данных', num24_x+num24_y)

#Двоичные операторы 
x1 = 275
x2 = 859
print("Двоичное И — ", x1 & x2)
print("Двоичное ИЛИ — ", x1 | x2)
print("Исключающее ИЛИ — ", x1 ^ x2, "\n")

#Последовательности
s1 = "Привет "
s2 = "всем"
print("Конкатенация — ", s1 + s2)
print("Повторение — ", s1 * 5)
print("Вхождение — ", s1 in s2, s2 in s1)
print("Невхождение — ", s1 not in s2, s2 not in s1, "\n")

#Присваивание
pq = 250
pq += 10
print("Инкремент —", pq)
pq -= 10
print("Декремент — ", pq)
pq *= 10
print("Умножение на n раз — ", pq)
pq /= 10
print("Деление на n раз — ", pq)
pq %= 10
print("Деление по модулю на n раз — ", pq)
pq **= 10
print("Возведение в степень n — ", pq, "\n")

#Проверка на четность
chet = 22
if chet % 2 == 0: 
    print(chet, "четное")
else: 
    print(chet, "нечетное") 
print("\n")

#Цикл for
for x in range(1, 5):
    print("Номер №", x, "в цикле for")
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    arr[i] *= 2
print("Результат for", arr)
arr2 = range(1,5)
print(arr2)
print("Входимость в диапазон — ", arr2.count(1))
print("Входимость в диапазон — ", arr2.count(20), "\n")

#Цикл while
w1 = 1
while w1 <= 4:
    print("Номер №", w1, "в цикле while")
    w1 += 1
arr3 = [1, 2, 3, 4]
i, count = 0, len(arr3)
while i <count:
    arr3[i] *= 2
    i += 1
print("Результат while*2", arr3, "\n")

#Числа
from fraction import Fraction
print('Дробь fraction — ', Fraction(4, 5))
print('Системы счисления')
c2v10, c8v10, c16v10 = 0b00101001, 0o72, 0xFF
print('Из 2 в 10 — ', c2v10)
print('Из 8 в 10 — ', c8v10)
print('Из 16 в 10 — ', c16v10)
chis = 5421
print("Из 10 в 2 — ", bin(chis))
print("Из 10 в 8 — ", oct(chis))
print("Из 10 в 16 — ", hex(chis), "\n")

#Модуль math
import math
print('Число Пи — ', math.pi)
print('Экспонента — ', math.e)
print('Число Пи (град) — ', math.degrees(math.pi))
print('Число Пи (рад) — ', math.radians(math.pi))
print('Десятичный логарифм — ', math.log10(chis))
print('Двоичный логарифм — ', math.log2(chis))
print('Квадратный корень — ', math.sqrt(chis))
print('Округ вверх — ', math.ceil(chis))
print('Округ вниз — ', math.floor(chis))
print('Возведение в степень — ', math.pow(chis, 1))
print('Абсолютное значение — ', math.fabs(chis))
print('Остаток от деления — ', math.fmod(chis, 2), "\n")
#print('Факториал', math.factorial(chis))

#Модуль random
import random
print('Рандом', random.random())
print('Рандом float от 1 до 50 — ', random.uniform(0, 50))
print('Рандом int от 1 до 50 — ', random.randint(0, 50))
print('Рандом диапазон 50 — ', random.randrange(0, 50))


