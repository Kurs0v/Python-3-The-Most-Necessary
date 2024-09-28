#Интернет-программирование
#Разбор URL
from urllib.parse import urlparse
url1 = urlparse("http://www.examples.ru:80/test.php;st?var=5#metka")
print('Разбор URL по составляющим —', list(url1))
print('Протокол —', url1.scheme)
print('Домен и номер порта —', url1.netloc)
print('Домен без порта —', url1.hostname)
print('Номер порта —', url1.port)
print('Путь —', url1.path)
print('Параметры —', url1.params)
print('Строка запроса —', url1.query)
print('Якорь —', url1.fragment)
print('Изначальный адрес —', url1.geturl, "\n")

#Разбор FTP
ftp = urlparse("ftp://egor:123456@yandex.ru")
print("Составляющие FTP —", ftp.scheme, ftp.hostname, ftp.username, ftp.password, '\n')

#Преобразование относительного URL-адреса в абсолютный
from urllib.parse import urljoin
OinA1 = urljoin('http://www.examples.ru/fl/f2/test.html', 'file.html')
print('Относительный адрес как абсолютный 1 —', OinA1)
OinA2 = urljoin('http://www.examples.ru/fl/f2/test.html', 'f3/file.html')
print('Относительный адрес как абсолютный 2 —', OinA2)
OinA3 = urljoin('http://www.examples.ru/fl/f2/test.html', '/file.html')
print('Относительный адрес как абсолютный 3 —', OinA3, '\n')

#Разбор HTML-эквивалентов
from xml.sax.saxutils import escape, quoteattr
ekvi_str = """ &<>" """
print('HTML-эквиваленты 1 —', escape(ekvi_str))
print('HTML-эквиваленты 2 —', quoteattr(ekvi_str), '\n')

#Определение кодировки
import chardet 
chardet.__version__
print('Определение кодировки 1 —', chardet.detect(bytes("Строка", "cp1251")))
print('Определение кодировки 2 —', chardet.detect(bytes("Строка", "koi8-r")))
print('Определение кодировки 3 —', chardet.detect(bytes("Строка", "utf-8")))
print('Определение кодировки 4 —', chardet.detect(bytes("String", "latin1")), '\n')

#Библиотека Tkinter. Основы разработки оконных приложений
#Первое приложение на Tkinter
import tkinter, tkinter.ttk, tkinter.messagebox
class Application1(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack ()
        self.create_widgets()
        self.master.title("Test")
        self.master.resizable(False, False)
    def create_widgets(self):
        self.btnHello = tkinter.ttk.Button(self,
                                           text = "Приветствовать\nпользователя")
        self.btnHello.bind("<ButtonRelease>" , self.say_hello)
        self.btnHello.pack()
        self.btnShow = tkinter.ttk.Button(self)
        self.btnShow["text"] = "Выход"
        self.btnShow["command"] = root.destroy
        self.btnShow.pack(side="bottom")
    def say_hello(self, evt):
        tkinter.messagebox.showinfo("Test", "Привет, пользователь!")
#root = tkinter.Tk()
#app = Application1(master=root)
#root.mainloop()

#Связывание компонентов с данными. Метапеременные
import tkinter, tkinter.ttk
class Application2(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.title("Использование метапеременных")
        self.master.resizable(False, False)
    def create_widgets(self):
        self.varValue = tkinter.StringVar()
        self.varValue.set("Значение")
        self.entValue = tkinter.ttk.Entry(self,
                                          textvariable=self.varValue)
        self.entValue.pack()
        self.btnShow = tkinter.ttk.Button (self, text="Вывести значение",
                                           command=self.show_value)
        self.btnShow.pack (side="bottom")
    def show_value(self):
        print(self.varValue.get())
#root = tkinter.Tk()
#app = Application2(master=root)
#root.mainloop()

#Обработка событий. Использование диспетчера компоновки Pack
import tkinter, tkinter.ttk
class Application3(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", padx=4, pady=4)
        self.create_widgets()
        self.master.title("Pack")
        self.master.resizable(True, False)
    def create_widgets(self):
        entValue = tkinter.ttk.Entry(self)
        entValue.pack(fill="x", padx=4)
        btnShow = tkinter.ttk.Button(self, 
                                        text = "Вывести значение")
        btnShow.pack(fill="x", padx=4, pady=(0, 10))
        btnExit = tkinter.ttk.Button(self, text="Выход")
        btnExit.pack(side="bottom", anchor="ne")
#root = tkinter.Tk()
#app = Application3(master=root)
#root.mainloop()

#Использование диспетчера компоновки Place
import tkinter, tkinter.ttk
class Application4(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(width=200, height=100)
        self.pack(padx=4, pady=4)
        self.create_widgets()
        self.master.title("Place")
        self.master.resizable(False, False)
    def create_widgets(self):
        entValue = tkinter.ttk.Entry(self)
        entValue.place(x=4, y=4, width=-8, relwidth=1.0, height=22)
        btnShow = tkinter.ttk.Button(self, text="Вывести значение")
        btnShow.place(x=4, y=30, width=-8, relwidth=1.0, height=26)
        btnExit = tkinter.ttk.Button(self, text="Выход")
        btnExit.place(x=-64, relx=1.0, y=-30, rely=1.0, width=60, height=26)
#root = tkinter.Tk()
#app = Application4(master=root)
#root.mainloop()

#Использование диспетчера компоновки Grid
import tkinter, tkinter.ttk
class Application5(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill="both", padx=4, pady=4)
        self.create_widgets()
        self.master.title("Grid")
        self.master.resizable(True, False)
    def create_widgets(self):
        entValue = tkinter.ttk.Entry(self)
        entValue.grid(sticky="w, e")
        btnShow = tkinter.ttk.Button(self, text="Вывести значение")
        btnShow.grid(row=0, column=1, sticky="w, e")
        btnExit = tkinter.ttk.Button(self, text="Выход")
        btnExit.grid(column=1, sticky="e, s")
        self.grid_rowconfigure(1, pad=5)
        self.grid_columnconfigure(0, minsize=100, weight=2, pad=5)
        self.grid_columnconfigure(1, weight=1, pad=5)
#root = tkinter.Tk()
#app = Application5(master=root)
#root.mainloop()

#Применение вложенных контейнеров
import tkinter, tkinter.ttk
class Application6(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(padx=4, pady=4)
        self.create_widgets()
        self.master.title("Вложенные контейнеры")
        self.master.resizable(False, False)
    def create_widgets(self):
        cont1 = tkinter.ttk.Frame(self)
        lblValue = tkinter.ttk.Label(cont1, text="Введите значение")
        lblValue.pack(padx=4, pady=4)
        entValue = tkinter.ttk.Entry(cont1)
        entValue.pack(padx=4, pady=4)
        cont1.pack(side="left")
        cont2 = tkinter.ttk.Frame(self)
        btnOK = tkinter.ttk.Button(self, text="OK")
        btnOK.pack(in_=cont2, padx=4, pady=4)
        btnCancel=tkinter.ttk.Button(self, text = "Отмена")
        btnCancel.pack(in_ = cont2, padx=4, pady = 4)
        cont2.pack(side="right")
#root = tkinter.Tk()
#app = Application6(master=root)
#root.mainloop()

#Управление жизненным циклом приложения
import tkinter, tkinter.ttk, time
class Application7(tkinter.Tk):
    def __init__(self) :
        super() .__init__()
        self.create_widgets ()
        self.title("update_idletasks")
        self.resizable(False, False)
        self .mainloop()
    def create_widgets(self):
        btnAction = tkinter.ttk.Button(self,
                                       text="Запустить действие", width=20, command=self.run)
        btnAction.pack()
        self.lblCounter = tkinter.ttk.Label(self, text="")
        self.lblCounter.pack ()
    def run(self):
        for i in range(0, 51):
            time.sleep(0.1)
            self.lblCounter["text"] = str(i)
            self.update_idletasks()
#app = Application7()

#Библиотека Tkinter. Компоненты и вспомогательные классы. 
#Проверка введенного значения на правильность
import tkinter, tkinter.ttk, re
class Application8(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack ()
        self.create_widgets()
        self.master.title("Correct")
        self.master.resizable(False, False)
    def create_widgets(self) :
        self.pre = re.compile(r"^[1-9]{6}$")
        v = self.register(self.is_valid)
        self.entValue = tkinter.ttk.Entry(self, validatecommand=v,
                                          validate="focusout")
        self.entValue.pack()
        btnOK = tkinter.ttk.Button(self, text="Отправить")
        btnOK.pack()
    def is_valid(self) :
        if self.pre.match(self.entValue.get()):
            return True
        else:
            self.entValue.focus_set()
            return False
#root = tkinter.Tk()
#app = Application8(master=root)
#root.mainloop()

#Обработка «горячих клавиш»
import tkinter, tkinter.ttk
class Application9(tkinter.ttk.Frame):
    def __init__(self, master=None):
        super ().__init__()
        self.pack ()
        self.create_widgets()
        self.master.title("Горячие клавиши")
    def create_widgets(self):
        window = self.master
        mainmenu = tkinter.Menu(window)
        window["menu"] = mainmenu
        self.menu = tkinter.Menu(mainmenu, tearoff=False)
        self.menu.add_command(label="Открыть",accelerator = "Ctrl+O")
        mainmenu.add_cascade(label="Файл", menu=self.menu)
        lbl = tkinter.ttk.Label(self, text="Введите значение", underline=8)
        lbl.pack()
        self.ent = tkinter.ttk.Entry(self)
        self.ent.pack()
        self.btn = tkinter.ttk.Button(self, text="Выполнить", underline=0)
        self.btn.pack()
        self.chk = tkinter.ttk.Checkbutton(self, text="Установить", underline=0)
        self.chk.pack()
        self.bind_all("<Alt-KeyPress-p>",
                      lambda evt: self.ent.focus_set())
        self.bind_all("<Alt-KeyPress-d>", 
                      lambda evt: self.btn.invoke())
        self.bind_all("<Alt-KeyPress-e>", 
                      lambda evt: self.chk.invoke())
        self.bind_all("<Control-KeyPress-o>", 
                      lambda evt: self.menu.invoke(0))
#root = tkinter.Tk()
#app = Application9(master=root)
#root.mainloop()

#Параллельное программирование
import concurrent.futures as cf
with cf.ThreadPoolExecutor() as tpe:
    f1 = tpe.submit(pow, 123, 456)
    f2 = tpe.submit(pow, 789, 123)
    f3 = tpe.submit(pow, 456, 789)
    f4 = tpe.submit(pow, 789, 987)
print(f1.result())
print(f2.result())
print(f3.result())
print(f4.result(), '\n')

#Использование планировщика заданий
import sched, time
def print_time(thread_num):
    t = time.strftime("%H:%M:%S", time.localtime(time.time()))
    print("Задание {0}: {1}".format(thread_num, t))
sch = sched.scheduler()
sch.enterabs(time.monotonic() + 10, 1, print_time, argument= (1,))
sch.enter(3, 1, print_time, argument=(2,))
sch.enter(3, 2, print_time, argument=(3,))
sch.run()
print()

#Работа с архивами
#Сохранение в архивном файле GZJP произвольных данных
import gzip
archive1 = "ArсhiveGZIP.gz"
soder1 = "Этот файл содержится в архиве"
newarch1 = gzip.open(archive1, mode="wt", encoding="utf-8")
newarch1.write(soder1)    #Запись в файл
newarch1.close()
newarch1 = gzip.open(archive1, mode="rt", encoding="utf-8")
print(newarch1.read())   #Чтение файла
newarch1.close()

#Сжатие и распаковка по алгоритму BZIP2
import bz2
archive2 = "ArсhiveBZ2.bz2"
soder2 = "Этот другой файл содержится в новом архиве"
newarch2 = bz2.open(archive1, mode="wt", encoding="utf-8")
newarch2.write(soder2)    #Запись в файл
newarch2.close()
newarch2 = bz2.open(archive1, mode="rt", encoding="utf-8")
print(newarch2.read())   #Чтение файла
newarch2.close()

#Сохранение строки в архиве LZMA
import lzma
archive3 = "ArсhiveLZMA.xz"
soder3 = "Этот еще один другой файл содержится в еще одном новом архиве"
newarch3 = lzma.open(archive3, mode="wt", encoding="utf-8")
newarch3.write(soder3)    #Запись в файл
newarch3.close()
newarch3 = lzma.LZMAFile(filename=archive3)
print(str(newarch3.read(), encoding="utf-8"))   #Чтение файла 
newarch3.close()
