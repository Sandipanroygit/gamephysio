# Catch Ball Game

A fun interactive game where you catch balls using hand gestures captured through your webcam. The game uses computer vision to track your hand movements and lets you catch moving balls on the screen.

## Requirements

- Python 3.7+
- Webcam
- The following Python packages:
  - pygame
  - opencv-python
  - cvzone

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install pygame opencv-python cvzone
```

3. Make sure your assets are in the correct directories:

```
assets/
├── images/
│   ├── ball_32.png
│   ├── closedHand.png
│   ├── openHand.png
│   └── TennisBack.png
└── music/
    ├── background.mp3
    ├── catching_sound.wav
    └── slap.mp3
```

## How to Play

1. Run the game:

```bash
python src/main.py
```

2. Game Controls:

- Use your hand in front of the webcam to control the game
- Open your hand to move around
- Close your hand over a ball to catch it
- Try to catch as many balls as possible before the time runs out!

3. Scoring:

- Each caught ball adds 1 point to your score
- The game ends after 100 seconds
- Try to get the highest score possible!

## Game Features

- Real-time hand tracking
- Sound effects for catching and hand movements
- Background music
- Timer with visual warning when time is running low
- Score tracking
- Multiple moving balls to catch

## Project Structure

```
src/
├── config/
│   └── settings.py      # Game configuration and constants
├── game/
│   ├── hand.py         # Hand tracking and rendering
│   ├── insect.py       # Ball/insect movement and rendering
│   └── game_state.py   # Game state management
└── main.py             # Main game loop and initialization
```

# Description

Multiple sclerosis (MS) is a condition that can affect the brain and spinal cord, causing a wide range of potential symptoms, including problems with vision, arm or leg movement, sensation, or balance. We have designed an exergame using computer vision for arm rehabilitation in individuals with multiple sclerosis.

# How to run

**Make Environment Ready By Following Steps Below:**<br>
1- Install [python 3.10 and pip](https://www.python.org/) on your computer<br>
2- Open your Terminal and by pip install mediapipe, pygame, cv2 and cvzone<br>
3- Clone the project on your computer or you can download the code from GitHub link above, and place it on your system<br>
4- Open your Terminal app inside the Root directory of the project and run main.py: `python main.py`<br>
5- Play the game

## Demo

![demo](https://github.com/mo-kasiri/catch_ball/assets/20669157/f3f83464-3ef2-4386-ad55-3213f869fe82)

# How to play

In the game-play, try to catch the Balls with your hand (it doesn't matter which one), so open your hand, and when a ball comes inside your hand, try to close it instantly.

# Soloution for possible errors

1. You must have a webcam to play this game, or you can use your smartphone as a webcam<br>
1. You need to change your webcam ID and set it to 0, or if it is not possible to change the camera ID, you can open the main.py file and in line 10 change the ID, set it on your webcam ID<br>
1. Check the direction of your webcam, and make sure that it's not upside down or reflects your picture as a mirror (that would cause the hand image in the game moves in the opposite direction of your actual hand)<br>
1. In case of missing a specific library make sure which one is missing, and try to Install it (it could be any one of these "cvzone, mediapipe, opencv and pygame")<br>
1. If you encounter issues while playing the game, such as a decrease in speed or the game not functioning correctly, try restarting the game to potentially solve the problem.<br>
