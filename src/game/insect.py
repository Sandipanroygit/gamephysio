import pygame
import random
from src.config.settings import *

class Insect:
    def __init__(self):
        self.image = pygame.image.load(BALL_ICON).convert_alpha()
        self.reset_position()
        self.move_x = 10
        self.move_y = 8

    def reset_position(self):
        """Reset insect to a random position"""
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self):
        """Update insect position and handle boundary collisions"""
        # X-axis movement
        self.rect.right += self.move_x
        if self.rect.right <= 16:
            self.move_x += 10
        elif self.rect.right >= WIDTH:
            self.move_x -= 10

        # Y-axis movement
        self.rect.top += self.move_y
        if self.rect.top <= 0:
            self.move_y += 8
        elif self.rect.top >= HEIGHT - 32:
            self.move_y -= 8

    def draw(self, screen):
        """Draw the insect on the screen"""
        screen.blit(self.image, self.rect) 