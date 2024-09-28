#Работа с файлами и каталогами
#Открытие файла
print(open(r"C:\Python_VSC\python1.txt", "r+"), "\n")         #Открыть файл

#О текущем файле
import os, sys
def current_file():
    print("%-25s%s" % ("Текущий файл:", os.path.abspath(__file__)))
    print("%-25s%s" % ("Текущий рабочий каталог:", os.getcwd()))
    print("%-25s%s" % ("Каталог для импорта:", sys.path[0]))
    print("%-25s%s" % ("Путь к файлу:", os.path.abspath("file.txt")))
    print("-" * 40)
print(current_file(), '\n')

#Редактирование файла
open(r"C:\Python_VSC\python1.txt", "r+")
with open(r"C:\Python_VSC\python1.txt", "r+") as mainfile:
    print(mainfile.write('''Hello everybody.
My name is Egor.
What is your name?
Nice to meet you!
I love you!'''))                                    #Запись в файл
with open(r"C:\Python_VSC\python1.txt", "r+") as mainfile:
    print(mainfile.read())                          #Чтение файла
with open(r"C:\Python_VSC\python1.txt", "r+") as mainfile:
    print(mainfile.close())                         #Закрыть файл

#"Обрезание" файла
#with open(r"C:\python1.txt", "r+") as mainfile:
    #print(mainfile.truncate(25))
    #print(mainfile.read())
    
#Доступ к файлам с помощью модуля os
import os
fileos = os.open(r"C:\Python_VSC\python2.txt", os.O_RDWR)     #Открыть файл
os.write(fileos, b'''That's the second text Python file.
Shall we continue?
Let's go!                                               
''')                                                 #Запись в файл
os.read(fileos, 100)                                 #Чтение файла
os.close(fileos)                                     #Закрыть файл

#Классы StringIO и BytesIO
import io
StrIO = io.StringIO(r"C:\Python_VSC\python2.txt")
print("Класс StringIO — ", StrIO.getvalue())
StrIO.close()
BytIO = io.BytesIO(b"C:\\Python_VSC\\python2.txt")
print("Класс BytesIO — ", BytIO.getvalue(), '\n')
StrIO.close()

#Проверка файла или каталога 
exist1 = os.access(r"C:\Python_VSC\python1.txt", os.F_OK)
exist2 = os.access(r"C:\Python_VSC\python2.txt", os.F_OK)
exist3 = os.access(r"C:\Python_VSC\python3.txt", os.F_OK)
print("Файл 1 существует — ", exist1)
print("Файл 2 существует — ", exist2)
print("Файл 3 существует — ", exist3, '\n')

#Функции для манипулирования файлами
import shutil
open(r"C:\Python_VSC\python3.txt", "r+")
print('Копирование файла — ')
shutil.copyfile(r"C:\Python_VSC\python1.txt", 
                r"C:\Python_VSC\python3.txt")
#print('Перемещение файла — ')
#shutil.move(r"C:\Python_VSC\python1.txt",  r"C:\python3.txt")
#shutil.move(r"C:\python3.txt", r"C:\Python_VSC\python1.txt")
#print('Удаление файла — ')
#os.remove(r"C:\Python_VSC\python1.txt")

print('Проверка пути — ', end="")
if os.path.exists(r"C:\Python_VSC\python1.txt") == True:
    print("путь существует")
else:
    print("путь не существует")
print()

bytetext1 = os.path.getsize(r"C:\Python_VSC\python1.txt")
bytetext2 = os.path.getsize(r"C:\Python_VSC\python2.txt")
bytetext3 = os.path.getsize(r"C:\Python_VSC\python3.txt")
print("Файл 1 в байтах —", bytetext1)
print("Файл 2 в байтах — ", bytetext2)
print("Файл 3 в байтах — ", bytetext3)
import time
lastaccess1 = os.path.getatime(r"C:\Python_VSC\python1.txt")
print("Время последнего доступа — ", lastaccess1)
createtime1 = os.path.getctime(r"C:\Python_VSC\python1.txt")
print("Дата создания файла — ", createtime1, '\n')

#Преобразование пути к файлу или каталогу
import os.path
absolut = os.path.abspath(r"python1.txt")
nameoffile = os.path.basename(r"C:\Python_VSC\python1.txt")
roadfile = os.path.dirname(r"C:\Python_VSC\python1.txt")
print("Абсолютный путь — ", absolut)
print("Имя файла без пути — ", nameoffile)
print("Путь к каталогу — ", roadfile, '\n')

#Сохранение объектов в файл
import pickle
print("Cохранение объектов в файл — ")
filething = open(r"C:\Python_VSC\python3.txt", "wb")
obj = ["Hello", (2, 3)]
print('Загружаемые объекты — ', obj)
pickle.dump (obj, filething)                            #Запись dump
filething.close()
filething = open(r"C:\Python_VSC\python3.txt", "rb")
obj = pickle.load(filething)                            #Чтение pickle
print('Загруженные объекты — ', obj)
filething.close()

#Функции для работы с каталогами
import os
print('Создание каталога — ', os.mkdir("Новая папка"))
print('Удаление каталога — ', os.rmdir("Новая папка"))
print('Cписок объектов — ', os.listdir(r"C:\Python_VSC"))
if os.path.isdir (r"C:\Python_VSC\python3.txt") == True:
    print("Это каталог")
else:
     print("Это не каталог")
if os.path.isfile(r"C:\Python_VSC\python3.txt") == True:
    print("Это файл")
else:
     print("Это не файл")
print()

#Работа с графикой
#Открытие файла
from PIL import Image
img = Image.open(r"C:\Users\suxra\OneDrive\Рабочий стол\Развитие\Python\Python_Proh\Кусакабе.jpg")
print('Размер изображения — ', img.size)
print('Формат изображения — ', img.format)
img.close()     #Закрыть изображение
img = Image.open(r"C:\Users\suxra\OneDrive\Рабочий стол\Развитие\Python\Python_Proh\Кусакабе.jpg")
obj = img.load()
print('Цвет пиксела — ', obj[25, 45])
#print('Просмотр изображения — ', img.show())
#print('Cохранение в формате — ', img.save('Кусакабе.jpg'))

#Создание нового изображения
#Черный квадрат
blacksquare1 = Image.new("RGB", (100, 100), (0, 0, 0))  
#Красный квадрат
blacksquare2 = Image.new("RGB", (100, 100), (255, 0, 0))
#Зеленый квадрат
blacksquare3 = Image.new("RGB", (100, 100), (0, 255, 0))
#Синий квадрат
blacksquare4 = Image.new("RGB", (100, 100), (0, 0, 255))
#print('Изображение квадрата — ', blacksquare4.show())
print()

#Получение информации об изображении
img = Image.open(r"C:\Users\suxra\OneDrive\Рабочий стол\Развитие\Python\Python_Proh\Кусакабе.jpg")
print('Ширина изображения — ', img.width)
print('Высота изображения — ', img.height)
print('Формат изображения — ', img.format)
print('Режим изображения — ', img.mode)
print('Путь к изображению — ', img.filename, '\n')

#Рисование линий и фигур
from PIL import Image, ImageDraw
img2 = Image.new("RGB", (300, 300), (255, 255, 255))
draw = ImageDraw.Draw(img2)
#Красная горизонтальная линия из точек
for n in range(5, 31) :
    draw.point((n, 5), fill=(255, 0, 0))
#Линия между двумя точками
draw.line((0, 0, 0, 300), fill=(0, 128, 0))
draw.line((297, 0, 297, 300), fill=(0, 128, 0), width=3)
#Прямоугольники
draw.rectangle((10, 10, 30, 30), fill=(0, 0, 255), outline=(0, 0, 0))
draw.rectangle((40, 10, 60, 30), fill=(0, 0, 128))
draw.rectangle((0, 0, 299, 299), outline=(0, 0, 0))
#Многоугольники
draw.polygon((50, 50, 150, 150, 50, 150), outline= (0,0,0), fill=(255, 0, 0))
draw.polygon((200, 200, 250, 200, 275, 250, 250, 300, 200, 300, 175, 250), fill=(255, 255, 0))
#Эллипсы
draw.ellipse((100, 100, 200, 200), fill= (255, 255, 0))
draw.ellipse((50, 170, 150, 300), outline=(0, 255, 255))
#Обычная дуга
draw.arc((10, 10, 290, 290), 180, 0, fill=(255, 0, 0))
#Сектор
draw.pieslice((10, 10, 290, 290), -90, 0, fill="red")

#Вывод текста
from PIL import ImageFont
font = ImageFont.load_default()
draw.text((10, 10), "Hello", font=font, fill="red")
#img2.show()

#Создание скриншотов
from PIL import ImageGrab
img3 = ImageGrab.grab()
img3.save("screen.bmp", "BMP")
img3.size
img3.mode
img3.show
