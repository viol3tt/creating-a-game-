import pygame
import random
import time
from plane import Plane
from bomb import Bomb
from red import Red

#set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times', 15)
start_font = pygame.font.SysFont('Times', 95)

# set up variables for the display
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = True
drop_bomb = False #is this even neccessairy
current_time = time.time()
elapsed_time = 0  #doesn't start until after title screen
red_number = 1 #variable set for how many duplicates
red_objects = [] #will store multiple instances (red circles)

#background(s)
bg = pygame.image.load("river landscape.jpg")


p = Plane(25, 50) #start at top left of screen
b = Bomb(50,500)#need to always set plane's location as a variable and bomb when button is clicked will appear right bellow


#bg = pygame.image.load("background.png") #will be interacted with? if yes needs a seperate class


# render the text for later
start_screen = start_font.render("Start Game", True, (155, 125, 240))
instructions = my_font.render("click b to drop bomb, a & d to move left right", True, (0, 0, 0))
#display for now
total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255))

# Instantiate


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 60
while run:
    clock.tick(60)
#commands with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p.move_plane("right")
    elif keys[pygame.K_a]:
        p.move_plane("left")
    elif keys[pygame.K_b]:
        drop_bomb = True
        b.move_bomb()
        Bomb = Plane(px-5, py-5) #how would I get this to work...?

    #if b.rect.colliderect(r.rect):

#deal with later // causing error messages
    #for i in range(red_number):
        #rx = random.randint(100, 900)
        #ry = random.randint(100, 650) #random location
        #red_obj = Red(rx, ry)
        #red_objects.append(red_obj)
    elapsed_time = time.time() - current_time
    elapsed_time = int(elapsed_time)
    total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255))
    if elapsed_time == 10:  # night??
        bg = ("france background.jpg")
    ####################################################################
    for event in pygame.event.get():  # User did something
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and title_screen:  #disapear after being clicked once
            title_screen = False
            elapsed_time = time.time() - current_time
            # after certain time different changes happen, background change??
            # at a certain point becomes night?
        if event.type == pygame.QUIT:  #Closed the tab, game over
            run = False


    ## FILL SCREEN, and BLIT here ##
    screen.blit(bg, (0, 0)) #when upload background image into the game
    #not working for changing background I'm not sure why
    if title_screen:
        screen.blit(start_screen, (430, 350)) #w, h
        screen.blit(instructions, (430, 400))
    if not title_screen:
        screen.blit(total_time, (20, 20)) #we will fix location/stuff later, main goal get game to work first!!
        screen.blit(p.image, p.rect)
        #screen.blit(r.image, r.rect) * red_number
        if drop_bomb:
            screen.blit(b.image, b.rect)
    pygame.display.update()
    ## END OF WHILE LOOP

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




