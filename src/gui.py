'''
Created on Mar 22, 2019

@author: aapolinjama
'''
from player import Player
from map import Map
from square_graphics import SquareGraphs
import sys
from PyQt5.QtCore import (
    QBasicTimer
)
from PyQt5 import QtWidgets
from PyQt5.Qt import  QGraphicsRectItem, QBrush, QColor


class GUI(QtWidgets.QMainWindow):
    
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        
        # hold the set of keys we're pressing
        self.keys_pressed = set()

        # use a timer to get refresh
        self.timer = QBasicTimer()
        self.timer.start(3, self)
        
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.horizontal = QtWidgets.QHBoxLayout() # Horizontal main layout
        self.centralWidget().setLayout(self.horizontal)
        '''
        Sets up the window.
        '''
        self.setGeometry(300, 300, 900, 1000)
        self.setWindowTitle('Tasohyppely')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 750, 750)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
        self.graph = SquareGraphs()
        self.graphSquares = self.graph.create_square_graphs()
        self.map = Map()
        
        for i in range(self.map.get_height()):
            for j in range(self.map.get_width()):
                self.scene.addItem(self.graphSquares[i][j])
        
        self.player = Player()
        self.player.setPos((450-self.player.pixmap().width())/2,
                           (600-self.player.pixmap().height())/2)
        self.scene.addItem(self.player)
        
    def get_graphSquares(self):
        return self.graphSquares
        
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()
    
    def game_update(self):
        self.player.game_update(self.keys_pressed)