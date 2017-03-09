from PyQt4 import QtCore, QtGui
import sys, time

def on_clicked():
    time.sleep(10) # "Засьmаем" на 10 секунд

арр = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Зaпycтить процесс")
button.resize(200, 40)

QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), on_clicked)
button.show()
sys.exit(арр.exec_())