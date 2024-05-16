import pygame

import pygame

class Bomb:
    def __init__(self, bx, by):
        self.image_list = ["unnamed.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image_bomb()
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect(topleft=(bx, by))
        self.speed_by = 5  # Speed at which the bomb falls

    def rescale_image_bomb(self):
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.1), int(self.image_size[1] * 0.1))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_bomb(self):
        self.rect.by += self.speed_by  # Bomb falls downwards





