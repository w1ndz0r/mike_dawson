from PyQt4 import QtCore, QtGui
import MyWindow

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.myWidget = MyWindow.MyWindow()
        self.myWidget.vbox.setMargin(0)
        self.button = QtGui.QPushButton("&Изменить надпись")
        mainBox = QtGui.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.connect(self.button, QtCore.SIGNAL("clicked()"), self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("Новая надпись")
        self.button.setDisabled(True)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Преимущества ООП-стиля")
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())