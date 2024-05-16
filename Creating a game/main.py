import pygame
import random
import time
from plane import Plane
from bomb import Bomb

#set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 15)
start_font = pygame.font.SysFont('Times', 95)

bg = pygame.image.load("river landscape.jpg")



# set up variables for the display
SCREEN_HEIGHT = 750 #find an image for background, maybe it's day but like in future code could have an elapsed time
#and at a certain point becomes night
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = True
drop_bomb = False
current_time = 0
elapsed_time = 0  # doesn't start until after title screen

p = Plane(25, 50) #start at top left of screen
b = Bomb(50,500)#need to always set plane's location as a variable and bomb when button is clicked will appear right bellow
r = Red(75, 550) #random location for now change later

#bg = pygame.image.load("background.png") #will be interacted with? if yes needs a seperate class


# render the text for later
start_screen = start_font.render("Start Game", True, (155, 125, 240))
instructions = my_font.render("click b to drop bomb, a & d to move left right", True, (0, 0, 0))
total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255)) #set this up

# Instantiate


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 60
while run:
#worry about later
#if title_screen:
    #elapsed_time = time.time() - current_time
    #total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True,
                                #(255, 255, 255))  # maybe don't display but simply keep note of it and \
    # after certain time different changes happen
    clock.tick(60)
#commands with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_plane("right")
    elif keys[pygame.K_a]:
        p.move_plane("left")
    elif keys[pygame.K_b]:
        drop_bomb = True
        Bomb = Plane(px-5, py-5) #how would I do this...?
    if b.rect.colliderect(r.rect):

####################################################################
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
        screen.blit(instructions, (430, 400))
    if not title_screen:
        screen.blit(p.image, p.rect)
        if drop_bomb:
            screen.blit(b.image, b.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




