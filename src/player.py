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
        self.jumping = 0
        self.can_jump = True
        self.won = False
        self.dead = False 
        self.map = Map()
        self.won_count = 100
        
    
    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
     
        #self.collision_detection()
        self.check_if_won()
        if self.won:
            self.won_count -= 1
            if self.won_count <= 1:
                self.won = False
                self.setPos((100-self.pixmap().width())/2,
                           (1000-self.pixmap().height())/2)
        
        if Qt.Key_A in keys_pressed and self.can_moveleft():
            dx -= 3
                    
        if Qt.Key_D in keys_pressed and self.can_moveright():
            dx += 3
            
        if Qt.Key_W in keys_pressed and self.jump() and self.can_jump:
            self.jumping = 90
            self.can_jump = False
            dy -= 25
            
        """if Qt.Key_S in keys_pressed:
            dy += 3"""
        if self.fall():
            dy += 3
            
        if not self.fall() and self.jumping > 0:
            dy -= 3
            
            
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
        
    def fall(self):
        map = self.map.get_map()
        player_loc_left = (self.x()-3)//50
        player_loc_right = (self.x()+40)//50
        loc_y = self.y()//50
        if self.jumping == 0:
            if not map[int(loc_y+1)][int(player_loc_left)].is_obstacle and not map[int(loc_y+1)][int(player_loc_right)].is_obstacle:
                return True
            else:
                self.can_jump = True
                return False
        else:
            if self.jump():
                self.jumping -= 1
                return False
            else:
                self.jumping = 0
                return True
            
    
    def jump(self):
        map = self.map.get_map()
        player_loc_up = (self.y()-3)//50
        player_xloc = self.x()//50
        player_loc_left = (self.x()-3)//50
        player_loc_right = (self.x()+40)//50
        
        if not map[int(player_loc_up)][int(player_loc_left)].is_obstacle and not map[int(player_loc_up)][int(player_loc_right)].is_obstacle:
            self.can_jumping = True
            return True
        else:
            return False
            
    def has_won(self):
        return self.won
            
            
    def check_if_won(self):
        map = self.map.get_map()
        if int(self.x()//50) == 0 and int(self.y()//50) == 1:
            self.won = True
            
            
            
        
        
        

        
        
                        
                
        
  