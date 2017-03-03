# считает клики
from tkinter import *

class Application(Frame):
    """GUI приложение считает клики"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()
    def create_widgets(self):
        """Создает кнопку на которой отобраджается количеств совершенных нажатий"""
        self.bttn = Button(self)
        self.bttn["text"] = "Количество щелчков: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        """Увеличивает количество нажатий на единицу и отображает его"""
        self.bttn_clicks += 1
        self.bttn["text"] = "Количество щелчков: " + str(self.bttn_clicks)


# основная часть
root = Tk()
root.title("Количество щелчков")
root.geometry("200x50")
app = Application(root)
root.mainloop()