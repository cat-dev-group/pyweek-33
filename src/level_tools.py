import pyglet
from .player import Player


class platform(pyglet.shapes.Rectangle):
    def __init__(self, x, y, width, color, alignment="h"):
        if alignment == "h":
            height = 10
        else:
            height = width
            width = 10

        super().__init__(x, y, width=width, height=height, color=color)
        self.on_platform = False
        self.a = alignment
        Player.entities["platform"][x, y] = self

    def collision_check(other, self):
        if (
            (other.x < self.x + self.width)
            and (other.x + other._width > self.x)
            and (other.y < self.y + self.height)
            and (other.y + other._height > self.y)
        ):
            return True
        return False


class flag:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.batch = pyglet.graphics.Batch()
        self.parts = (
            pyglet.shapes.Rectangle(
                self.x,
                self.y,
                width=10,
                height=30,
                color=(165, 42, 42),
                batch=self.batch,
            ),
            pyglet.shapes.Rectangle(
                self.x,
                self.y + 30,
                width=50,
                height=30,
                color=(255, 0, 0),
                batch=self.batch,
            ),
        )

        Player.entities["flag"][x, y] = self.batch

    def draw(self):
        self.batch.draw()

    def collision_check(flag_, other):
        if any(
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
            for self in flag_.parts
        ):
            return True


class button:
    def __init__(self, x, y, on_trigger, off_trigger):
        self.x = x
        self.y = y
        self.state = False
        self.on_trigger = on_trigger
        self.off_trigger = off_trigger
        self.batch = pyglet.graphics.Batch()
        self.parts = (
            pyglet.shapes.Rectangle(
                self.x + 10,
                self.y - 10,
                width=12,
                height=40,
                color=(128, 128, 128),
                batch=self.batch,
            ),
            pyglet.shapes.Rectangle(
                self.x, self.y, width=15, height=22, color=(255, 0, 0), batch=self.batch
            ),
        )
        Player.entities["button"][x, y] = self.batch

    def collision_check(self, other):
        self = self.parts[1]
        if (
            self.x < other.x + other.width
            and self.x + self.width > other.x
            and self.y < other.y + other.height
            and self.y + self.height > other.y
        ):
            return True

    def draw(self):
        self.batch.draw()

    def update(self, dt):
        for i in Player.entities['players'].values():
            if self.collision_check(i):
                if not i.button_pressed:
                    if not self.state:
                        self.on_trigger()
                    else:
                        self.off_trigger()
                    self.state = not self.state
                    self.parts[1].color = (0, 255, 0) if self.state else (255, 0, 0)
                    i.button_pressed = True

            else:
                i.button_pressed = False
# class spike(pyglet.shapes.Triangle):
#     def __init__(self, x, y, color=(0, 0, 0)):
#         super().__init__(x, y, x + 30, y, x + 15, y + 30, color=color)
#         Player.entities["spike"][x, y] = self

#     def collision_check(self, other):
#         if (
#             self.x < other.x + other.width
#             and self.x + self.width > other.x
#             and self.y < other.y + other.height
#             and self.y + self.height > other.y
#         ):
#             return True
