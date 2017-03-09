from PyQt4 import QtCore, QtGui, uic
import sys

app = QtGui.QApplication(sys.argv)
window = uic.loadUi("MyForm.ui")
QtCore.QObject.connect(window.btnQuit, QtCore)
