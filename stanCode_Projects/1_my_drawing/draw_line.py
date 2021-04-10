"""
File: draw_line.py
Name: Alice
-------------------------
TODO:
This is a program of drawing straight lines. When Users click the mouse first time,
the first clicking position will appear a circle.
When users click mouse second times, the clicking position of first and second time will be linked as a line.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the circle.
SIZE = 7
oval = GOval(SIZE, SIZE)
window = GWindow()
# To save the position of the user's first click.
origin_x = 0
origin_y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(punch)


def punch(m):
    global origin_x, origin_y, oval
    # Check if it's the first/third/fifth... time of click
    if origin_x == 0 and origin_y == 0:
        oval = GOval(SIZE, SIZE, x=m.x - (SIZE / 2), y=m.y - (SIZE / 2))
        oval.color = 'black'
        window.add(oval)
        origin_x = m.x
        origin_y = m.y
    else:
        line = GLine(m.x-(SIZE/2), m.y-(SIZE/2), origin_x, origin_y)
        window.remove(oval)
        window.add(line)
        origin_x = 0
        origin_y = 0


if __name__ == "__main__":
    main()
