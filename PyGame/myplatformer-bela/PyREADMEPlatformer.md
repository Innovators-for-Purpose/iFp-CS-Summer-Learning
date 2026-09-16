# iFp Python Coding Practice: Platform game!

Welcome to iFp's Python coding practice 2! In this session you will practice Python by building your own version of a platform game with Pygame.

## What You'll Do

- Work with Python and the Pygame library
- Build your own version of a platform game in `myplatformer.py`
- Practice organizing a program into functions
- Create a player and platforms
- Add keyboard controls and jumping
- Add gravity and collision detection
- Create a scrolling screen for the game

## What You'll Learn

Work on this project will help you to:

- Improve your Python programming skills
- Understand variables and constants
- Work with lists
- Respond to keyboard and window events
- Use conditionals and loops
- Break a large problem into smaller functions

## Your Next Step

By the time you finish, or when you feel you've made good progress, you can choose a project path to continue with:

- Game Development with Python and Pygame
- Game Development in Godot 3.5
- Web Development with JavaScript, CSS, and HTML
- AI Research and Development using Python

## Before Start Coding

- Step 1: Install Python
Download and install([Python](https://www.python.org/downloads/)) on your computer. 

After installing Python, open your VS Code terminal and check that it works:

`python3 --version`

You should see a Python version number.

- Step 2: Install Pygame

Pygame is the Python library we will use to create the game.
Open your terminal and run:

`python3 -m pip install pygame`

## Start coding!

Navigate to VS Code in your applications and open the iFp Fall Coding Practice folder. In the `PyGame` folder, open `platformer.py` to study the example. Then create a new file named `myplatformer.py`. You will edit `myplatformer.py` and use the example as a guide while making your own version of the platform game.

Each section has an objective to help you understand both Python syntax and the structure of a small game. There are tips and definitions here to guide you and give you something to reference when you feel unsure. You are also encouraged to make your own decisions and research Python or Pygame documentation when you are curious or stuck. Your mentors will be available to answer questions.

## "myplatformer.py"

A Python file is a text file containing instructions written in the Python programming language. Python reads the instructions from top to bottom when the file runs.

Pygame is a Python library. A library is a collection of code that someone else has already written so you can use features such as windows, drawings, keyboard input, and timing.

The provided `platformer.py` file is a reference example. Your `myplatformer.py` file will contain the structure and behavior of your game. You will organize it into imports, constants, functions, game objects, and the main game loop.

### Imports and Setup

1. Open `platformer.py` in VS Code and look through the example.
2. Create a new file in the same folder named `myplatformer.py`.
3. Open `myplatformer.py` in VS Code.
4. Add the imports at the top of `myplatformer.py`:

```python
import pygame
import sys
```

`import` loads code that your program can use. `pygame` gives you the game tools, and `sys` gives you access to Python system functions such as exiting the program.

Before using Pygame, initialize it:

```python
pygame.init()
```

`pygame.init()` prepares the Pygame modules so your program can create a window, read events, draw shapes, and use other Pygame features.

Now let's create the game window:

```python
WIDTH, HEIGHT = 960, 600
FPS = 60
WORLD_WIDTH = 3600
```

`WIDTH` and `HEIGHT` describe the size of the game window.

`FPS` represents frames per second. The game uses this value to control how quickly the game loop runs.

`WORLD_WIDTH` describes the width of the game world. The game world is wider than the visible window, which allows the player to explore by moving from left to right.

### Variables and Player Settings

Create *variables* for the player movement and physics settings:

```python
PLAYER_SIZE = 34
MOVE_SPEED = 5
JUMP_SPEED = -13
GRAVITY = 0.6
```

A *variable* is a name that stores a value. For example:

`PLAYER_SIZE` stores the size of the player.

`MOVE_SPEED` controls how fast the player moves horizontally.

`JUMP_SPEED` controls how fast the player moves when jumping.

`GRAVITY` controls how fast the player starts falling down after jumping.


### Variables and Colors

Pygame colors use an RGB tuple. RGB means red, green, and blue. Each value normally ranges from `0` to `255`:

For example:

```python
SKY = (116, 190, 212)
SUN = (255, 220, 132)
CLOUD = (224, 244, 237)
HILL_FAR = (103, 166, 151)
HILL_NEAR = (72, 135, 119)
GROUND = (50, 77, 68)
PLATFORM_TOP = (226, 183, 91)
PLATFORM_SIDE = (157, 103, 61)
PLAYER_COLOR = (239, 91, 91)
PLAYER_FACE = (255, 232, 188)
INK = (35, 45, 48)
```

You can create your own colors and use them throughout your game. Enter to this free RGB Calculator([RGB Calculator](https://www.w3schools.com/colors/colors_rgb.asp)) and find the code for your favorite colors. Try changing the colors and see how the appearance of your game changes.

### Game Objects: Platforms

The player needs platforms to walk and jump on. Create a function to build the platforms:

`