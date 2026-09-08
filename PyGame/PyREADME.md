# iFp Python Coding Practice

Welcome to iFp's Python coding practice! Over the next several sessions, you will practice Python by building your own version of the classic Pong game with Pygame.

You will begin with a simple program, then organize it into functions and a game loop. By the end, you will have a game that you can customize with your own colors, speed, rules, and graphics.

## What You'll Do

- Work with Python and the Pygame library
- Build your own version of Pong in `mypong.py`
- Practice organizing a program into functions
- Create game objects such as paddles and a ball
- Add movement, collision, scoring, and a game loop

## What You'll Learn

This project will help you:

- Improve your Python programming skills
- Understand variables, lists, conditionals, and loops
- Define and call functions with `def`
- Understand how a Python program is structured
- Use a library to create a window and draw graphics
- Respond to keyboard and window events
- Break a large problem into smaller pieces

## Your Next Step

By the time you finish, or when you feel you've made good progress, you can choose a project path to continue with:

- Game Development with Python and Pygame
- Game Development in Godot 3.5
- Web Development with JavaScript, CSS, and HTML
- AI Research and Development using Python


# Day 1-5

Navigate to VS Code in your applications and open the iFp Fall Coding Practice folder. In the `PyGame` folder, open `pong.py` to study the example. Then create a new file named `mypong.py`. You will edit `mypong.py` and use the example as a guide while making your own version of Pong.

Each section has an objective to help you understand both Python syntax and the structure of a small game. There are tips and definitions here to guide you and give you something to reference when you feel unsure. You are also encouraged to make your own decisions and research Python or Pygame documentation when you are curious or stuck. Your mentors will be available to answer questions.

## "mypong.py"

A Python file is a text file containing instructions written in the Python programming language. Python reads the instructions from top to bottom when the file runs.

Pygame is a Python library. A library is a collection of code that someone else has already written so you can use features such as windows, drawings, keyboard input, sound, and timing.

The provided `pong.py` file is a reference example. Your `mypong.py` file will contain the structure and behavior of your game. You will organize it into imports, constants, functions, game objects, and the main game loop.

### Imports and Setup

1. Open `pong.py` in VS Code and look through the example.
2. Create a new file in the same folder named `mypong.py`.
3. Open `mypong.py` in VS Code.
4. Add the imports at the top of `mypong.py`:

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

Now create the game window:

```python
WIDTH, HEIGHT = 900, 600

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
```

`WIDTH` and `HEIGHT` are constants. A constant is a value that your program treats as fixed while it runs. The uppercase names make constants easier to recognize.

`window` is the surface where the game will be drawn. A surface is an area that can contain graphics. `clock` helps control the game's frame rate.

### Variables and Colors

Create names for the colors and game settings you will use:

```python
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PADDLE_SPEED = 6
BALL_SPEED_X = 5
BALL_SPEED_Y = 4
```

Pygame colors use an RGB tuple. RGB means red, green, and blue. Each value normally ranges from `0` to `255`:

```python
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
```

A variable is a name that stores a value. For example, `PADDLE_SPEED` stores the number used when moving a paddle.

### Game Objects

Pygame uses `Rect` objects to represent rectangles. A `Rect` stores a position and a size, and it also provides useful properties such as `top`, `bottom`, `left`, `right`, and `center`.

Add the paddles and ball:

```python
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 110
BALL_SIZE = 18

left_paddle = pygame.Rect(
	40,
	HEIGHT // 2 - PADDLE_HEIGHT // 2,
	PADDLE_WIDTH,
	PADDLE_HEIGHT,
)

right_paddle = pygame.Rect(
	WIDTH - 40 - PADDLE_WIDTH,
	HEIGHT // 2 - PADDLE_HEIGHT // 2,
	PADDLE_WIDTH,
	PADDLE_HEIGHT,
)

ball = pygame.Rect(
	WIDTH // 2 - BALL_SIZE // 2,
	HEIGHT // 2 - BALL_SIZE // 2,
	BALL_SIZE,
	BALL_SIZE,
)
```

The first two values passed to `pygame.Rect` are the x and y position. The last two values are the width and height.

`//` is floor division. It divides two numbers and keeps the whole-number result. It is useful here because screen positions need to be whole pixels.

### Functions

A function is a named, reusable block of code. Functions help you organize a large program into smaller tasks.

Define a function with `def`:

```python
def reset_ball(direction):
	ball.center = (WIDTH // 2, HEIGHT // 2)
```

`direction` is a parameter. A parameter is a value that a function receives when it is called. Call the function by writing its name and parentheses:

```python
reset_ball(1)
```

The game needs to change the ball's speed, so the function can update both speed variables:

```python
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y


def reset_ball(direction):
	global ball_speed_x, ball_speed_y

	ball.center = (WIDTH // 2, HEIGHT // 2)
	ball_speed_x = direction * BALL_SPEED_X
	ball_speed_y = BALL_SPEED_Y
```

`global` tells Python that the function is changing variables created outside the function. We will later practice a structure that avoids needing `global`, but it is useful for understanding how scope works.

### Structuring the Main Function

Instead of placing the game loop at the top level of the file, put it inside a `main` function. This gives the program a clear starting point and makes the file easier to reuse.

```python
def main(window):
	clock = pygame.time.Clock()

	while True:
		# Game code goes here.
		clock.tick(60)
```

`window` is an argument containing the Pygame window. The `while True` loop repeats forever until the player closes the game or the program exits.

At the bottom of the file, create the window and call `main`:

```python
if __name__ == "__main__":
	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Pong")
	main(window)
	pygame.quit()
```

`if __name__ == "__main__":` means “run this code when this file is started directly.” It prevents the game from starting automatically if another Python file imports `mypong.py`.

### Events and Keyboard Input

Games need to check what the player is doing. Pygame stores actions such as closing the window or pressing a key as events.

Add this inside `main` and inside the `while` loop:

```python
for event in pygame.event.get():
	if event.type == pygame.QUIT:
		pygame.quit()
		sys.exit()
```

`pygame.event.get()` gets the events waiting to be handled. The `for` loop checks each event. `pygame.QUIT` happens when the player closes the window.

To read keys that are currently being held down, use `pygame.key.get_pressed()`:

```python
keys = pygame.key.get_pressed()

if keys[pygame.K_w] and left_paddle.top > 0:
	left_paddle.y -= PADDLE_SPEED

if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
	left_paddle.y += PADDLE_SPEED
```

An `if` statement runs code only when its condition is true. `and` combines conditions. The checks keep the paddle inside the window.

Try adding controls for the right paddle using `pygame.K_UP` and `pygame.K_DOWN`.

### Moving the Ball

Use the ball speed variables to update the ball's position each frame:

```python
ball.x += ball_speed_x
ball.y += ball_speed_y
```

`+=` means “add this value to the current value.” This moves the ball a small amount every frame.

Make the ball bounce off the top and bottom edges:

```python
if ball.top <= 0 or ball.bottom >= HEIGHT:
	ball_speed_y *= -1
```

`or` means at least one condition must be true. Multiplying a speed by `-1` reverses its direction.

### Collision Detection

Collision detection checks whether two objects touch or overlap. Pygame's `colliderect()` method checks whether two rectangles overlap.

```python
if ball.colliderect(left_paddle) and ball_speed_x < 0:
	ball_speed_x *= -1
```

The second condition makes sure the ball is moving toward the left paddle. Without it, the ball could collide again on the next frame and change direction repeatedly.

You can change the ball's vertical direction based on where it hits the paddle:

```python
offset = (ball.centery - left_paddle.centery) / (PADDLE_HEIGHT / 2)
ball_speed_y = offset * 6
```

`offset` describes how far the ball is from the paddle's center. A hit near the top sends the ball upward, while a hit near the bottom sends it downward.

### Scoring

Create score variables before the game loop:

```python
left_score = 0
right_score = 0
```

If the ball leaves the left side, the right player scores. If it leaves the right side, the left player scores:

```python
if ball.left <= 0:
	right_score += 1
	reset_ball(1)
elif ball.right >= WIDTH:
	left_score += 1
	reset_ball(-1)
```

`elif` means “else if.” It checks another condition only if the first `if` condition was false.

### Drawing the Game

Each frame should be drawn in this order:

1. Clear the window.
2. Draw the center line.
3. Draw the paddles and ball.
4. Draw the score.
5. Update the display.

```python
window.fill(BLACK)

for y in range(0, HEIGHT, 20):
	pygame.draw.rect(window, WHITE, (WIDTH // 2 - 2, y, 4, 10))

pygame.draw.rect(window, WHITE, left_paddle)
pygame.draw.rect(window, WHITE, right_paddle)
pygame.draw.ellipse(window, WHITE, ball)

score_text = font.render(f"{left_score}  {right_score}", True, WHITE)
window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

pygame.display.flip()
clock.tick(FPS)
```

`pygame.draw.rect()` draws a rectangle, and `pygame.draw.ellipse()` draws an oval or circle inside a rectangle. `blit()` copies one surface onto another, such as putting text on the game window.

An f-string lets you place variable values inside text. In `f"{left_score}  {right_score}"`, Python replaces the braces with the current scores.

`pygame.display.flip()` shows the completed frame. `clock.tick(FPS)` limits the game to the number of frames per second stored in `FPS`.

### Putting It Together

Your file should have a structure similar to this:

```python
import pygame
import sys


WIDTH, HEIGHT = 900, 600
FPS = 60


def reset_ball(direction):
	# Reset the ball position and speed.
	pass


def main(window):
	# Create game objects and scores.
	while True:
		# Handle events.
		# Move paddles and ball.
		# Check collisions and scoring.
		# Draw the current frame.
		pass


if __name__ == "__main__":
	pygame.init()
	window = pygame.display.set_mode((WIDTH, HEIGHT))
	main(window)
	pygame.quit()
```

`pass` is a placeholder that tells Python to do nothing for now. Replace each `pass` with the code you build during the lesson.

Things to remember:

- Use four spaces for each indentation level.
- A colon `:` begins the indented block after a function, loop, or condition.
- Keep related code together inside functions.
- Use clear names such as `left_paddle` instead of unclear names such as `x`.
- Run the file often so you can find errors while the change is still small.

## "Test your knowledge"

Now that you have practiced the structure of a Pygame program, keep improving your Pong game. Try changing one part at a time and test after each change.

### "Pong Assignment"

This challenge will help you use the Python and Pygame skills from this lesson. Build your own Pong game in `mypong.py`. You should use functions to organize the setup, input, movement, collisions, scoring, and drawing.

For this assignment, do not edit the provided `pong.py` example. Work in your own `mypong.py` file. You can use `pong.py` and the examples above as guides, but your game should include your own choices for colors, speed, text, and rules.

### "mypong.py"

Your game should include:

1. A Pygame window with a title.
2. A left paddle and a right paddle.
3. A ball that moves around the screen.
4. Keyboard controls for both paddles.
5. Bounces from the top and bottom edges.
6. Paddle collision detection.
7. A score for each player.
8. A function that resets the ball after a point.
9. A `main(window)` function containing the game loop.
10. A `if __name__ == "__main__":` entry point.

Example function structure:

```python
def reset_ball(direction):
	pass


def handle_events():
	pass


def move_paddles(keys):
	pass


def move_ball():
	pass


def draw_game(window):
	pass


def main(window):
	while True:
		# Call the smaller functions here.
		pass
```

The names are suggestions. You may organize your functions differently as long as your structure is easy to understand.

### "Your Challenge"

Try to complete these goals:

- Change the game colors and window title.
- Add a start screen before the game begins.
- Add a winning score, such as first player to 5 points.
- Display a message when someone wins.
- Add a pause key.
- Make the ball speed increase after each paddle hit.
- Add a second ball or a power-up.
- Replace the simple shapes with your own artwork.
- Keep the game loop readable by moving repeated tasks into functions.

Remember: the goal is not only to make the game run. The goal is to understand why it runs and how the pieces of the Python program fit together.
