from PyQt4 import QtCore, QtGui, uic
import sys

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("MyForm.ui")
QtCore.QObject.connect(window.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
window.show()
sys.exit(app.exec_())