import pygame
import time

class Bomb:
    def __init__(self, bx, by):
        self.image_list = ["bombv2.PNG", "explode.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image_bomb()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(bx, by, self.image_size[0], self.image_size[1])
        self.speed_by = 10  # Speed at which the bomb falls
        self.exploded = False

    def rescale_image_bomb(self):
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.1), int(self.image_size[1] * 0.1))
        self.image = pygame.transform.scale(self.image, scale_size)
    def move_bomb(self):
       if not self.exploded:
            self.rect.y += self.speed_by

    def explode(self, current_time):
        self.image = pygame.image.load(self.image_list[1])  #explosion image!!!
        self.rescale_image_bomb()
        self.exploded = True
        self.explosion_time = current_time  #storing bomb explosion time

    def reset_bomb(self):
        if self.exploded and (time.time() - self.explosion_time) >= 3:
            self.exploded = False
            self.image = pygame.image.load(self.image_list[0]) #go back to bomb image
            self.rescale_image_bomb()
            self.rect.topleft = (-100, -100)  #bomb goes off screen

