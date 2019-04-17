'''
Created on Apr 4, 2019

@author: aapolinjama
'''
class Square:
    
    
    def __init__(self, is_obs = False):
        
        self.player = None
        self.is_obstacle = is_obs
        
    def is_obstacle(self):
        return self.is_obstacle
    
    def is_empty(self):
        return not self.is_obstacle()