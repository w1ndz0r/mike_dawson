import win32api, win32con, pythoncom, pyHook, os
from threading import Timer

###
#def OnKeyboardEventAll(event):
#    print('MessageName:',event.MessageName)
#    print('Message:',event.Message)
#    print('Time:',event.Time)
#    print('Window:',event.Window)
#    print('WindowName:',event.WindowName)
#    print('Ascii:', event.Ascii, chr(event.Ascii))
#    print('Key:', event.Key)
#    print('KeyID:', event.KeyID)
#    print('ScanCode:', event.ScanCode)
#    print('Extended:', event.Extended)
#    print('Injected:', event.Injected)
#    print('Alt', event.Alt)
#    print('Transition', event.Transition)
#    print('---')
#

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
            os.startfile("https:\\ya.ru")
    return True

main_thread_id = win32api.GetCurrentThreadId()

def exit_on_timer():
    win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0)
    print("Выходим из треда:", main_thread_id)
    second_thread_id = win32api.GetCurrentThreadId()
    print("Второй тред: ", second_thread_id)

#t = Timer(5.0, exit_on_timer) # Quit after 5 seconds
#t.start()

hm = pyHook.HookManager()       # создание экземпляра класса HookManager
hm.KeyAll = OnKeyboardEvent     # отслеживаем нажатия клавиш
hm.HookKeyboard()               # вешаем хук
pythoncom.PumpMessages()        # ловим сообщения