# http://stackoverflow.com/questions/16036336/how-to-change-minimize-event-behavior-in-pyqt-or-pyside
# http://stackoverflow.com/questions/4044994/hide-pyqt-app-from-taskbar

from PyQt4 import QtGui, QtCore

class MyWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.systemTrayIcon = QtGui.QSystemTrayIcon(self)
        self.systemTrayIcon.setIcon(QtGui.QIcon.fromTheme("face-smile"))
        self.systemTrayIcon.setVisible(True)
        self.systemTrayIcon.activated.connect(self.on_systemTrayIcon_activated)

        self.label = QtGui.QLabel(self)
        self.label.setText("Minimize me!")

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.label)

    @QtCore.pyqtSlot(QtGui.QSystemTrayIcon.ActivationReason)
    def on_systemTrayIcon_activated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()

            else:
                self.hide()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                event.ignore()
                #self.close()
                QtCore.QTimer.singleShot(0, self.close)
                return

        super(MyWindow, self).changeEvent(event)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        #self.systemTrayIcon.showMessage('Running', 'Running in the background.')

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())