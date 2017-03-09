from PyQt4 import QtCore, QtGui


class Thread1(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.count = 0

    def run(self):
        self.exec_()

    def on_start(self):
        self.count += 1
        self.emit(QtCore.SIGNAL("s1(int)"), self.count)


class Thread2(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        self.exec_()

    def on_change(self, i):
        i += 10
        self.emit(QtCore.SIGNAL("s2(const QString&)"), "%d" % i)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Нажмите кноnку")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtGui.QPushButton("Сгенерировать сигнал")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.thread1 = Thread1()
        self.thread2 = Thread2()
        self.thread1.start()
        self.thread2.start()
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.thread1.on_start)
        self.connect(self.thread1, QtCore.SIGNAL("s1(int)"), self.thread2.on_change)
        self.connect(self.thread2, QtCore.SIGNAL("s2(const QString&)"),
                     self.label, QtCore.SLOT("setText(const QString&)"))

if __name__ == "__main__":
    import sys
    арр = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Обмен сигналами между nотоками")
    window.resize(300, 70)
    window.show ()
    sys.exit(арр.exec_())