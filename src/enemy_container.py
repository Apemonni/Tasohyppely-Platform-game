'''
Created on Apr 20, 2019

@author: aapolinjama
'''
from enemy import Enemy

class Enemy_container():
    def __init__(self):
        self.enemies = []
        
    def add_enemy(self,enemy):
        self.enemies.append(enemy)
    
    def get_enemies(self):
        return self.enemies
