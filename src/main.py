import pygame
import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
from pygame import mixer

from src.config.settings import *
from src.game.hand import Hand
from src.game.insect import Insect
from src.game.game_state import GameState

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        
        # Set up display
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch Ball")
        icon = pygame.image.load(BALL_ICON).convert_alpha()
        pygame.display.set_icon(icon)
        
        # Load background
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert()
        
        # Initialize camera and hand detector
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, WIDTH)
        self.cap.set(4, HEIGHT)
        self.detector = HandDetector(maxHands=MAX_HANDS, detectionCon=DETECTION_CONFIDENCE)
        
        # Initialize sound
        self.setup_sound()
        
        # Initialize game objects
        self.hand = Hand()
        self.insects = [Insect() for _ in range(NUMBER_OF_INSECTS)]
        self.game_state = GameState()
        
        # Game clock
        self.clock = pygame.time.Clock()

    def setup_sound(self):
        """Initialize game sounds"""
        mixer.music.load(BACKGROUND_MUSIC)
        mixer.music.play(loops=-1)
        self.closed_hand_sound = mixer.Sound(SLAP_SOUND)
        self.catching_sound = mixer.Sound(CATCHING_SOUND)

    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.cleanup()
                return False
        return True

    def update_hand_tracking(self):
        """Update hand tracking from camera"""
        success, frame = self.cap.read()
        if not success:
            return None
        
        hands, frame = self.detector.findHands(frame)
        cv2.imshow("webcam", frame)
        
        if hands:
            return hands[0]['lmList']
        return None

    def update(self):
        """Update game state"""
        # Update hand position and state
        hand_position = self.update_hand_tracking()
        if hand_position:
            self.hand.update_position(hand_position)
            prev_state = self.hand.is_closed
            self.hand.update_state(hand_position)
            
            # Handle hand state changes and collisions
            if self.hand.is_closed and not prev_state:
                self.closed_hand_sound.play()
                
            if self.hand.is_closed:
                for insect in self.insects:
                    if self.hand.get_rect().colliderect(insect.rect) and self.hand.catch_insect:
                        self.game_state.update_score()
                        self.catching_sound.play()
                        self.hand.catch_insect = False
                        insect.reset_position()
            else:
                for insect in self.insects:
                    if self.hand.get_rect().colliderect(insect.rect):
                        self.hand.catch_insect = True

        # Update insects
        for insect in self.insects:
            insect.update()

    def draw(self):
        """Draw game elements"""
        # Draw background
        self.screen.blit(self.background, (0, 0))
        
        # Draw insects
        for insect in self.insects:
            insect.draw(self.screen)
        
        # Draw hand
        self.hand.draw(self.screen)
        
        # Draw UI
        self.game_state.draw_score(self.screen)
        self.game_state.draw_timer(self.screen)
        
        # Update display
        pygame.display.update()

    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        pygame.quit()
        sys.exit()

    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            if not running:
                break
                
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
            if self.game_state.is_game_over():
                pygame.time.wait(3000)  # Wait 3 seconds before closing
                running = False
        
        self.cleanup()

if __name__ == "__main__":
    game = Game()
    game.run() 