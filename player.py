'''
Created on Mar 19, 2019

@author: aapolinjama
'''

import sys
from PyQt5.QtCore import (
    Qt,
)
from PyQt5.QtGui import (
    QPixmap
)
from PyQt5.QtWidgets import (
    QGraphicsPixmapItem,
)

class Player(QGraphicsPixmapItem):
    def __init__(self, parent = None):
        QGraphicsPixmapItem.__init__(self,parent)
        self.setPixmap(QPixmap("frame-111.png"))
    
    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
        if Qt.Key_A in keys_pressed:
            dx -= 3
        if Qt.Key_D in keys_pressed:
            dx += 3
        if Qt.Key_W in keys_pressed:
            dy -= 3
        if Qt.Key_S in keys_pressed:
            dy += 3
        self.setPos(self.x()+dx, self.y()+dy)