import pygame
#if bomb collides w/ bad
##very rough outline code  #get this to work properly
class Red:
    def __init__(self, rx, ry):
        self.prx = rx
        self.pry = ry
        self.image_list = ["red circle.JPG"] #just test
        self.image = pygame.image.load(self.image_list[0])
        self.rect = pygame.Rect(self.prx, self.pry, self.image_list[0])

    def rescale_image(self, image): #works!!
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * 0.6), int(self.image_size[1] * 0.6))  # Scale size should be integers
        self.image = pygame.transform.scale(self.image, scale_size)


#want to have muliplte scaterred as an end goal not sure how I'll do that yet duplicate image?
# move across the screen at what rate/ when/ how/??

    def move(self):
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5) #d for direction moving
        self.prx += drx
        self.pry += dry
        self.rect = pygame.Rect(self.prx, self.pry, self.image_size[0], self.image_size[1])
