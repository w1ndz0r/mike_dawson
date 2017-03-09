from PyQt4 import QtCore, QtGui


class MyТhread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.emit(QtCore.SIGNAL("mysignal(QString)"), "count = %s" % self.count)
            self.sleep(1)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Haжмитe кнопку дnя запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.btnStart = QtGui.QPushButton("Зaпycтить поток")
        self.btnStop = QtGui.QPushButton("Ocтaнoвить поток")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.setLayout(self.vbox)
        self.mythread = MyТhread()
        self.connect(self.btnStart, QtCore.SIGNAL("clicked()"), self.on_start)
        self.connect(self.btnStop, QtCore.SIGNAL("clicked()"), self.on_stop)
        self.connect(self.mythread, QtCore.SIGNAL("mysignal(QString)"), self.on_change, QtCore.Qt.QueuedConnection)

    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start()

    def on_stop(self):
        self.mythread.running = False

    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        self.hide() # сворачивает окно
        self.mythread.running = False
        self.mythread.wait(5000)
        event.accept()


if __name__ == "__main__":
    import sys
    арр = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Запуск и остановка потока")
    window.resize(300, 100)
    window.show()
    sys.exit(арр.exec_())