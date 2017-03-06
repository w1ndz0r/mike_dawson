import pythoncom, pyHook, time, ctypes, sys, win32api, win32con
from tkinter import *
from threading import Thread

# отслеживает нажатия клавиш
#
def OnKeyboardEvent(event):
    # 0 или 1 - клавиша отжата
    # (-127) или (-128) - клавиша нажата#
    f12 = win32api.GetKeyState(0x7B)
    shift_key = win32api.GetKeyState(0x10)
    if event.Key == 'F12' and event.MessageName == 'key down':
        if shift_key < 0:
            print("Нажато Shift+F12")
            # тут должна быть функция загружающая картинку
    return True


class Application(Frame):
    """GUI приложение"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        """Создаёт кнопку"""
        # первая кнопка
        self.bttn1 = Button(self, text= "Я ничего не делаю!")
        self.bttn1.grid()

# Запуск создания окна - должен быть в конце
root = Tk()
root.title("Бесполезные кнопки - 2")
root.geometry("200x85")
app = Application(root)

def startPyhookThread():
    def run():
        hm = pyHook.HookManager()  # создание экземпляра класса HookManager
        hm.KeyAll = OnKeyboardEvent  # отслеживаем нажатия клавиш
        hm.HookKeyboard()
        pythoncom.PumpMessages()

pyhookThread = Thread(target=startPyhookThread)
pyhookThread.start()


root.mainloop()


