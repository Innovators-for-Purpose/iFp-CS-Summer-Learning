# iFp Python Coding Practice: Platform game!

Welcome to iFp's Python coding practice 2! In this session you will practice Python by building your own version of a platform game with Pygame.

## What you'll do

- Build your own version of a platform game in `myplatformer.py`
- Create a player and platforms
- Add keyboard controls and jumping
- Add gravity and collision detection
- Create a scrolling screen for the game

## What you'll learn

Work on this project will help you to:

- Improve your Python programming skills
- Understand variables, constants and lists
- Respond to keyboard and window events
- Use conditionals and loops
- Break a large problem into smaller functions

This tutorial is part of the **Game Development with Python and Pygame** iFp curriculum.

## Before start coding

We need to make sure we have the following install in our computer:

**Step 1: Install Python**
Download and install [Python](https://www.python.org/downloads/) on your computer. 

After installing Python, open your VS Code terminal and check that it works:

`python3 --version`

You should see a Python version number.

**Step 2: Install Pygame**

Pygame is the Python library we will use to create the game.
Open your terminal and run:

`python3 -m pip install pygame`

## Start coding!

Navigate to Visual Studio Code in your applications and clone the iFp Fall Coding Practice folder from the iFp Github repository. In the `PyGame` folder, open `platformer.py` to study the example. Then create a new folder named `myplatformer_NameOfStudent`. We will create here our version of the game.

Each section has an objective to help you understand both Python syntax and the structure of a small game. You are also encouraged to make your own decisions and research Python or Pygame documentation when you are curious or stuck. Your mentors will be available to answer questions.

### `myplatformer.py`

The provided `platformer.py` file is a reference example. Your `myplatformer.py` file will contain the structure and behavior of your game. You will organize it into imports, constants, functions, game objects, and the main game loop.

### Imports

1. Open `platformer.py` in VS Code and look through the example.
2. Create a new folder named `myplatformer_NameOfStudent`.
3. Create a file in the same folder named `myplatformer.py`.
4. Open `myplatformer.py` in VS Code.
5. Add the folling imports at the top of `myplatformer.py`:

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

You can create your own colors and use them throughout your game. Enter to this free [RGB Calculator](https://www.w3schools.com/colors/colors_rgb.asp) and find the code for your favorite colors. 

*After you declare the main() function*: Change one color at a time and run your game to see what happens!

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

At this point, we can try running our game. You may see the game window trying to open, but there is **nothing to see yet** because we haven't defined our `main()` function or drawn any of the game objects.

Don't worry! That's expected. In the end of our tutorial, we'll create our `main()` function and start putting the different parts of our game together.

### Game Objects: Platforms

The player needs platforms to walk and jump on. We can create our platforms using `Rect`. Pygame uses `Rect` objects to represent rectangles. Each `pygame.Rect()` has four important values.

For example:

`pygame.Rect(420, 430, 180, 22)`

Which means:

`420` → x position
`430` → y position
`180` → width
`22` → height

We have several platforms to create (which means several Rectangules!), so instead of writing all of the platform code directly inside the main game loop, we group it together in a *function* called `make_platforms()`:

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

### Game Objects: Background

We already created our platforms and player but our background has no color or design. We need to draw a background.

```python
def draw_background(surface, camera_x):
    surface.fill(SKY)
    pygame.draw.circle(surface, SUN, (WIDTH - 110, 90), 48)
```

Let's start with something basic:
`surface.fill(SKY)` fills the entire game window with the sky color.
`pygame.draw.circle()` creates the sun.
Inside of your `draw_background` function, let's add some clouds:

```python
for cloud_x, cloud_y in ((150, 105), (540, 170), (830, 90)):
    x = cloud_x - int(camera_x * 0.15) % (WIDTH + 240)
    pygame.draw.circle(surface, CLOUD, (x, cloud_y), 25)
    pygame.draw.circle(surface, CLOUD, (x + 28, cloud_y - 10), 34)
    pygame.draw.circle(surface, CLOUD, (x + 60, cloud_y), 25)
```   
We are using a for loop so we can draw a lot of clouds.

With: `x = cloud_x - int(camera_x * 0.15) % (WIDTH + 240)` The clouds move more slowly than the player. This makes the background look like it is farther away.

To finish with our basic background let's create some hills inside of our `draw_background` function.

```python
for offset, color, height in ((0.18, HILL_FAR, 110), (0.32, HILL_NEAR, 160)):
    points = [(-200, HEIGHT), (-200, HEIGHT - height)]
    for world_x in range(-200, WORLD_WIDTH + 400, 260):
        screen_x = world_x - int(camera_x * offset)
        points.extend(((screen_x, HEIGHT - height), (screen_x + 130, HEIGHT - height - 85), (screen_x + 260, HEIGHT - height)))
    points.append((WIDTH + 200, HEIGHT))
    pygame.draw.polygon(surface, color, points)

```

I know this code make look pretty big and confusing so let's explain it little by little.

First, we have:

```python
for offset, color, height in ((0.18, HILL_FAR, 110), (0.32, HILL_NEAR, 160))
 ```
Here we are creating two groups of hills. For each group, we give the hills three values:

The `offset` controls how much the hills move when the camera moves.
The `color` tells us what color to use for the hills.
The `height` controls how tall the hills are.

The farther hills use a smaller offset, so they move more slowly when the camera moves. This helps make the background look farther away.

Next, we create our `points` list:

```python
points = [(-200, HEIGHT), (-200, HEIGHT - height)]
```
This list will store the different points we need to create the shape of our hills.

Each point has an `x` and a `y` position. We will keep adding points to this list as we create more hills.

Now let's look at this for loop:

```python
for world_x in range(-200, WORLD_WIDTH + 400, 260):
```

We use `world_x` to help decide where to create each hill. Inside the loop, we calculate the position of the hill on the screen:

```python
screen_x = world_x - int(camera_x * offset)
```
camera_x tells us how far the camera has moved.

By multiplying `camera_x` by `offset`, we can make the hills move at different speeds depending on how far away they appear.

Then we add three points for each hill:

```python
points.extend((
    (screen_x, HEIGHT - height),
    (screen_x + 130, HEIGHT - height - 85),
    (screen_x + 260, HEIGHT - height)
))
```

These three points are:
- The start of the hill.
- The top of the hill.
- The end of the hill.

Finally, we add a point at the bottom of the screen:

```python
points.append((WIDTH + 200, HEIGHT))
```

Then we add:

```python
pygame.draw.polygon(surface, color, points)
```
This connect all of our points and fill the shape with the color we chose.

### Movement: Making the player move horizontally

We finish creating our platforms, player and background but our player can't move yet on the game world. Let's create a function to help the player move!

```python
def move_player(player, velocity, platforms):
    player.x += velocity.x
    player.x = max(0, min(player.x, WORLD_WIDTH - PLAYER_SIZE))
    for platform in platforms:
        if player.colliderect(platform):
            if velocity.x > 0:
                player.right = platform.left
            elif velocity.x < 0:
                player.left = platform.right

    velocity.y += GRAVITY
    player.y += velocity.y
    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if velocity.y > 0:
                player.bottom = platform.top
                velocity.y = 0
                on_ground = True
            elif velocity.y < 0:
                player.top = platform.bottom
                velocity.y = 0
    return on_ground
```
Let's create our function:

```python
def move_player(player, velocity, platforms):
```
The function receives three things:

- `player` the player's Rect that we created at the beginning of our program that represent the  position and size of our player.
- `velocity` how fast the player is moving.
- `platforms` the list of platforms

First, move the player horizontally: `player.x += velocity.x`

We also want to keep the player inside the game world:

`player.x = max(0, min(player.x, WORLD_WIDTH - PLAYER_SIZE))`

This prevents the player from moving beyond the left or right edges of the world.

### Movement: Making sure the player don't collide with platforms

Let's start with:

```python
for platform in platforms:
    if player.colliderect(platform):
        if velocity.x > 0:
            player.right = platform.left
        elif velocity.x < 0:
            player.left = platform.right
```

`colliderect()` checks whether two rectangles overlap.
This code checks whether the player is moving right or left.
If the player is moving right: `player.right = platform.left` moves the player back to the left side of the platform.
If the player is moving left: `player.left = platform.right` moves the player back to the right side of the platform.

This prevents the player from walking through platforms.

### Movement: Making the player jump!

First, increase the player's vertical velocity:

```python
velocity.y += GRAVITY
```

This is what creates the effect of gravity. If the player is moving up, gravity gradually makes the upward movement slower. When the player starts to fall, the player's vertical velocity becomes positive.

Then move the player: `player.y += velocity.y`

Now check whether the player has landed on a platform:

```python
on_ground = False

for platform in platforms:
    if player.colliderect(platform):
        if velocity.y > 0:
            player.bottom = platform.top
            velocity.y = 0
            on_ground = True
```

When `velocity.y > 0`, the player is moving down.

If the player hits a platform while moving down: `player.bottom = platform.top` places the player directly on top of the platform. And `velocity.y = 0` stops the down movement.

Finally: `on_ground = True` records that the player is standing on a platform. We also need to handle hitting the bottom of a platform while jumping:

```python
elif velocity.y < 0:
    player.top = platform.bottom
    velocity.y = 0
```

When the player is moving up and hits the bottom of a platform, the player stops moving up. At the end of the function, return whether the player is standing on the ground: `return on_ground`

### Structuring the Main Function

Our game has a lot of code, so we can organize it into functions. Let's put the code that runs our game inside a function called `main()`.

### Main Function: Variables

The `main()` function will contain the game loop and will bring together the different parts we created for our game. We will then call `main()` at the bottom of our file to start the game.

```python
def main(window):
    platforms = make_platforms()
    player = pygame.Rect(100, 470, PLAYER_SIZE, PLAYER_SIZE)
    velocity = pygame.Vector2(0, 0)
    camera_x = 0
    on_ground = False
    won = False
    font = pygame.font.Font(None, 28)
    big_font = pygame.font.Font(None, 46)
```

- `platforms` stores our list of platforms (yes! the list we created earlier in our program!).

- `player` stores the player's position and size.

- `velocity` stores how fast the player is moving horizontally and vertically.

- `camera_x` stores the camera's horizontal position.

- `on_ground` keeps track of whether the player is standing on something.

- `won` keeps track of whether the player has reached the end.

Games need a loop that repeats many times every second. A typical game loop has three major jobs:

- Check what the player is doing.
- Update the game.
- Draw the new frame.

```python
while True:
    # We will add the code here little by little.
```

Everything inside this loop will happen over and over while the game is running. All the following steps are happening inside the `while True` loop.

### Main Function: Events

Our game needs to know when the player does something, like closing the game window or pressing a key.

These actions are called events in Pygame, We can check these actions using `pygame.event.get()`.

Add this inside the game loop:

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
```
The `for` loop goes through each action one at a time. `pygame.QUIT` happens when the player closes the game window.

### Main Function: Jump

Now let's make make our player jump everytime we press specific keyboard keys. Inside our `for event in pygame.event.get()` and after the end of our `if event.type == pygame.QUIT` let's add:

```python
if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP):
    if on_ground and not won:
        velocity.y = JUMP_SPEED
```

`pygame.KEYDOWN` means that a key was pressed.

The player can jump using the following keys:
- `SPACE`
- `W`
- `the UP arrow`

The player can only jump if: `on_ground` is True. This prevents the player from continuously jumping in the air.
The line: `velocity.y = JUMP_SPEED` gives the player an upward velocity. Remember that our jump speed is negative: `JUMP_SPEED = -13`
In Pygame, smaller `y` values are higher on the screen, so a negative vertical velocity moves the player up.

### Main Function: Re-start the game

Let's give the player a restart key. Add the following code after the end of our `if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_w, pygame.K_UP)`:

```python
if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
    player.topleft = (100, 470)
    velocity.update(0, 0)
    won = False
```
When the player presses the key `R`:

- The player returns to the starting position.
- The velocity is reset.
- The win state is reset.

Try adding another key that does something interesting!

### Main Function: Left and Right Keys

We can check which keys are currently being held down:

```python
keys = pygame.key.get_pressed()
```

Now use the keys to control horizontal movement:

```python
velocity.x = (
    (keys[pygame.K_d] or keys[pygame.K_RIGHT]) * MOVE_SPEED - (keys[pygame.K_a] or keys[pygame.K_LEFT]) * MOVE_SPEED
)
```

The player can use:
- `A` or `the left arrow` to move left
- `D` or the `right arrow` to move right

The result is stored in `velocity.x`

### Main Function: Player status

Now let's update the player's status inside the game loop. We want to check three things:

1. Is the game still going?
2. Did the player fall off the screen?
3. Did the player reach the end of the world?

First, check if the player has not won yet:

```python
if not won:
    on_ground = move_player(player, velocity, platforms)
```

`not won` means that the game will continue updating the player as long as the player has not reached the goal.

`move_player()` moves the player and checks for collisions with the platforms. It also returns whether the player is standing on a platform, which we save in `on_ground`.

Let's check what happens if the player misses a platform and falls:

```python
    if player.top > HEIGHT:
        player.topleft = (100, 470)
        velocity.update(0, 0)
```

If the top of the player goes below the height of the game window, we know the player has fallen off the screen.

Instead of ending the game, we reset the player: 
- `player.topleft = (100, 470)` moves the player back to the starting position.
- `velocity.update(0, 0)` stops the player's movement.

Finally, let's check if the player has won:

```python
    if player.right >= WORLD_WIDTH - 180:
        won = True
```

Our game world is wider than the screen, so we need a way to know when the player has reached the end. When the player's right side gets close to the end of the world, `won` becomes `True`.

### Main Function: Scrolling Camera

Our game world is 3600 pixels wide, but the window is only 960 pixels wide. We don't want the player to disappear off the screen when they move to the right.

Instead, the camera follows the player:

```python
camera_x = max(0, min(player.centerx - WIDTH // 2, WORLD_WIDTH - WIDTH))
```

The camera tries to keep the player near the center of the screen `WIDTH // 2` finds half of the window width. The `max()` and `min()` functions keep the camera from moving beyond the edges of the game world.

### Main Function: Platforms

Now we need to draw the platforms.

```python
draw_background(window, camera_x)
for platform in platforms:
    visible = platform.copy().move(-camera_x, 0)
    pygame.draw.rect(window, PLATFORM_SIDE, visible)
    pygame.draw.rect(window, PLATFORM_TOP, (visible.x, visible.y, visible.width, 7))
```

`-camera_x` makes the platforms appear to move as the camera follows the player. We draw two rectangles to create one platform:

`PLATFORM_SIDE` is the rectangle for the side.
`PLATFORM_TOP` is the smaller rectangle for the top.

This gives the platforms a little more visual detail.

### Main Function: Player

Now let's draw the player:

```python
draw_player(window, player, camera_x)`
```

The `draw_player()` function uses the camera position to decide where the player should appear on the screen.

This is another example of **why functions are useful**: instead of writing all of the drawing code inside the game loop, we can simply call the function we already created.

### Main Function: Game Instructions

We can display text on the screen to remind the player about the game controls:

```python
hint = font.render("A / D or arrows: move    SPACE: jump    R: restart", True, INK)
window.blit(hint, (22, 20))
```

`font.render()` creates an image containing the text.
`window.blit()` places that image onto the game window.

### Main Function: Winning Message

If the player reaches the end and wins, show a message:

```python
if won:
    message = big_font.render("You made it!", True, INK)
    window.blit(message, (WIDTH // 2 - message.get_width() // 2, 76))
```

The `if won` condition means this code only runs after the player wins.
`WIDTH // 2 - message.get_width() // 2` helps center the message horizontally.

### Main Function: Refreshing the Screen

At the end of every game loop, update the display:

```python
pygame.display.flip()
clock.tick(FPS)
```

`pygame.display.flip()` shows the completed frame on the screen.
`clock.tick(FPS)` controls how fast the game loop runs.

### Run the game!

We finish our main function. Now let's run the game!

```python
if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main(window)
```

`if __name__ == "__main__"` runs the game when this file is opened directly.
`pygame.display.set_mode()` creates the game window.
`main(window)` starts the main game loop.

### Putting It Together

Your `myplatformer.py` file should now contain:

1. Imports
2. Game settings and constants
3. Colors
4. Pygame setup
5. A function for creating platforms
6. A function for drawing the player
7. A function for drawing the background
8. A function for moving the player
9. A main() function containing the game loop

For the final step, run your `myplatformer.py` and play the game!

**Congrats! You made it!!!**

### Your Challenge

- Change the game colors and window title.
- Add a start screen before the game begins.
- Add a pause key.
- Add an object to power-up the player.
- Replace the simple shapes with your own artwork.
- Keep the game loop readable by moving repeated tasks into functions.

Remember: the goal is not only to make the game run. The goal is to understand why it runs and how the pieces of the Python program fit together.
