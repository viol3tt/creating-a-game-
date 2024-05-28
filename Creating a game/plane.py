import pygame


class Plane:

    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.image_list = ["planebackup2.png", "planebackupflipped.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.px, self.py, self.image_size[0], self.image_size[1])

    def rescale_image(self, image): #works!!
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.6), int(self.image_size[1] * 0.6))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_plane(self, direction):
        if direction == "right":
            self.px += 2.5  #//
        elif direction == "left":
            self.px -= 2.5  #//

        #...
        self.rect = pygame.Rect(self.px, self.py, self.image_size[0], self.image_size[1])




