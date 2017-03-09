from PyQt4 import QtCore, QtGui
import sys, time

def on_clicked():
    button.setDisabled(True)
    for i in range(1, 21):
        QtGui.qApp.processEvents()
        time.sleep(1) # "Засьmаем" на 10 секунд
        print("step -", i)
    button.setDisabled(False)

арр = QtGui.QApplication(sys.argv)
button = QtGui.QPushButton("Зaпycтить процесс")
button.resize(200, 40)

QtCore.QObject.connect(button, QtCore.SIGNAL("clicked()"), on_clicked)
button.show()
sys.exit(арр.exec_())