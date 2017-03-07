import win32api, pythoncom, pyHook, requests, base64, sys, threading
from datetime import datetime
from PyQt4.QtGui import QPixmap, QApplication

date = datetime.now()
filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')

CLIENT_KEY = "pQP0y1XUyfBcNzQ7Or8G"
SECRET_KEY = "5rt7rEV2PZn1QkoO2QiYlOpFmhJ2uX5qfpn"
API_URL = 'https://api.imageban.ru/v1'
HEADER = {'Authorization: TOKEN': CLIENT_KEY}


def send_screenshot():
    app = QApplication(sys.argv)
    QPixmap.grabWindow(QApplication.desktop().winId()).save('screenshot.jpg', 'jpg')
    with open("screenshot.jpg", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
    data = {'secret_key': SECRET_KEY, 'image': encoded_image}
    r = requests.post(API_URL, headers=HEADER, data=data)
    print("Отправлено")
    return True


def OnKeyboardEvent(event):
    # 0 или 1 - клавиша отжата
    # (-127) или (-128) - клавиша нажата#
    f12 = win32api.GetKeyState(0x7B)
    shift_key = win32api.GetKeyState(0x10)
    if event.Key == 'F12' and event.MessageName == 'key down':
        if shift_key < 0:
            print("Нажато Shift+F12")
        else:
            print("Нажато F12")
            t1 = threading.Thread(target=send_screenshot())
            print(threading.activeCount())
    return True

hm = pyHook.HookManager()       # создание экземпляра класса HookManager
hm.KeyAll = OnKeyboardEvent     # отслеживаем нажатия клавиш
hm.HookKeyboard()               # вешаем хук
pythoncom.PumpMessages()        # ловим сообщения


