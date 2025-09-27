import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    BLACK = (0, 0 , 0)
    clock = pygame.time.Clock ()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_status = 1
    #initializes player
    player = Player (SCREEN_WIDTH / 2 , SCREEN_HEIGHT /2)

    while game_status != 0:

        #makes close button work
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                return
        #fills screen with black color
        screen.fill (BLACK, None, 0)

        
        player.update (dt)
        player.draw (screen)

        #pauses game loop for 1/60 of a second
        dt = clock.tick(60) / 1000
        
        #updates game screen
        pygame.display.flip ()



if __name__ == "__main__":
    main()
