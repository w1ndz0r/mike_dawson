from PyQt4 import QtGui, QtCore
import inspect
for name in dir(QtGui):
    obj = getattr(QtGui, name)
    if inspect.isclass(obj) and issubclass(obj, QtCore.QObject):
        for name2 in dir(obj):
            obj2 = getattr(obj, name2)
            if isinstance(obj2, QtCore.pyqtSignal):
                print(name, name2)
