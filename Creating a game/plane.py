import pygame


class Plane:

    def __init__(self):
        self.image = pygame.image.load("plane.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    #def rescale_image(self, image): #include???
        #self.image_size = self.image.get_size()
        #scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        #self.image = pygame.transform.scale(self.image, scale_size)

    def move_plane(self, direction):
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
