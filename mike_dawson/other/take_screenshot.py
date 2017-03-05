import sys
from PyQt4.QtGui import *
from datetime import datetime

# take screenshot of desktop
#date = datetime.now()
#filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
#app = QApplication(sys.argv)
#QPixmap.grabWindow(QApplication.desktop().winId()).save(filename, 'jpg')

app = QApplication(sys.argv)
widget = QWidget()
# set up the QWidget...
widget.setLayout(QVBoxLayout())

label = QLabel()
widget.layout().addWidget(label)

def shoot():
    date = datetime.now()
    filename = date.strftime('%Y-%m-%d_%H-%M-%S.jpg')
    p = QPixmap.grabWindow(widget.winId())
    p.save(filename, 'jpg')
    label.setPixmap(p)        # just for fun :)
    print("shot taken")

widget.layout().addWidget(QPushButton('take screenshot', clicked=shoot))

widget.show()
app.exec_()