'''
Created on Apr 4, 2019

@author: aapolinjama
'''

from square import Square

class Map:
    
    def __init__(self):
        
        file = open("kentta1.txt", "r")
        self.squares = [[int(n) for n in line.split()] for line in file] 
        self.map = len(self.squares) * [None]
        a = 0
        b = 0
        for i in self.squares:
            self.map[a] = len(self.squares[1]) * [None]
            for j in i:
                if j == 0:
                    self.map[a][b] = Square()
                    b += 1
                else:
                    self.map[a][b] = Square(True)
                    b += 1
            a += 1
            b = 0  
                
    
    def get_squares(self):
        return self.squares
    
    
    def get_map(self):
        return self.map
    
    def get_height(self):
        return len(self.squares)
    
    def get_width(self):
        return len(self.squares[1])
    
    
        
