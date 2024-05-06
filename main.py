import pygame
import random
import time

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 15)
start_font = pygame.font.SysFont('Times', 45)


# set up variables for the display
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = True

#bg = pygame.image.load("background.png") #will be interacted with? if yes needs a seperate class

r = 203
g = 237
b = 247

# render the text for later
start_screen = start_font.render("Start Game", True, (0, 0, 0))


# Instantiate


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:


    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        if event.type == pygame.MOUSEBUTTONDOWN and title_screen:  # disapear after being clicked once
            title_screen = False
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    #screen.blit(bg, (0, 0)) #when upload background image into the game
    screen.fill((r, g, b))
    if title_screen:
        screen.blit(start_screen, (200, 200)) #w, h
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




