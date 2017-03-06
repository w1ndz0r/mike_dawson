import pythoncom, pyHook, time, ctypes, sys, win32api, win32con
from PyQt4 import QtCore, QtGui


class WorkerThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        print("hello")

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(250, 150)
widget.setWindowTitle('simple')
widget.show()

sys.exit(app.exec_())

