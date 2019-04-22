'''
Created on Mar 22, 2019

@author: aapolinjama
'''
from player import Player
from enemy_container import Enemy_container
from map import Map
from square_graphics import SquareGraphs
import sys
from enemy import Enemy
from PyQt5.QtCore import (
    QBasicTimer
)
from PyQt5 import QtWidgets
from PyQt5.Qt import  QGraphicsRectItem, QBrush, QColor, QLabel, QFont, QWidget, QVBoxLayout


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
        self.showFullScreen()

        # Add a scene for drawing 2d objects
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 800, 800)

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
        self.player.setPos(53, 700)
        self.scene.addItem(self.player)
        self.enemy_container = Enemy_container()
        self.enemy = Enemy()
        self.enemy.setPos(200, 500)
        self.scene.addItem(self.enemy)
        self.enemy_container.add_enemy(self.enemy)
        self.enemy2 = Enemy()
        self.enemy2.setPos(650, 300)
        self.scene.addItem(self.enemy2)
        self.enemy_container.add_enemy(self.enemy2)
        self.enemy3 = Enemy()
        self.enemy3.setPos(150,200)
        self.scene.addItem(self.enemy3)
        self.enemy_container.add_enemy(self.enemy3)
        self.enemies = self.enemy_container.get_enemies()
        self.text = QLabel()
        self.text.setText("You Won!")
        a = QFont("Arial", 40, QFont.Bold)
        self.text.setFont(a)
        
        self.text1 = QLabel(self.centralWidget())
        self.text1.setText("You Lost!")
        a = QFont("Arial", 40, QFont.Bold)
        self.text1.setFont(a)
        self.draw_loss = 250
        self.a = 0
    
            
        
    def get_graphSquares(self):
        return self.graphSquares
        
    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        
        self.game_update()
        if self.player.has_won():
            
            self.horizontal.addWidget(self.text)
            self.draw_won = 1

            
            
        if self.player.get_draw_won() == 1:
            
            self.horizontal.removeWidget(self.text)
            self.text.deleteLater()
            self.text = None
            self.player.add_draw_won()
            self.reset_won()
            
        self.player.check_if_coll_enemy(self.enemies)
        if self.player.has_lost():
            self.a = 1
            self.horizontal.addWidget(self.text1)
        if self.a == 1 and self.draw_loss > 1:
            self.draw_loss -= 1
            
            
        if self.draw_loss == 1:
            self.horizontal.removeWidget(self.text1)
            self.text1.deleteLater()
            self.text1 = None
            self.player.add_draw_loss()
            self.reset_loss()
            self.a = 0
            self.draw_loss = 250
            
            
        
    
            
        self.enemy.enemy_update()
        self.enemy2.enemy_update()
        self.enemy3.enemy_update()
        self.update()
    
    def reset_won(self):
        self.text = QLabel()
        self.text.setText("You Won!")
        a = QFont("Arial", 35, QFont.Bold)
        self.text.setFont(a)
        
    def reset_loss(self):
        self.text1 = QLabel()
        self.text1.setText("You Lost!")
        a = QFont("Arial", 35, QFont.Bold)
        self.text1.setFont(a)
        
    
    def game_update(self):
        self.player.game_update(self.keys_pressed)