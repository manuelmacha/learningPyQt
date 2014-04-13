from PyQt4 import QtGui

# 1.)
class MyWindow(QtGui.QWidget):
    def __init__(self, parent = None):
        super(MyWindow, self).__init__(parent)
     
        # 2.)   
        lineEdit = QtGui.QLineEdit('Enter Text', self)
        self.label = QtGui.QLabel('Nothing typed yet', self)
        button = QtGui.QPushButton('Clear', self)
        
        # 3.)
        self.setWindowTitle('Signals & Slots')
        self.setFixedSize(320, 120)
        
        # 4.)
        self.setLayout(QtGui.QVBoxLayout())
        
        # 5.)
        for widget in [lineEdit, self.label, button]:
            self.layout().addWidget(widget)
        
        # 6.)
        button.clicked.connect(lineEdit.clear)
        lineEdit.textChanged.connect(self.displayResult)
            
    # 7.)        
    def displayResult(self, text):
        self.label.setText('You just typed "%s"' % text)
            
# 8.)        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
        