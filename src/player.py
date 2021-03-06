'''
Created on Mar 19, 2019

@author: aapolinjama
'''
import sys
from map import Map
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
        self.jumping = 0
        self.can_jump = True
        self.won = False
        self.loss = False 
        self.map = Map()
        self.won_count = 50
        self.draw_won = 100
        self.loss_count = 2
        self.draw_loss = 100
        
    
    def game_update(self, keys_pressed):
        dx = 0
        dy = 0
     
        #self.collision_detection()
        self.check_if_won()
        if self.won:
            self.won_count -= 1
            self.draw_won -= 1
            if self.won_count == 1:
                self.won = False
                self.setPos(53,700)
                self.won_count = 50
        
        
        if self.loss:
            self.loss_count -= 1
            self.draw_loss -= 1
            if self.loss_count == 1:
                self.loss = False
                self.setPos(53,700)
                self.loss_count = 2
                

        if Qt.Key_A in keys_pressed and self.can_moveleft() and self.check_left_boundary():
            dx -= 3
                    
        if Qt.Key_D in keys_pressed and self.check_right_boundary():
            if self.can_moveright():
                dx += 3
            
        if Qt.Key_W in keys_pressed and self.check_up_boundary() and self.check_right_boundary() and self.check_left_boundary():
            if self.jump() and self.can_jump:
                self.jumping = 90
                self.can_jump = False
                dy -= 25
            
        if self.fall():
            dy += 3
            
        if not self.fall() and self.jumping > 0:
            dy -= 3
            

            
        
        self.setPos(self.x() + dx, self.y() + dy)
        
    def get_won_count(self):
        return self.won_count    
    
    def get_draw_won(self):
        return self.draw_won
    
    def get_draw_loss(self):
        return self.draw_loss
    
    def add_draw_loss(self):
        
        self.draw_loss = 30
    
    def add_draw_won(self):
        
        self.draw_won = 100
            
    def can_moveright(self):
        map = self.map.get_map()
        player_loc_right = (self.x()+40)//50
        player_loc_down = (self.y()+32)//50
        loc_y = self.y()//50
        if int(player_loc_down) != int(loc_y) and int(loc_y) < int(player_loc_down):
            loc_y += 1
            if map[int(loc_y)-1][int(player_loc_right)].is_obstacle:
                loc_y -= 1
                
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
        if not map[int(loc_y)][int(player_loc_left)].is_obstacle:
            return True
        else:
            return False
        
    def fall(self):
        map = self.map.get_map()
        player_loc_left = (self.x()-3)//50
        player_loc_right = (self.x()+40)//50
        loc_y = (self.y()-15)//50
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
            return True
        else:
            return False
            
    def has_won(self):
        return self.won
            
            
    def check_if_won(self):
        map = self.map.get_map()
        if int(self.x()//50) == 1 and int(self.y()//50) == 2:
            self.won = True
        else:
            self.won = False
            
    def check_left_boundary(self):
        
        player_loc_left = (self.x()-3)//50
        if not int(player_loc_left) < 0:
            return True 
        
        
            
    def check_right_boundary(self):
        
        player_loc_right = (self.x()+40)//50
        if not int(player_loc_right) > self.map.get_width() -1:
            return True 
                
    def check_up_boundary(self):

        player_loc_up = (self.y()-3)//50
        if not int(player_loc_up) < 0:
            return True
        
    
    def check_if_coll_enemy(self, enemy_container):
        for i in enemy_container:
            if self.collidesWithItem(i):
                self.loss = True
                return
        
        self.loss=False
        
    def has_lost(self):
        return self.loss
        
        
        
        

        
        
                        
                
        
  