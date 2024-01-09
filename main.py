import pygame
from classes import Box, Player


BACKGROUND = (255, 0, 0)

def main():
    pygame.init()
    BACKGROUND = (255,0,0)
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    player = Player(100,200,1)
    boxes = []
    for bx in range(0,600,70):
      boxes.append(Box(bx,300))
    boxes.append(Box(500,200))
    done = False
    while not done:
        ## LAJ added this to allow the user to close the window down with the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.event.pump() # LAJ what does this do?
        player.update(boxes)
        
        #Drawing
        screen.fill(BACKGROUND)
        
        for box in boxes:
          box.draw(screen)
        player.draw(screen)
        pygame.display.flip()
        

        clock.tick(60)


main()
