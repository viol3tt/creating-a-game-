import pygame
import random
import time
from plane import Plane

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 15)
start_font = pygame.font.SysFont('Times', 95)

bg = pygame.image.load("france background.jpg")



# set up variables for the display
SCREEN_HEIGHT = 846 #find an image for background, maybe it's day but like in future code could have an elapsed time
#and at a certain point becomes night
SCREEN_WIDTH = 1300
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = True
current_time = 0
elapsed_time = 0  # doesn't start until after title screen

p = Plane(200, 350) #start at top left of screen

#bg = pygame.image.load("background.png") #will be interacted with? if yes needs a seperate class


# render the text for later
start_screen = start_font.render("Start Game", True, (155, 125, 240))
total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255)) #set this up

# Instantiate


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_plane("right")
    elif keys[pygame.K_a]:
        p.move_plane("left")

    if title_screen:
        elapsed_time = time.time() - current_time
        total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True,
                                    (255, 255, 255))  #maybe don't display but simply keep note of it and \
        #after certain time different changes happen

    # --- Main event loop
    ## ----- NO BLIT ZONE START ----- ##
    for event in pygame.event.get():  # User did something
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and title_screen:  # disapear after being clicked once
            title_screen = False
        if event.type == pygame.QUIT:  # If user clicked close
            run = False


    ##  ----- NO BLIT ZONE END  ----- ##

    ## FILL SCREEN, and BLIT here ##
    screen.blit(bg, (0, 0)) #when upload background image into the game
    if title_screen:
        screen.blit(start_screen, (430, 350)) #w, h
    if not title_screen:
        screen.blit(p.image, p.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




