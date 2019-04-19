'''
Created on Apr 19, 2019

@author: aapolinjama
'''
from PyQt5.QtCore import (
    Qt,
)
from PyQt5.QtGui import (
    QPixmap
)
from PyQt5.QtWidgets import (
    QGraphicsPixmapItem,
)

class Enemy(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("frame-111.png"))
