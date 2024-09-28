import tkinter, tkinter.ttk, tkinter.messagebox
class Application(tkinter.ttk.Frame):
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
root = tkinter.Tk()
app = Application(master=root)
root.mainloop()