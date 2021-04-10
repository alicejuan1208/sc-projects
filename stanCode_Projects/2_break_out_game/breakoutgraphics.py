"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        onmousemoved(self.move)
        self.start = False
        onmouseclicked(self.click)

        # Draw bricks.
        for j in range(brick_rows):
            for i in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=0+(brick_spacing+brick_width) * i, y=brick_offset+(brick_spacing+brick_height) * j)
                self.brick.filled = True
                if j <= 1:
                    self.brick.fill_color = 'red'
                elif j <= 3:
                    self.brick.fill_color = 'orange'
                elif j <= 5:
                    self.brick.fill_color = 'yellow'
                elif j <= 7:
                    self.brick.fill_color = 'green'
                elif j <= 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

    def move(self, m):
        """
        Users can move their mouse to control the paddle.
        """
        if m.x <= self.paddle.width / 2:
            self.paddle.x = 0
        elif m.x + self.paddle.width / 2 >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = m.x - self.paddle.width / 2

    def get_dx(self):
        """
        :return: Returns a random dx as horizontal speed to make the ball move.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def get_dy(self):
        """
        :return: Returns a dy as vertical speed to make the ball move.
        """
        self.__dy = INITIAL_Y_SPEED
        return self.__dy

    def click(self, m):
        """
        Starts the breakout game if users click
        """
        self.start = True

    def game_end(self):
        word = GLabel('Game Over', x=self.window.width/2-95, y=self.window.height/2)
        word.font = '-40'
        word.color = 'red'
        return word

    def game_completed(self):
        word = GLabel('Completed!', x=self.window.width/2-95, y=self.window.height/2)
        word.font = '-40'
        word.color = 'green'
        return word

    def warning(self):
        word = GLabel('warning!', x=self.window.width/2-95, y=self.window.height/2)
        word.font = '-60'
        word.color = 'red'
        return word



