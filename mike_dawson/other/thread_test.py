import win32api
import win32con
import pythoncom
from threading import Timer

main_thread_id = win32api.GetCurrentThreadId()

def on_timer():
    win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0);

t = Timer(5.0, on_timer) # Quit after 5 seconds
t.start()

pythoncom.PumpMessages()