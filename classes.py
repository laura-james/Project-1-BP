import pygame

# size    = [400,400]
# screen  = pygame.display.set_mode(size)
ground = False


class Sprite(pygame.sprite.Sprite):
    def __init__(self, images, startx, starty):  # constructor method
        super().__init__()

        self.images = [pygame.image.load(image) for image in images]
        self.rect = self.images[0].get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.images[0], self.rect)
        # function to create the player model


class Player(Sprite):

    def __init__(self, startx, starty, direction):
        super().__init__(["sprites/p1_front.png"], startx, starty)
        self.stand_image = self.images

        self.facing_left = False

        self.speed = 4
        self.jumpspeed = 10
        self.vsp = 0  # vertical speed
        self._hsp = 0  # horizontal speed
        self.gravity = 0.5
        self.ground = False
        self.collide = True
        self.friction = 0.1
        self.hitwallr = False

    def checkcollision(self, Box):
        if self.rect.colliderect(Box.rect) and self.vsp > 0: #check that the bottom of the player is less than the centre of the box (as y is inverse)
            self.ground = True
            self.rect.bottom = Box.rect.top
        # check for collision on the right
        if self.rect.colliderect(Box.rect) and self.rect.right > Box.rect.left  : #LAJ change
            self.hitwallr = True  # LAJ change
            print("hit wall r")  # LAJ change
        else:#LAJ change
            self.hitwallr = False  # LAJ change
        # TODO check for collision on the left....


    def update(self, list):
        key = pygame.key.get_pressed()  # detects if a key is pressed

        if key[pygame.K_LEFT]:
            self._hsp = -self.speed
            self.facing_left = True
        elif key[pygame.K_RIGHT]:
            self._hsp = self.speed - self.friction
            self.facing_left = False
        else:
            self.image = self.stand_image

        if key[pygame.K_UP]:
            if self.ground:
                self.vsp = -self.jumpspeed
                self.ground = False

        if self.ground == False:
            if self.vsp < 10:  # if the player is travelling at less than gravity then gravity will drag the player down
                self.vsp += self.gravity  # adds gravity to the vertical speed to move downwards
        #LAJ moved this into this method rather than the move method
        if self.hitwallr == True:
            print("hitwall True")
            #self.speed = 0
            #self._hsp = 0
            self._hsp = -self.speed #bounce back
        else:
            self.hitwallr = False
            print("hitwall False")
            #self.speed = -4
            #self._hsp = 1

        # TODO check for collision on the left (see above)....
        #  End LAJ changes

        self.move(self._hsp, self.vsp, )

        for Box in list:
            self.checkcollision(Box)  # loops through the box list checking for collisions

        if self.ground == True:  # while player is on the ground it is set to true
            self.vsp = 0  # when the player is on the ground the vertical speed is set to 0

    def move(self, x, y):
        self.rect.move_ip([x, y])
        # function to move the player

class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__(["sprites/boxAlt.png"], startx, starty)

