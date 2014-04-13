# 1.)
from PyQt4 import uic

# 2.)
mybase, myform = uic.loadUiType('/Users/manuel/Desktop/HelloWorld.ui')

# 3.)
class MyUI(mybase, myform):
    def __init__(self, parent = None):
        super(MyUI, self).__init__(parent)
        
        # 4.)
        self.setupUi(self)

# 5.)            
myUI = MyUI()
myUI.show()