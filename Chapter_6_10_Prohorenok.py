#СТРОКИ
s = 'Определите вид предложений по составу грамматической основы.'

#Индекс
print('1-ый индекс — ', s[0])
print('2-ой индекс — ', s[1])
print('7-ой индекс — ', s[6])
print('Последний индекс — ', s[-1])
print('Длина строки — ', len(s), "\n")

#Фиксация строки
print(r'Фиксированная \n строка \n строк')
print('Путь к файлу 1-ый способ — ', r'C:\Users\Python.exe')
print('Путь к файлу 2-ой способ — ', 'C:\\Users\\Python.exe', "\n")

#Срезы
print('Вся строка — ', s[:])
print('Обратный порядок — ', s[::-1])
print('Замена первого символа — ', "O", s[1:])
print('Удаление последнего символа — ', s[:-1])
print('Первый символ — ', s[0:1])
print('Последний символ — ', s[-1:])
print('Индексы 2-14 — ', s[2:14])
print('Конкатенация символов — ', s[0:7] + s[7:14])
print("Добавление str — ", s, str(10), "\n")

#Точность знаков
import math
from posixpath import splitext
print('Точность знаков после запятой float — ', '%.5f' % math.pi, "\n")

#Регистры символов
print('Все заглавные — ', s.upper())
print('Все строчные — ', s.lower())
print('Регистр наоборот — ', s.swapcase())
print('Первая заглавная — ', s.capitalize())
print('Первая строчная — ', s.title(), "\n")

#Код символа
print('Символ по коду — ', chr(1055))
print('Код по символу — ', ord("П"), "\n")

#Поиск в строке
print('Найти позицию find: ', s.find('Pres'))
print('Вхождение в строку count: ', s.count('e'))
print('Замена replace: ', s.replace("ation", ""), "\n")

#Тип содержимого
from curses.ascii import isalnum, isalpha, isdigit, isupper, islower
print('Только буквы/цифры? ', s. isalnum())
print('Только буквы? ', s.isalpha())
print('Только цифры? ', s.isdigit())
print('Только верхний регистр? ', s.isupper())
print('Только нижний регистр? ', s.islower(), "\n")

#Вычисление выражений в форме строки
print('eval 2 * 3 =', eval('2*3'), "\n")

#Шифрование строк
import hashlib
h = hashlib.sha256(b"password")
print('Шифр sha256 бинарный — ', h.digest())
print('Шифр sha256 — ', h.hexdigest())
h2 = hashlib.md5(b"password")
print('Шифр md5 — ', h2.hexdigest(), "\n")

#Регулярные выражения
import re

#Проверка ввода даты 
dateth = '20.11.2012'
rv1 = re.compile(r'[0-9][0-9][.][0-9][0-9][.][0-9][0-9][0-9][0-9]')
if rv1.search(dateth):
    print('Дата введена верно!')
else:
    print('Дата введена неверно!')

#Проверка наличия текста
bisytext = 'Анализируйте данные бизнеса с помощью инструмента!'
rv2 = re.compile(r'[а-яА-ЯёЁ]')
if rv2.search(bisytext):
    print('Здесь текст!')
else:
    print('Здесь нет текста!')

#Проверка наличия чисел в тексте
numtext = 'Агент 21 прибыл на планету 5 в 14 часов 48 минут'
rv3 = re.compile(r'[0-9]+')
print('Цифры из текста согласно шаблону —', rv3.findall(numtext))

#Метод split
splittext = 'Он,ушел,а,она,уехала.Теперь,они,не,вместе.'
rv4 = re.compile(r'[\s,.]+')
print('Деление split', rv4.split(splittext), '\n')


#Список
templist = [1, 2, 3, 4, 5]
print('Временный список — ', templist, type(templist))
print('Элементы списка — ', templist[0], templist[2], templist[4])
templist2 = [1, 2, 3, 4, 5]
templist2[0] = 10
print('Временный список 2 — ', templist2, type(templist2))

#Кортеж
temptuple = (1, 2, 3, 4, 5)
print('Временный кортеж — ', temptuple, type(temptuple))
print('Элементы кортежа — ', temptuple[0], temptuple[2], temptuple[4]) 

#Множество
tempset = set([1, 1, 2, 3, 4, 4, 5])
print('Временное множество — ', tempset, type(tempset))

#Диапазон
temprange = range(0, 100, 25)
print('Элементы диапазона —')
for i in temprange: 
    print(i)
print('\n')

#Создание списка
newlist = [1, 5, 10, 15, 20]
print('Новый список — ', newlist, type(newlist))

#Добавление элемента списка
emptylist = []
emptylist.append(10)
emptylist.append(20)
emptylist.append(30)
print('Добавление элементов в список — ', emptylist)

#Изменение элемента списка
emptylist[2] = 1000
print('Изменение элемента списка — ', emptylist)
emptylist[2] = 30

#Повторение элемента списка
replist = emptylist * 3
print('Повторение элементов списка — ', replist)

#Копирование списка
coplist = emptylist.copy()
print('Скопированный список — ', coplist)

#Последний элемент списка
print('Последний элемент списка — ',  coplist[len(coplist) - 1], '\n')

#Многомерный список
multilist = [ 
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
print('Элементы многомерного списка — ', 
      multilist[0][2], #первая строка третий столбец
      multilist[1][1], #вторая строка второй столбец
      multilist[1][0], '\n') #вторая строка первый столбец

#Сложение элементов списка
ziplist1 = [2, 5, 8]
ziplist2 = [4, 6, 2]
ziplist3 = [7, 1, 3]
print('Сложение списков zip — ', 
      [ziplist1 + ziplist2 + ziplist3 
       for (ziplist1, ziplist2, ziplist3) in zip(ziplist1, ziplist2, ziplist3)], '\n')

#Добавление элементов списка
coplist.append(40)
print('Добавить один элемент в конец списка —', coplist)
coplist.extend([50, 60])
print('Добавить много элементов в конец списка — ', coplist)

#Удаление элементов списка
del coplist[4:]
print('Удалить элементы списка — ', coplist)

#Переворачивание списка
coplist.reverse()
print('Переворачивание списка — ', coplist)

#Перемешивание списка
import random
random.shuffle(coplist)
print('Перемешивание списка — ', coplist)

#Сортировка списка
coplist.sort()
print('Сортировка списка — ', coplist)

#Преобразование списка в строку
print('Из list в str — ', " ".join(map(str, coplist)))
print('Проверка типа "str" — ', type(" ".join(map(str, coplist))), '\n')

#Создание кортежа
newtuple = (1, "pon", 2, "vlan", 4, 5)
print('Новый кортеж — ', newtuple, type(newtuple))
print('Элементы кортежа — ', newtuple[0], newtuple[1], newtuple[3])

#Создание множества
newrange = set()
print('Новое пустое множество —', newrange, type(newrange))

#Конвертация в множество
print('Из str в set —', set(s))
print('Из list в set — ', set(newlist))
print('Из tuple в set — ', set(newtuple), '\n')

#Объединение множеств
print('Объединение множеств — ', set(s) | set(newlist) | set(newtuple))

#Копирование множества
unionset = set('АБВ') | set([1, 2, 3]) | set((1, 2, 3))
copyset = unionset.copy()
print('Копия множества —', copyset)

#Добавить и удалить элемент множества
copyset.add(4)
print('Добавление элемента во множество — ', copyset)
copyset.remove(4)
print('Удаление элемента из множества — ', copyset, '\n')

#Создание диапазона
newrange = range(1, 10)
print('Новый диапазон — ', newrange, type(newrange))
print('Из range в list — ', list(newrange))
print('Из range в tuple — ', tuple(newrange))
print('Из range в set — ', set(newrange), '\n')

#Cловари
newdict = dict(
    [('a', 1),
     ('b', 2),
     ('c', 3),
     ('d', 4)] 
    )
print('Новый словарь — ', newdict, type(newdict))

#Объединение словарей
key = [8, 5, 6, 9, 7]
value = ['Виноград', 'Банан', 'Яблоко', 'Грейпфрут', 'Авокадо']
fruitdict = dict(zip(key, value))
print('Объединение словарей — ', fruitdict,)

#Операции над словарями
print('Элементы словаря  — ', fruitdict[8], fruitdict[5], 
      fruitdict[6], fruitdict[9])
print('Существование ключа — ', 8 in fruitdict, 341 in fruitdict)
print('Отсутствие ключа — ', 8 not in fruitdict, 341 not in fruitdict)

#Добавить и удалить элементы словаря
fruitdict[10] = 'Наранхилья'
fruitdict[11] = 'Финики деглет'
print('Добавить элементы словаря — ', fruitdict)
print('Длина словаря — ', len(fruitdict))
del fruitdict[10]
del fruitdict[11]
print('Удалить элементы словаря — ', fruitdict, '\n')

#Перебор элементов словаря
print('Перебор элементов словаря 1 — ')
for key in fruitdict.keys():
    print( "({0} -> {1})".format(key, fruitdict[key]), end=" " '\n')
print('Перебор элементов словаря 2 — ')
for key in sorted(fruitdict):
    print("({0} -> {1})".format(key, fruitdict[key]), end=" " '\n')
print('\n')

#Методы для работы со словарями
keys_plus = newdict.keys() | fruitdict.keys() 
print('Объединение ключей словаря — ', keys_plus)
keys_minus1 = newdict.keys() - fruitdict.keys()
print('Разница ключей словаря 1 — ', keys_minus1)
keys_minus2 =  fruitdict.keys() - newdict.keys()
print('Разница ключей словаря 2 — ', keys_minus2)
keys_same = newdict.keys() & fruitdict.keys()
print('Одинаковые ключи — ', keys_same)
keys_unique = newdict.keys() ^ fruitdict.keys()
print('Уникальные ключи — ', keys_unique, '\n')

#Дата и время
#Получение текущих даты и времени
import time 
print('Количество секунд time — ', time.time())
print('Начало эпохи gmtime — ', time.gmtime(0))
print('Текущая дата и время gmtime — ', time.gmtime())
print('Дата по числу gmtime — ', time.gmtime(155111716.0))
print('Текущая дата и время localtime — ', time.localtime())
print('Дата по числу localtime — ', time.localtime(155111716.0), '\n')

#Время и дата по спискам
d = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
m = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
t = time.localtime()
print("Сегодня:\n%s %s %s %s %02d:%02d:%02d\n%02d.%02d.%02d" %
      (d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t [5], t[2], t[1], t[0]), '\n')

#Форматирование даты и времени
print('Форматирование даты — ', time.strftime("%d.%m.%Y"))
print('Форматирование времени — ', time.strftime("%H:%M:%S"))
print('Форматирование времени — ', time.strftime("%H:%M:%S", time.localtime(1321954972.0)))
print('Текущая дата и время asctime — ', time.asctime())
print('Текущая дата и время ctime — ', time.ctime())
print('Прерывание на время sleep — ', time.sleep(5), '\n')

#Модуль datetime
import datetime
deltatime1 = datetime.timedelta(hours=10, minutes=45, seconds=12)
print('Время timedelta 1 — ', deltatime1)
deltatime2 = datetime.timedelta(hours=5, minutes=22, seconds=37)
print('Время timedelta 2 — ', deltatime2)
print('Сложение времени —', deltatime1 + deltatime2)
print('Вычитание времени —', deltatime1 - deltatime2)
print('Умножение времени —', deltatime2 * 2)
print('Деление времени —', deltatime1 // 5, '\n')

#Модуль date
datedi = datetime.date(1999, 2, 17)
print('Дата date — ', datedi)
print('Текущая дата date — ', datetime.date.today())
t = datetime.timedelta(days=10)
print('Прибавить дату — ', datedi + t)
print('Убавить дату — ', datedi - t)
print('Формат ГГГГ-ММ-ДД — ', datedi.isoformat())
print('Порядковый номер дня в неделе — ', datedi.isoweekday(), '\n')

#Модуль calendar
import calendar
calen = calendar.TextCalendar(0)
print('Календарь 2020 год — ', calen.formatyear(2020))
month = 11
print('Месяц 2020 год — ', calendar.month (2017, month))