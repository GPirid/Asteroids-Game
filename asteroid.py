import pygame
import random
from circleshape import *
from constants import *

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super ().__init__( x, y, radius)
    def draw (self, screen):
        pygame.draw.circle(screen, WHITE, self.position,  self.radius)

    def update (self, dt):
        self.position += (self.velocity * dt)

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
        new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        
        

class Shot (CircleShape):
    def __init__(self, x, y):
        super ().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
    
    def draw (self, screen):
        pygame.draw.circle(screen, WHITE, self.position,  self.radius)

    def update (self, dt):
        self.position += (self.velocity * dt)
        