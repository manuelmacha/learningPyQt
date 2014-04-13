from PyQt4 import QtGui, QtCore

class Communicate(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPointF)

class TwoDSlider(QtGui.QWidget):
    
    positionChanged = QtCore.pyqtSignal(QtCore.QPointF)
    
    def __init__(self, parent = None):
        super(TwoDSlider, self).__init__(parent)
        
        self.valX = 0.0
        self.valY = 0.0
        
        self.nValX = 0.0
        self.nValY = 0.0
        
        self.radiusDot = 5.0
        
        QtGui.QResizeEvent()
        
    def mouseMoveEvent(self, event):
        self.valX = self.size().width() * 0.5 - event.pos().x()
        self.valY = self.size().height() * 0.5 - event.pos().y()
        
        self.nValX = self.valX / (self.width() * 0.5) * -1
        self.nValY = self.valY / (self.height() * 0.5)        
        
        self.repaint()
        
        self.positionChanged.emit(QtCore.QPointF(self.nValX, self.nValY))
        
    def paintEvent(self, event):
        
        size = self.size()
        painter = QtGui.QPainter()
        painter.begin(self)
        
        painter.setPen(QtCore.Qt.darkGray)
        painter.setBrush(QtCore.Qt.lightGray)
        
        painter.drawRect(0, 0, size.width(), size.height())
        
        dottedPen = QtGui.QPen(QtCore.Qt.DashLine)
        dottedPen.setColor(QtCore.Qt.black)
        painter.setPen(dottedPen)
        
        painter.drawLine(0.0, size.height() * 0.5, size.width(), size.height() * 0.5)
        painter.drawLine(size.width() * 0.5, 0.0, size.width() * 0.5, size.height())
        
        painter.setPen(QtCore.Qt.black)
        painter.setBrush(QtCore.Qt.darkGray)
        
        posX = self.width() * 0.5 - self.valX
        posY = self.height() * 0.5 - self.valY
        
        painter.setRenderHint(painter.Antialiasing)
        
        painter.drawEllipse(posX - self.radiusDot, posY - self.radiusDot, self.radiusDot * 2.0, self.radiusDot * 2.0)
        painter.drawText(QtCore.QPointF(5.0, size.height() - 5.0), QtCore.QString('x: %s y: %s' % (self.nValX, self.nValY)))        
        
        painter.end()
        
        
def __printposN(pos):
    print pos

def main():
    import sys        
    app = QtGui.QApplication(sys.argv)
    twods = TwoDSlider()
    twods.positionChanged.connect(__printposN)
    twods.show()
    twods.raise_()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()
            


