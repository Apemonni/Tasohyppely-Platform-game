'''
Created on Apr 16, 2019

@author: aapolinjama
'''
from PyQt5.Qt import  QGraphicsRectItem, QBrush, QColor
from map import Map

class SquareGraphs:
    
    def __init__(self):
        self.map = Map()
        self.objects = self.map.get_map()
        self.graphSquares = [None] * self.map.get_height()
    
    def create_square_graphs(self):
        a = 0
        b = 0
        for i in range(self.map.get_height()):
            self.graphSquares[i] = [None] * self.map.get_width()
            for j in range(self.map.get_width()):
                squar = QGraphicsRectItem(b*50, a*50, 50, 50)
                if not self.objects[i][j].is_obstacle:
                    color = QColor(20,20,20)
                    brush = QBrush(color)
                    squar.setBrush(brush)
                    b += 1
                else:
                    color = QColor(211,211,211)
                    brush = QBrush(color)
                    squar.setBrush(brush)
                    b += 1
                self.graphSquares[i][j] = squar
            a += 1
            b = 0
        return self.graphSquares
                    
                    
                    
                    
    