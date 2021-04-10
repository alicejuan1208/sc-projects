"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays the game named "Breakout".
    Players can move their mouse to control the paddle to prevent the ball from dropping out of the window.
    The brick will disappear when it's hit by the ball,
    once players clean all the bricks, they win the game.
    """
    graphics = BreakoutGraphics()

    # Life Board
    lives = NUM_LIVES
    life = GLabel(f'Life: {lives}')
    life.font = '-30'
    graphics.window.add(life, x=0, y=graphics.window.height)

    # Score Board
    score = 0
    score_board = GLabel(f'Score: {score}')
    score_board.font = '-30'
    graphics.window.add(score_board, x=graphics.window.width-150, y=graphics.window.height)

    # Add animation loop here!
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    while lives > 0:
        if score == graphics.brick_rows*graphics.brick_cols:
            completed = graphics.game_completed()
            graphics.window.add(completed)
            break
        pause(FRAME_RATE)
        if graphics.start:  # Check if users have clicked or not.
            graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:  # Check if the ball has hit the wall
            dx = -dx
        elif graphics.ball.y <= 0:
            dy = -dy
        elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.start = False
            graphics.window.remove(life)
            life = GLabel(f'Life: {lives}')
            life.font = '-30'
            graphics.window.add(life, x=0, y=graphics.window.height)
            graphics.ball.x = graphics.window.width/2-graphics.ball_radius
            graphics.ball.y = graphics.window.height/2-graphics.ball_radius
            dx = graphics.get_dx()
            dy = graphics.get_dy()
        # Check if the 4 corners of the ball have hit something.
        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        obj3 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.height)
        if obj1 is not None:
            if obj1 == graphics.paddle:
                dy = -dy
                if dy > 0:
                    dy = -dy
            elif obj1 == life:
                pass
            elif obj1 == score_board:
                pass
            else:
                graphics.window.remove(obj1)
                dy = -dy
                graphics.window.remove(score_board)
                score += 1
                score_board = GLabel(f'Score: {score}')
                score_board.font = '-30'
                graphics.window.add(score_board, x=graphics.window.width - 150, y=graphics.window.height)
        elif obj2 is not None:
            if obj2 == graphics.paddle:
                dy = -dy
                if dy > 0:
                    dy = -dy
            elif obj2 == life:
                pass
            elif obj2 == score_board:
                pass
            else:
                graphics.window.remove(obj2)
                dy = -dy
                graphics.window.remove(score_board)
                score += 1
                score_board = GLabel(f'Score: {score}')
                score_board.font = '-30'
                graphics.window.add(score_board, x=graphics.window.width - 150, y=graphics.window.height)
        elif obj3 is not None:
            if obj3 == graphics.paddle:
                dy = -dy
                if dy > 0:
                    dy = -dy
            elif obj3 == life:
                pass
            elif obj3 == score_board:
                pass
            else:
                graphics.window.remove(obj3)
                dy = -dy
                graphics.window.remove(score_board)
                score += 1
                score_board = GLabel(f'Score: {score}')
                score_board.font = '-30'
                graphics.window.add(score_board, x=graphics.window.width - 150, y=graphics.window.height)
        elif obj4 is not None:
            if obj4 == graphics.paddle:
                dy = -dy
                if dy > 0:
                    dy = -dy
            elif obj4 == life:
                pass
            elif obj4 == score_board:
                pass
            else:
                graphics.window.remove(obj4)
                dy = -dy
                graphics.window.remove(score_board)
                score += 1
                score_board = GLabel(f'Score: {score}')
                score_board.font = '-30'
                graphics.window.add(score_board, x=graphics.window.width - 150, y=graphics.window.height)
    if score != graphics.brick_rows * graphics.brick_cols:  # If the live number comes to zero.
        end = graphics.game_end()
        graphics.window.add(end)




if __name__ == '__main__':
    main()
