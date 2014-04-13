
# 1.)
from PyQt4 import QtGui
import sys

# 2.)
app = QtGui.QApplication(sys.argv)

# 3.)
widget = QtGui.QWidget()
widget.setWindowTitle('Hello World')
widget.setMaximumSize(240, 60)

# 4.)
widget.show()
widget.raise_()

# 5.)
sys.exit(app.exec_())