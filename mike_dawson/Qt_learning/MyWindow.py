from PyQt4 import QtCore, QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Hello World!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnQuit = QtGui.QPushButton("&Close window")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        self.connect(self.btnQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())