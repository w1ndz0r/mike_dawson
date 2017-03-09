# https://habrahabr.ru/post/31690/
import sys
from PyQt4 import QtGui, QtCore


class Escape(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('escape')
        self.resize(250, 150)
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'), QtCore.SLOT('close()'))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()


app = QtGui.QApplication(sys.argv)
qb = Escape()
qb.show()
sys.exit(app.exec_())
