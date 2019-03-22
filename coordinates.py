'''
Created on Mar 18, 2019

@author: aapolinjama
'''
class Coordinates():

    def __init__(self, x, y):
        '''
        Creates a new coordinate pair.

        Parameter x: int

        Parameter y: int
        '''
        self.x = x    # fixed value
        self.y = y    # fixed value


    def get_x(self):
        '''
        Returns the x coordinate (int)
        '''
        return self.x



    def get_y(self):
        '''
        Returns the y coordinate (int)
        '''
        return self.y