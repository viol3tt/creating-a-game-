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
current_time = time.time()
elapsed_time = 0  #doesn't start until after title screen
red_number = 5 #variable set for how many duplicates
score = 0
red_objects = [] #will store multiple instances (red circles)

#background(s)
bg = pygame.image.load("river landscape.jpg")
night_bg = pygame.image.load("france background.jpg") # why is it automattically going to this bg
current_bg = bg

p = Plane(25, 50) #start at top left of screen
b = Bomb(-100,-100)#bomb starts off screen until activated


# render the text for later
start_screen = start_font.render("Start Game", True, (155, 125, 240))
instructions = my_font.render("click b to drop bomb, a & d to move left right", True, (0, 0, 0))
#display for now
total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255))


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop ----------- #
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
    #activate bomb
    if keys[pygame.K_b] and b.rect.top < 0:
       b.rect.topleft = (p.rect.centerx, p.rect.bottom)  #bomb will be bellow the plane

    if b.rect.top >= 0:
        b.move_bomb()

    if len(red_objects) < red_number: #makes sure there's always set amount of red
        rx = random.randint(100, 900)
        ry = random.randint(100, 650) #random location
        red_obj = Red(rx, ry)
        red_objects.append(red_obj)

    for red_obj in red_objects:
         red_obj.move()
    if b.rect.bottom >= 750: #if bomb is off screen
        b.rect.topleft = (-100, -100)

    #bomb collides w/ red
    if b.rect.colliderect(red_obj.rect):
        for red_obj in red_objects:
            red_objects.remove(red_obj)
            score += 10
            b.rect.topleft = (-100, -100)

    elapsed_time = int(time.time() - current_time)
    total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255))

    #background change
    if elapsed_time % 120 == 0 and not elapsed_time % 60 == 0:
        current_bg = night_bg
    else:
        current_bg = bg
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
    screen.blit(current_bg, (0, 0))
    if title_screen:
        screen.blit(start_screen, (430, 350)) #w, h
        screen.blit(instructions, (430, 400))
    if not title_screen:
        screen.blit(total_time, (20, 20)) #we will fix location/stuff later, main goal get game to work first!!
        screen.blit(p.image, p.rect)
        for red_obj in red_objects:
            screen.blit(red_obj.image, red_obj.rect)
        if b.rect.top >=0:
            screen.blit(b.image, b.rect)
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




