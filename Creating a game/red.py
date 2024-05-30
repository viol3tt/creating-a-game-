import pygame
import random
class Red:
    def __init__(self, rx, ry):
        self.prx = rx
        self.pry = ry
        self.image_list = ["testredcircle2.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()  # Move this line before creating self.rect
        self.rect = pygame.Rect(self.prx, self.pry, self.image_size[0], self.image_size[1])

    def rescale_image(self, image): #works!!
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.05), int(self.image_size[1] * 0.05))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_red(self): #don't change numbers until you get collision w/ bomb to work
        drx = random.randint(0, 0)
        dry = random.randint(0, 0) #d for direction moving
        self.prx += drx
        self.pry += dry
        self.rect = pygame.Rect(self.prx, self.pry, self.image_size[0], self.image_size[1])
