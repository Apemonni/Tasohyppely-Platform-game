'''
Created on Mar 22, 2019

@author: aapolinjama
'''
from player import Player
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
        self.setGeometry(300, 300, 800, 800)
        self.setWindowTitle('Tasohyppely')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)
        a = 0
        b = 0
        
        map = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],[1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0], 
               [1, 1, 1, 0, 0, 1, 1, 1]]
        for i in map:
            for j in i:
                squar = QGraphicsRectItem(b*50, a*50, 50, 50)
                if j == 0:
                    color = QColor(20,20,20)
                    brush = QBrush(color)
                    squar.setBrush(brush)
                    self.scene.addItem(squar)
                    b += 1
                else:
                    color = QColor(211,211,211)
                    brush = QBrush(color)
                    squar.setBrush(brush)
                    self.scene.addItem(squar)
                    b += 1
            a += 1
            b = 0
        self.player = Player()
        self.player.setPos((450-self.player.pixmap().width())/2,
                           (600-self.player.pixmap().height())/2)
        self.scene.addItem(self.player)
        
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.game_update()
        self.update()
    
    def game_update(self):
        self.player.game_update(self.keys_pressed)