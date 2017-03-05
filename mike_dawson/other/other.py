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

hm = pyHook.HookManager()       # создание экземпляра класса HookManager
hm.KeyAll = OnKeyboardEvent     # отслеживаем нажатия клавиш
hm.HookKeyboard()               # вешаем хук

# класс Application для создания окна
# запуск окна возможен через
# root = Tk()
# root.title("Заголовок")
# root.geometry("200x85")
# app = Application(root)
# root.mainloop()
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


# запуск рут треда
def startRootThread():
    root.mainloop()
    # пеерзапуск треда каждые 100 мс ("перерисовка окна")
    root.after(100, root.quit())
    root.mainLoop()



def upload():
    None
    # тут должна быть функция загрузки изображения привязанная к OnKeyboardEvent

def killProgram():
    ctypes.windll.user32.PostQuitMessage(0) # stops pumpMessages
    #
    root.destroy() #stops the root widget
    rootThread.join()
    print('rootThread stopped')


rootThread = Thread(target=startRootThread)
rootThread.start()

# запуск окна постоянно отслеживающего события
pythoncom.PumpMessages()



def startTimerThread():
    while True:
        win32api.PostThreadMessage(mainThreadId, win32con.WM_QUIT, 0, 0)
        time.sleep(1)

# ХЗ. Забирает ID трела
mainThreadId = win32api.GetCurrentThreadId()
# стартует таймер тред (чтоблядь)
timerThread = Thread(target=startTimerThread)
timerThread.start()

while programRunning:
    root.after(100,root.quit)
    root.mainloop()
    pythoncom.PumpMessages()


print('PumpMessages stopped')