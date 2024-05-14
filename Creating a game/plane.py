import pygame


class Plane:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["planebackup2.png", "planebackupflipped.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


        ###

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.4), int(self.image_size[1] * 0.4))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)

    def move_plane(self, direction):
        if direction == "right":
            self.x += 5  #//
        elif direction == "left":
            self.x -= 5  #//

        #...
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])



