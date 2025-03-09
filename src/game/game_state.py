import pygame
from src.config.settings import *

class GameState:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
        self.gameover_font = pygame.font.Font('freesansbold.ttf', GAMEOVER_FONT_SIZE)
        self.start_time = pygame.time.get_ticks()

    def update_score(self):
        """Increment the score"""
        self.score += 1

    def get_current_time(self):
        """Get the current game time in seconds"""
        return (pygame.time.get_ticks() - self.start_time) / 1000

    def draw_score(self, screen):
        """Draw the score on the screen"""
        score_text = self.font.render(f"Score : {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    def draw_timer(self, screen):
        """Draw the timer on the screen"""
        current_time = self.get_current_time()
        time_left = GAME_DURATION - current_time
        
        if current_time >= WARNING_TIME:
            color = RED
        else:
            color = WHITE
            
        timer_text = self.font.render(f"Time: {int(time_left)}", True, color)
        screen.blit(timer_text, (1210, 10))
        
        if current_time >= GAME_DURATION:
            gameover_text = self.gameover_font.render("Game Over!", True, RED)
            screen.blit(gameover_text, (WIDTH/2 - 300, HEIGHT/2 - 30))
            return True
        return False

    def is_game_over(self):
        """Check if the game is over"""
        return self.get_current_time() >= GAME_DURATION 