import pygame
#if bomb collides w/ bad
##very rough outline code  #get this to work properly
class Red:
    def __init__(self, rx, ry):
        self.px = rx
        self.py = ry
        self.image_list = ["360_F_268712736_pYacy8wSc6CtXj1YzRMOOrSFZwsaJd0z.jpg"] #just test
        self.image = pygame.image.load(self.image_list[0])
        self.rect = pygame.Rect(self.px, self.py, self.image_list[0])

    def rescale_image(self, image): #works!!
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.6), int(self.image_size[1] * 0.6))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)


#want to have muliplte scaterred as an end goal not sure how I'll do that yet duplicate image?
# move across the screen at what rate/ when/ how/??