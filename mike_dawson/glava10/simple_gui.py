# простейший GUI
# Демонстрирует создание окна
from tkinter import *

# создание базового окна
root = Tk()
root.title("Простейший GUI")
root.geometry("200x100")

app = Frame(root)
app.grid()

bttn1 = Button(app, text = "Я не делаю ничего")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "И я тоже")

bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И я!"

# старт событийного цикла
root.mainloop()

