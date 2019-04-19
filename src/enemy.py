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
        self.setPixmap(QPixmap("enemy-1.png"))
        self.up_down_counter = 200
    
    def enemy_update(self):
        
        dy = 0
        dx = 0
        if self.up_down_counter > 100:
            dy += 1
            self.up_down_counter -= 1
            
        if self.up_down_counter <= 100:
            dy -= 1
            self.up_down_counter -= 1
            if self.up_down_counter == 0:
                self.up_down_counter = 200
            
        
        self.setPos(self.x(), self.y() + dy)
