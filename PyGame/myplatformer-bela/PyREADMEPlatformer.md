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
Download and install [Python](https://www.python.org/downloads/) on your computer. 

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

### Imports

1. Open `platformer.py` in VS Code and look through the example.
2. Create a new file in the same folder named `myplatformer.py`.
3. Open `myplatformer.py` in VS Code.
4. Add the imports at the top of `myplatformer.py`:

```python
import pygame
import sys
```

`import` loads code that your program can use. `pygame` gives you the game tools, and `sys` gives you access to Python system functions such as exiting the program.

### Creating our game window

```python
WIDTH, HEIGHT = 960, 600
FPS = 60
WORLD_WIDTH = 3600
```

`WIDTH` and `HEIGHT` describe the size of the game window.

`FPS` represents frames per second. The game uses this value to control how quickly the game loop runs.

`WORLD_WIDTH` describes the width of the game world. The game world is wider than the visible window, which allows the player to explore by moving from left to right.

### Adding more variables for our player and the game world

Create *variables* for the player movement:

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

You can create your own colors and use them throughout your game. Enter to this free [RGB Calculator](https://www.w3schools.com/colors/colors_rgb.asp) and find the code for your favorite colors. Change one color at a time and run your game to see what happens!

### Initial Pygame setup

To start running our game before we add functions we need to make sure Pygame library is set up.

```python
pygame.init()
pygame.display.set_caption("My Platform Game")
clock = pygame.time.Clock
```

`pygame.init()` prepares the Pygame modules to create a window, draw graphics, etc.

`pygame.display.set_caption("Change me!")`changes the title of the game window.

`clock` creates a Pygame clock that helps control how fast the game runs.


### Game Objects: Platforms

The player needs platforms to walk and jump on. We can create our platforms using `Rect`. Pygame uses `Rect` objects to represent rectangles.

Each `pygame.Rect()` has four important values.
For example:

`pygame.Rect(420, 430, 180, 22)`

Which means:

`420` → x position
`430` → y position
`180` → width
`22` → height

We have several platforms to create (which meand several Rectangules!), so instead of writing all of the platform code directly inside the main game loop, we group it together in a *function* called `make_platforms()`:

```python
def make_platforms():
    return [
        pygame.Rect(0, 530, 720, 70),
        pygame.Rect(800, 530, 620, 70),
        pygame.Rect(1510, 530, 720, 70),
        pygame.Rect(2320, 530, 1280, 70),
        pygame.Rect(420, 430, 180, 22),
        pygame.Rect(960, 390, 190, 22),
        pygame.Rect(1240, 470, 150, 22),
        pygame.Rect(1660, 410, 210, 22),
        pygame.Rect(1980, 330, 180, 22),
        pygame.Rect(2470, 420, 210, 22),
        pygame.Rect(2860, 350, 180, 22),
        pygame.Rect(3200, 455, 190, 22),
    ]
```

This function creates all of the platforms and returns them as a list.

### Game Objects: Player

Now that we have the world game, let's create a function to draw our player.

```python
def draw_player(surface, player_rect, camera_x):
    screen_rect = player_rect.move(-camera_x, 0)
    pygame.draw.ellipse(surface, PLAYER_COLOR, screen_rect)
    pygame.draw.circle(surface, PLAYER_FACE, (screen_rect.centerx, screen_rect.top + 13), 10)
    pygame.draw.circle(surface, INK, (screen_rect.centerx - 4, screen_rect.top + 12), 2)
    pygame.draw.circle(surface, INK, (screen_rect.centerx + 4, screen_rect.top + 12), 2)
```

The player is currently made from simple shapes.

`pygame.draw.ellipse()` draws the player's body.

`pygame.draw.circle()` draws the face and eyes.

The player does not have to look like this! Later, you can replace these shapes with your own artwork or sprites.

Notice that we are using the color variables we created earlier, such as `PLAYER_COLOR`, `PLAYER_FACE`, and `INK`.
This means we don't have to write the RGB values every time we draw something. If you want a different color for the player, you only need to change the value of the variable at the beginning of your program, and the new color will be used everywhere that variable is called.

This is one of the **advantages of using variables**: *instead of changing the same value in many different places, we can change it once and reuse it throughout our program.*

You may notice something new here:

`player_rect.move(-camera_x, 0)`

The player's actual position exists in the larger game world. `camera_x` tells us how far the camera has moved.

We will learn more about the camera later!

