import pyglet
from pyglet.shapes import Rectangle

from .constants import WIDTH


class Player(Rectangle):
    def __init__(self, x, y, ground, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.x = x
        self.y = y
        self.event_handlers = [self, self.key_handler]
        self.ground = ground
        self.max_jump_height_reached = False

    def update(self, dt):
        # movements
        if self.key_handler[pyglet.window.key.A]:
            self.x -= 250 * dt

        if self.key_handler[pyglet.window.key.D]:
            self.x += 250 * dt

        # jump logic
        if self.key_handler[pyglet.window.key.W]:
            self.y += 250 * dt if not self.max_jump_height_reached else 0

        if self.y - self.ground > 100:
            self.max_jump_height_reached = True
        if self.y - self.ground <= 0:
            self.max_jump_height_reached = False

        self.y -= (
            250 * dt
            if (self.y - self.ground > 0 and not self.key_handler[pyglet.window.key.W])
            or self.max_jump_height_reached
            else 0
        )

        # restriction to leave screen
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

        if self.x < 0:
            self.x = 0
