"""
File: bouncing_ball.py
Name: Alice
-------------------------
TODO:
Once the user clicks the mouse, the ball will start bouncing to right way several times.
When the ball leave at the right of the window, it will appear again at the initial position.
This action can be executed three times. After that, clicking mouse can't trigger the action anymore.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
# The initial position of the ball
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
# Create a ball at the initial position
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'black'
window.add(ball)
# Calculate the time of the ball finish bouncing
t = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(punch)


def punch(m):
    global ball, t
    # Check if the ball is at the initial position
    origin_ball = window.get_object_at(START_X + (SIZE/2), START_Y + (SIZE/2))
    if origin_ball is not None:
        all_gravity = GRAVITY
        while t < 3:
            ball.move(VX, all_gravity)
            all_gravity = GRAVITY + all_gravity
            pause(DELAY)
            if ball.y >= 500:
                all_gravity = -all_gravity * REDUCE
                if all_gravity > 0:
                    all_gravity = -all_gravity
            elif ball.x >= 800:
                ball.x = START_X
                ball.y = START_Y
                t += 1
                break


if __name__ == "__main__":
    main()
