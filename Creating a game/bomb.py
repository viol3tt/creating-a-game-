import pygame

import pygame

class Bomb:
    def __init__(self, bx, by):
        self.image_list = ["bombv2.PNG"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image_bomb()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(bx, by, self.image_size[0], self.image_size[1])
        self.speed_by = 10  # Speed at which the bomb falls

    def rescale_image_bomb(self):
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.1), int(self.image_size[1] * 0.1))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_bomb(self):
        #  code it so it falls down a bit like 20/30 or whatever amount per second
        # orr... is their a way to use frames for this maybe
        self.rect.y += self.speed_by


#could create set amount of bombs here, that can be used at once

