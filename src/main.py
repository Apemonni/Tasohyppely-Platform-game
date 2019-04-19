'''
Created on Mar 17, 2019

@author: aapolinjama
'''
from gui import GUI
import sys
from PyQt5.QtWidgets import (
    QApplication
    )
                  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
                