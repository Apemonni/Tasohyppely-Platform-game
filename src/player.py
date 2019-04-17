'''
Created on Mar 19, 2019

@author: aapolinjama
'''
import sys
from map import Map
from square_graphics import SquareGraphs
from coordinates import Coordinates
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
        self.collides = False
        self.moveright = True
        self.moveleft = True
        self.moveUp = True
        self.moveDown = True
        self.location = Coordinates(self.x(), self.y()) 
        self.jumping = False
        self.map = Map()
        
    
    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
     
        #self.collision_detection()
        if Qt.Key_A in keys_pressed and self.can_moveleft():
            dx -= 3
                    
        if Qt.Key_D in keys_pressed and self.can_moveright():
            dx += 3
            
        if Qt.Key_W in keys_pressed:
            dy -= 3
            
        if Qt.Key_S in keys_pressed:
            dy += 3
            
        print(self.y())
        print(self.x())
        self.location = Coordinates(self.x()+dx, self.y()+dy)
        self.setPos(self.location.get_x(), self.location.get_y())
        
        
        
            
    def can_moveright(self):
        map = self.map.get_map()
        player_loc_right = (self.x()+40)//50
        player_loc_down = (self.y()+32)//50
        loc_y = self.y()//50
        if int(player_loc_down) != int(loc_y) and int(loc_y) < int(player_loc_down):
            loc_y += 1
            if map[int(loc_y)-1][int(player_loc_right)].is_obstacle:
                loc_y -= 1
            
        print(player_loc_right)
        if not map[int(loc_y)][int(player_loc_right)].is_obstacle:
            return True
        else:
            return False
    
    def can_moveleft(self):
        map = self.map.get_map()
        player_loc_left = (self.x()-3)//50
        player_loc_down = (self.y()+32)//50
        loc_y = self.y()//50
        if int(player_loc_down) != int(loc_y) and int(loc_y) < int(player_loc_down):
            loc_y += 1
            if map[int(loc_y)-1][int(player_loc_left)].is_obstacle:
                loc_y -= 1
        #player_loc_up = (self.y())
        print(player_loc_left)
        if not map[int(loc_y)][int(player_loc_left)].is_obstacle:
            return True
        else:
            return False

        
        
                        
                
        
  