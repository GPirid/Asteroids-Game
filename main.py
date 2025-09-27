import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    
    clock = pygame.time.Clock ()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_status = 1
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    #initializes player
    player = Player (SCREEN_WIDTH / 2 , SCREEN_HEIGHT /2)
    Asteroid_Field = AsteroidField ()

    while game_status != 0:

        #makes close button work
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                return
        #fills screen with black color
        screen.fill (BLACK, None, 0)

        
        
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw (screen)

        #pauses game loop for 1/60 of a second
        dt = clock.tick(60) / 1000
        
        #updates game screen
        pygame.display.flip ()



if __name__ == "__main__":
    main()
