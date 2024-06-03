import pygame
import random
import time
from plane import Plane
from bomb import Bomb
from red import Red
from green import Green

#set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comforta', 25)
start_font = pygame.font.SysFont('Comforta', 95)

# set up variables for the display
SCREEN_HEIGHT = 750
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
title_screen = True
end_screen = False
current_time = time.time()
elapsed_time = 0  #doesn't start until after title screen
red_number = 5 #variable set for how many duplicates
green_number = 5
score = 0
red_objects = [] #will store multiple instances (red circles)
green_objects = []

#background(s)
bg = pygame.image.load("river landscape.jpg")
night_bg = pygame.image.load("france background.jpg")
current_bg = bg

p = Plane(25, 50) #start at top left of screen
b = Bomb(-100,-100)#bomb starts off screen until activated


# render the text for later
start_screen = start_font.render("Start Game", True, (155, 125, 240))
instructions = my_font.render("click b to drop bomb, a & d to move left right", True, (0, 0, 0))
#display for now
total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255))
display_score = my_font.render("Score: " + str(score) + " points", True, (0, 0, 0))
display_gameover = start_font.render("Game Over!", True, (155, 125, 240))


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop ----------- #
clock = pygame.time.Clock()
frame = 60 #should I remove or incorperate something with this
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

#RED CIRCLE
    if b.rect.top >= 0: #bomb will move only when it's visible on the screen
        b.move_bomb()

    if len(red_objects) < red_number: #makes sure there's always set amount of red
        rx = random.randint(100, 900)
        ry = random.randint(100, 650) #random location
        red_obj = Red(rx, ry)
        red_objects.append(red_obj)

    for red_obj in red_objects:
         red_obj.move_red()
    if b.rect.bottom >= 750: #if bomb is off screen
        #add something for when circles become off screen
        b.rect.topleft = (-100, -100)

#a) when collide get the bomb to stop moving
#b)explosion image will replace bomb image
#c)appear/disapear quickly


    #bomb collides w/red circle
    collided_red_objects = []
    # when collide change background color a bit or should I add an explosion image
    for red_obj in red_objects:
        if b.rect.colliderect(red_obj.rect):
            collided_red_objects.append(red_obj)
            score += 10
            display_score = my_font.render("Score: " + str(score) + " points", True, (0, 0, 0))
            b.rect.topleft = (-100, -100)

    for red_obj in collided_red_objects:
        red_objects.remove(red_obj)

#GREEN CIRCLE #add code to make sure green circle doesn't appear on red circle + maybe certain distance away
    #if b.rect.top >= 0:
        #b.move_bomb()  #need twice...??

    if len(green_objects) < green_number:
        gx = random.randint(100, 900)
        gy = random.randint(100, 650)
        #for rx in red_objects:
            #if gx == rx[i]:
                #gx = random.randint(100, 900)
            #if gx == rx[i] (find code for like between a certain range of numbers)
            #i = i + 1
        #if not gx == rx and not gy == ry #will have to somehow go through whole list
        green_obj = Green(gx, gy)
        green_objects.append(green_obj)

    for green_obj in green_objects:
        green_obj.move_green()
    if b.rect.bottom >= 750:  # if bomb is off screen
        b.rect.topleft = (-100, -100)

    collided_green_objects = []
    for green_obj in green_objects:
        if b.rect.colliderect(green_obj.rect):
            collided_green_objects.append(green_obj)
            score -= 10
            display_score = my_font.render("Score: " + str(score) + " points", True, (0, 0, 0))
            b.rect.topleft = (-100, -100)

    for green_obj in collided_green_objects:
        green_objects.remove(green_obj)
#make bomb stop and explode when hits circle
#OTHER STUFF
    elapsed_time = int(time.time() - current_time)
    total_time = my_font.render("Elapsed Time: " + str(round(elapsed_time, 2)) + "s", True, (255, 255, 255))
    if int(elapsed_time) == 25:
        end_screen = True
    #background change
    if 20 >= elapsed_time >= 10: #need to generalize more, game could have a max time/ time limit and then determine
        #night/day
        current_bg = night_bg
    else:
        current_bg = bg
    ####################################################################
    for event in pygame.event.get():  # User did something
        print(event)
        if event.type == pygame.MOUSEBUTTONDOWN and title_screen:  #disapear after being clicked once
            title_screen = False
            elapsed_time = time.time() - current_time
        if event.type == pygame.QUIT:  #Closed the tab, game over
            run = False


    ## FILL SCREEN, and BLIT here ##
    screen.blit(current_bg, (0, 0))
    if title_screen:
        screen.blit(start_screen, (320, 320)) #w, h
        screen.blit(instructions, (315, 400))
    if not title_screen and not end_screen : #end screen not appearing
        screen.blit(total_time, (20, 20))
        screen.blit(display_score, (20, 40))
        screen.blit(p.image, p.rect)
        for red_obj in red_objects: #red circles
            screen.blit(red_obj.image, red_obj.rect)
        for green_obj in green_objects: #green circles
            screen.blit(green_obj.image, green_obj.rect)
        if b.rect.top >=0:
            screen.blit(b.image, b.rect)
        if end_screen:
            screen.blit(display_gameover, (320, 320))
            screen.blit(display_score, (20, 40))  # will this cause a problem??
    pygame.display.update()


# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




