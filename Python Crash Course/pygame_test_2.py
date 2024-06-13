# Note) to run -- try run and debug instaed of play

import pygame
# for creating video games basically easy to use as beginners

from pygame.locals import *
pygame.init()# to call all functionalities

# for understanding colors rgb
# red = (0,200,255)
# orange = (200,0,200)
# setting the screen 
screen = pygame.display.set_mode((400,500)) # initializes screen

# for understanding colors rgb
# font = pygame.font.Font('freesanbold.ttf',24)# the font desc
# text = font.render('hello kitty...' True,red) the test desc

#textrect = text.get_rect()#the text rect don't know yet
# a game loop
while True:
    screen.fill((200,0,0)) # background
    #screen.blit(text, textrecct) # call display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # deacivates the pygame library
            pygame.quit()

            # quit the program
            quit()
        # draws the surface object to the screen
        pygame.display.update() #print everytime until no data available

# difference between update and flip
# events in pygame
# clock