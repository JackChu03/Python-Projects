"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Name: Jack Chu

DESCRIPTION:
To set up the environment of the break out game
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

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING
                 , title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        # I Var(self.n) controls the start of the game, I Var(self.k) controls the limited life
        self.n = 0
        self.k = 0
        self.ball_r = ball_radius
        self.brick_n = brick_rows * brick_cols
        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
            self.__dy = -self.__dy
        # Initialize our mouse listeners

        def start(jack):
            self.n = self.n + 1

        onmouseclicked(start)

        def move_paddle(jack):
            if self.paddle.width/2 <= jack.x < self.window.width-self.paddle.width/2:
                self.window.add(self.paddle, x=jack.x-self.paddle.width/2, y=self.window.height - self.paddle_offset)
        onmousemoved(move_paddle)

        # Draw bricks
        x_spot = 0
        y_spot = brick_offset
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                brick.filled = True
                if 0 <= i <= 2:
                    brick.fill_color = 'red'
                    brick.color = 'red'
                if 3 <= i <= 5:
                    brick.fill_color = 'yellow'
                    brick.color = 'yellow'
                if 6 <= i <= 8:
                    brick.fill_color = 'blue'
                    brick.color = 'blue'
                if i == 9:
                    brick.fill_color = 'green'
                    brick.color = 'green'
                self.window.add(brick, x=x_spot, y=y_spot)
                x_spot = x_spot + brick.width + brick_spacing
            x_spot = 0
            y_spot = y_spot + brick_height + brick_spacing

    # getter
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reset(self):
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)

    def hit_paddle(self):
        x = self.ball.x > self.paddle.x - self.ball_r
        y = self.ball.x < self.paddle.x+self.paddle.width + self.ball_r
        z = self.ball.y + self.ball_r > self.window.height - self.paddle_offset
        return x and y and z

    def hit_paddle_down(self):
        x = self.ball.x > self.paddle.x - self.ball_r
        y = self.ball.x < self.paddle.x + self.paddle.width + self.ball_r
        z = self.ball.y > self.window.height - self.paddle_offset
        return x and y and z































































