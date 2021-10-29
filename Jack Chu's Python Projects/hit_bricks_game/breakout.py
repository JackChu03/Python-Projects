"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Jack Chu

DESCRIPTION:
To create a game that the ball will hit the bricks, when bricks are all disappear, and the game
will be over! Use the paddle to control the ball to hit the bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # get velocity x & y from coder
    dx = graphics.get_dx()
    dy = graphics.get_dy()
    # Add animation loop here!
    while True:
        r = graphics.ball_r
        # the following four points are game's ball's four edge
        m_obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        m_obj2 = graphics.window.get_object_at(graphics.ball.x+r, graphics.ball.y)
        m_obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+r)
        m_obj4 = graphics.window.get_object_at(graphics.ball.x+r, graphics.ball.y + r)
        if graphics.n >= 1 and graphics.k != NUM_LIVES and graphics.brick_n != 0:
            # to allow click move, lose when limited life is over, over when bricks are all disappear
            graphics.ball.move(dx, dy)
            # if bounce to the edge, then bounce back
            if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy
            # if hit paddle, then bounce up
            if graphics.hit_paddle():
                dy = -dy
            # if want to fastly save the ball when ball is pass the paddle
            if graphics.hit_paddle_down():
                dy = -dy
                dx = -dx
            # if get bricks successfully, then remove them
            if m_obj1 is not None and m_obj1 != graphics.paddle:
                graphics.window.remove(m_obj1)
                graphics.brick_n = graphics.brick_n - 1
                dy = -dy
            elif m_obj2 is not None and m_obj2 != graphics.paddle:
                graphics.window.remove(m_obj2)
                graphics.brick_n = graphics.brick_n - 1
                dy = -dy
            elif m_obj3 is not None and m_obj3 != graphics.paddle:
                graphics.window.remove(m_obj3)
                graphics.brick_n = graphics.brick_n - 1
                dy = -dy
            elif m_obj4 is not None and m_obj4 != graphics.paddle:
                graphics.window.remove(m_obj4)
                graphics.brick_n = graphics.brick_n - 1
                dy = -dy
            # if hit bottom edge, die, lose a life, and restart the game
            if graphics.ball.y >= graphics.window.height:
                graphics.k = graphics.k + 1
                graphics.reset()
                graphics.n = 0
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()


