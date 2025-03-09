"""
Game configuration settings
"""

# Screen settings
WIDTH = 1366
HEIGHT = 768

# Game settings
FPS = 60
NUMBER_OF_INSECTS = 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Font settings
FONT_SIZE = 32
GAMEOVER_FONT_SIZE = 100

# Hand detection settings
MAX_HANDS = 1
DETECTION_CONFIDENCE = 0.8

# Asset paths
BACKGROUND_MUSIC = 'assets/music/background.mp3'
SLAP_SOUND = 'assets/music/slap.mp3'
CATCHING_SOUND = 'assets/music/catching_sound.wav'
BALL_ICON = 'assets/images/ball_32.png'
BACKGROUND_IMAGE = 'assets/images/TennisBack.png'
OPEN_HAND_IMAGE = 'assets/images/openHand.png'
CLOSED_HAND_IMAGE = 'assets/images/closedHand.png'

# Hand tracking
INDEXES_FOR_CLOSED_FINGERS = [8, 12, 16, 20]

# Game timing
GAME_DURATION = 100  # seconds
WARNING_TIME = 80  # seconds 