import pygame
import random
class Green:
#Once I get the red circle to work exactly as planned I will replicate the same code (mostly) with the green circles
    def __init__(self, gx, gy):
        self.pgx = gx
        self.pgy = gy
        self.image_list = ["greencircle.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()  # Move this line before creating self.rect
        self.rect = pygame.Rect(self.pgx, self.pgy, self.image_size[0], self.image_size[1])


    def rescale_image(self, image):  # works!!
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.03), int(self.image_size[1] * 0.03))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)


    def move_green(self):  # don't change numbers until you get collision w/ bomb to work
        dgx = random.randint(0, 0)
        dgy = random.randint(0, 0)  # d for direction moving
        self.pgx += dgx
        self.pgy += dgy
        self.rect = pygame.Rect(self.pgx, self.pgy, self.image_size[0], self.image_size[1])

