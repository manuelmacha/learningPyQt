# 1.)
from PyQt4 import QtGui, QtCore

# 2.)
class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)
        
        self.setWindowTitle('MyMainWindow')
        # 3.)
        self.icon = QtGui.QIcon('myIcon.png')
        # 4.)
        self.initToolBar()
        self.initDockWidget()
        self.initCentralWidget()
        
    # 5.)
    def initToolBar(self):
        toolBar = QtGui.QToolBar('MyToolbar')
        toolBar.setFloatable(True)
        self.addToolBar(QtCore.Qt.TopToolBarArea, toolBar)
        # 6.)
        quitCmd = QtCore.QCoreApplication.instance().quit
        action = toolBar.addAction(self.icon, 'Quit', quitCmd)
        action.setToolTip('Click to quit app')

    # 7.)
    def initDockWidget(self):
        dockWidget = QtGui.QDockWidget('MyDockWidget', self)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockWidget)
        widget = QtGui.QWidget(dockWidget)
        dockWidget.setWidget(widget)
        widget.setLayout(QtGui.QVBoxLayout(widget))
        widget.layout().addWidget(QtGui.QCheckBox('MyCheckBox', widget))
        widget.layout().addWidget(QtGui.QSlider(QtCore.Qt.Horizontal, widget))
        widget.layout().addWidget(QtGui.QTextEdit('MyTextEdit', widget))
        comboBox = QtGui.QComboBox(widget)
        for char in ['C', 'B', 'A']:
            comboBox.insertItem(0, 'Option %s' % char)
        widget.layout().addWidget(comboBox)
        widget.layout().addWidget(QtGui.QCalendarWidget(widget))
    
    # 8.)    
    def initCentralWidget(self):
        widget = QtGui.QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(QtGui.QVBoxLayout())
        tableWidget = QtGui.QTableWidget(widget)
        widget.layout().addWidget(tableWidget)
        tableWidget.setColumnCount(2)
        colors = QtGui.QColor.colorNames()
        tableWidget.setRowCount(colors.count())
        for i in range(colors.count()):
            item = QtGui.QTableWidgetItem(colors[i])
            item.setToolTip(colors[i])
            color = QtGui.QColor(colors[i])
            item.setForeground(QtGui.QBrush(color))
            item.setBackgroundColor(QtGui.QColor(color.darker()))
            tableWidget.setItem(i, 0, item)
            rgb = color.toRgb()
            tableWidget.setItem(i, 1, QtGui.QTableWidgetItem('%d, %d, %d' % (rgb.red(), rgb.green(), rgb.blue())))
        tableWidget.setHorizontalHeaderLabels(['Name', 'RGB'])

            
# 9.)        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
        