#(c) A+ Computer Science
# www.apluscompsci.com

import pygame, sys, time
from pygame.locals import *
from Molecule import *
from Button import *

# Initialize pygames and set the screen
pygame.init()
theScreen = pygame.display.set_mode((800,600))

# Create molecules
moles=[]

for x in range(50):
    moles.append(Molecule(random.randint(0,800),random.randint(150,600), 10,random.randint(0,359)))

#Create buttons to change the temperature
b1 = Button((800*.25),75,"Decrease Temperature")
b2 = Button((800*.5),75, "Reset")
b3 = Button((800*.75),75,"Increase Temperature")


while True:
    #Draw the screen
    theScreen.fill((255,255,255))
    pygame.draw.rect(theScreen, (102, 0, 153),(0,0,800,100))

    # Draw the buttons on the screen
    b1.draw(theScreen)
    b2.draw(theScreen)
    b3.draw(theScreen)

    # Draw the text that displays the temperature
    font = pygame.font.Font(None, 35)
    text = font.render(("Temperature = " + str(moles[0].getSpeed())),1, (255,255,255))
    textpos = text.get_rect(centerx=400, centery=30)
    theScreen.blit(text, textpos)

    # Move and draw each molecule
    for m in moles:
        m.move()
        m.draw(theScreen)


    # Process events/input
    for event in pygame.event.get():
        # If the window is closed or Esc is pressed end the program
        if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
            pygame.quit()
            sys.exit()

        # If the mouse is clicked while on a button, change the temperature
        if event.type==MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if b1.isClicked(pos):
                if moles[0].getSpeed() > 0:
                    moles[0].decreaseSpeed()
            elif b2.isClicked(pos):
                moles[0].resetSpeed()
            elif b3.isClicked(pos):
                moles[0].increaseSpeed()

        # If up or down arrows, or spacebar is pressed, change the temperature
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                moles[0].resetSpeed()
            elif event.key==K_DOWN:
                if moles[0].getSpeed() > 0:
                    moles[0].decreaseSpeed()
            elif event.key==K_UP:
                moles[0].increaseSpeed()
   
    # Update screen
    pygame.display.flip()
    time.sleep(.02)
