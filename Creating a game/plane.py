import pygame


class Plane:

    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.image_list = ["planebackup2.png", "planebackupflipped.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image = self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.px, self.py, self.image_size[0], self.image_size[1])

    def move_plane(self, direction):
        if direction == "right":
            self.px += 2.5
            self.image = pygame.image.load(self.image_list[0]) #plane facing right
        elif direction == "left":
            self.px -= 2.5
            self.image = pygame.image.load(self.image_list[1]) #plane facing left
        self.image = self.rescale_image(self.image) #reupdated scaling
        self.rect.topleft = (self.px, self.py)

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.4), int(self.image_size[1] * 0.4))  # Scale size should be integers
        scaled_image = pygame.transform.scale(image, scale_size)
        return scaled_image




