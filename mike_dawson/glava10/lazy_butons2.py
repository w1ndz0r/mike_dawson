# Бесполезные кнопки 2
# Демонстриует создание класса в оконном приложении на основе tkinter
from tkinter import *

class Application(Frame):
    """GUI приложение с 3мя кнопками"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Создает 3три бесполезные кнопки"""
        # первая кнопка
        self.bttn1 = Button(self, text= "Я ничего не делаю!")
        self.bttn1.grid()
        # втоаря кнопка
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "И я тоже")
        # третья кнопка
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "И я!"

# основная часть
root = Tk()
root.title("Бесполезные кнопки - 2")
root.geometry("200x85")

app = Application(root)

root.mainloop()