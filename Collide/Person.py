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
        x = self.x
        y = self.y
        otherRec = other.getRec()
        oRight = otherRec[0] + otherRec[1]

        oLeft = otherRec[0] - otherRec[1]

        oBottom = otherRec[1] + otherRec[3]
        oTop = myRec[1] - myRec[3]

        right = myRec[0] + myRec[2]
        bottom = myRec[1] + myRec[2]

        # if person is right of the object - person.x greater than (other.x + other.width)
        #    person and object do not intersect

        if x > 400-40 and x < 450 and y < 50:
            return True
        else:
            return False

    # This method returns a rectangle - (x, y, width, height)
    # that represents the object
    def getRec(self):
        myRec = self.img.get_rect()
        return (self.x, self.y, myRec[2], myRec[3])
