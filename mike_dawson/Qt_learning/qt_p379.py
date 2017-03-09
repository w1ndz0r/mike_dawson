from PyQt4 import QtCore, QtGui


class MyThread(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        for i in range(1, 21):
            self.sleep(3)
            self.emit(QtCore.SIGNAL("mysignal(QString)"), "i = %s" % i)


class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.label = QtGui.QLabel("Haжмитe кнопку дпя запуска потока")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtGui.QPushButton("Зaпycтить процесс")
        self.vbox = QtGui.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()  # Создаем экземпляр класса
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.on_clicked)
        self.connect(self.mythread, QtCore.SIGNAL("started()"), self.on_started)
        self.connect(self.mythread, QtCore.SIGNAL("finished()"), self.on_finished)
        self.connect(self.mythread, QtCore.SIGNAL("mysignal(QString)"), self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.button.setDisabled(True)  # Делаем кнопкунеактивной
        self.mythread.start()  # Запускаем поток

    def on_started(self):  # Вьвывается при запуске потока
        self.label.setText("Bызвaн метод on_started()")

    def on_finished(self):  # Вызывается при завершении потока
        self.label.setText("Bызвaн метод on_finished()")
        self.button.setDisabled(False)  # Делаем кнопку активной

    def on_change(self, s):
        self.label.setText(s)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Using of QThread")
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())