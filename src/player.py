import pyglet
from .constants import WIDTH
from pyglet.shapes import Rectangle


class Player(Rectangle):
    left_col, right_col = False, False
    entities = {"platform": {}, "button": {}, "flag": {}, "spike": {}, "players": {}}

    def __init__(self, x, y, ground, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.x = x
        self.y = y
        self.event_handlers = [self, self.key_handler]
        self.ground = ground
        self.max_jump_height_reached = False
        self.relative_rest = self.ground
        self.max_jump_height = 100
        self.button_pressed = False
        Player.entities["players"][self] = self

    @property
    def on_platform(self):
        return any(i.on_platform for i in Player.entities["platform"].values())

    def update(self, dt):
        for i in Player.entities["platform"].values():
            if i.collision_check(self):
                if (
                    self.y < i.y + i._height / 2 < self.y + self.height
                    if i.a == "h"
                    else True
                ):
                    if self.x < i.x:
                        Player.left_col = True
                        break
                    elif self.x > i.x:
                        Player.right_col = True
                        break
                elif self.y > i.y:
                    i.on_platform = True
                    self.relative_rest = self.y
                    self.max_jump_height_reached = False
                else:
                    self.max_jump_height_reached = True
            else:
                i.on_platform = False
        else:
            Player.left_col = False
            Player.right_col = False

        # movements
        if self.key_handler[pyglet.window.key.A]:
            self.x -= 250 * dt * (not Player.right_col)

        if self.key_handler[pyglet.window.key.D]:
            self.x += 250 * dt * (not Player.left_col)

        # jump logic
        if self.key_handler[pyglet.window.key.W]:
            self.y += 250 * dt if not self.max_jump_height_reached else 0

        if self.y - self.relative_rest > self.max_jump_height:
            self.max_jump_height_reached = True
        if self.y - self.ground <= 0:
            self.y = self.ground
            self.max_jump_height_reached = False

        if self.y - self.relative_rest <= 0 and not self.on_platform:
            self.relative_rest = self.ground

        # restriction to leave screen
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

        if self.x < 0:
            self.x = 0

        if (
            (self.y - self.ground > 0 and not self.key_handler[pyglet.window.key.W])
            or self.max_jump_height_reached
        ) and not self.on_platform:
            self.y -= 250 * dt
        for i in Player.entities["spike"].values():
            if i.collision_check(self):
                print("You died")
                # pyglet.app.exit()
