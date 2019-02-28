# (c) A+ Computer Science
# www.apluscompsci.com

import pygame
from pygame.locals import *


# Create a class called person
class Person:
    # Create a constructor method that sets self.x to newX, 
    # self.y to newY and loads the image "dude.gif" into self.img
    def __init__(self, newX, newY):
        self.x = newX
        self.y = newY
        self.img = pygame.image.load("dude.gif")

    # draw the image on the surface
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def moveLeft(self):
        self.x = self.x - 15
        pass

    def moveRight(self):
        self.x = self.x + 15
        pass

    def moveUp(self):
        self.y = self.y - 15
        pass

    def moveDown(self):
        self.y = self.y + 15
        pass

    # It will return True if your person has 
    # collided with another object
    def collide(self, other):
        myRec = self.getRec()
        otherRec = other.getRec()
        oRight = otherRec[0] + otherRec[2]
        oBottom = otherRec[1] + otherRec[3]

        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[3]

        if (otherRec[0] <= right) and (oRight >= self.x) and (otherRec[1] <= bottom) and (oBottom >= self.y):
            return True
        return False

    # This method returns a rectangle - (x, y, width, height)
    # that represents the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
