# 1.)
try:
    from PySide import QtGui, QtCore
except:
    from PyQt4 import QtGui, QtCore
    QtCore.Signal = QtCore.pyqtSignal
    QtCore.Slot = QtCore.pyqtSlot

# 2.)
print QtGui
    
class PySidePyQtExample(QtGui.QPushButton):
    # 3.)
    mySignal = QtCore.Signal(str)
    def __init__(self, parent = None):
        super(PySidePyQtExample, self).__init__(parent)
        self.resize(240, 60)
        self.clicked.connect(self.emitMySignal)
        self.mySignal.connect(self.setText)
        
    def emitMySignal(self):
        self.mySignal.emit('I just emitted mySignal')
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = PySidePyQtExample()
    w.show()
    w.raise_()
    sys.exit(app.exec_())
        