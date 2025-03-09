import pygame
from src.config.settings import *

class Hand:
    def __init__(self):
        self.x = WIDTH/2 - 64
        self.y = HEIGHT/2 - 64
        
        # Load hand images
        self.open_hand_img = pygame.image.load(OPEN_HAND_IMAGE).convert_alpha()
        self.open_hand_img = pygame.transform.scale(self.open_hand_img, (128, 128))
        self.open_hand_rect = self.open_hand_img.get_rect(topleft=(self.x, self.y))
        
        self.closed_hand_img = pygame.image.load(CLOSED_HAND_IMAGE).convert_alpha()
        self.closed_hand_img = pygame.transform.scale(self.closed_hand_img, (128, 128))
        self.closed_hand_rect = self.closed_hand_img.get_rect(topleft=(self.x, self.y))
        
        self.fingers = [0, 0, 0, 0]
        self.is_closed = False
        self.catch_insect = False

    def update_position(self, hand_position):
        """Update hand position based on detected hand landmarks"""
        x = (hand_position[9][0] - 200) * 1.5
        y = (hand_position[9][1] - 200) * 1.5
        self.open_hand_rect.topleft = (x, y)
        self.closed_hand_rect.topleft = (x, y)

    def update_state(self, hand_position):
        """Update hand state (open/closed) based on finger positions"""
        self.is_closed = True
        for index in range(4):
            if hand_position[INDEXES_FOR_CLOSED_FINGERS[index]][1] > hand_position[INDEXES_FOR_CLOSED_FINGERS[index] - 2][1]:
                self.fingers[index] = 1
            else:
                self.fingers[index] = 0
            if not all(self.fingers):
                self.is_closed = False

    def draw(self, screen):
        """Draw the hand on the screen"""
        if self.is_closed:
            screen.blit(self.closed_hand_img, self.closed_hand_rect)
        else:
            screen.blit(self.open_hand_img, self.open_hand_rect)

    def get_rect(self):
        """Get the current hand rectangle for collision detection"""
        return self.open_hand_rect 