from pathlib import Path

import pyglet

from .constants import HEIGHT, WIDTH


class Pause(pyglet.shapes.Rectangle):
    def __init__(self, x, y, width, height, *args, **kwargs):
        super().__init__(x, y, width, height, *args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.anchor_x = width // 2
        self.anchor_y = height // 2


menu_batch = pyglet.graphics.Batch()

image_path = Path("src/resources/test.png")
test = pyglet.image.load(image_path)
image_path_1 = Path("src/resources/test1.png")
test1 = pyglet.image.load(image_path_1)


pause = Pause(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    width=800,
    height=600,
    color=(100, 0, 100),
    batch=menu_batch
)


resume = pyglet.gui.ToggleButton(
    x=WIDTH // 2 - 100,
    y=HEIGHT // 2,
    pressed=test,
    depressed=test1,
    batch=menu_batch
)
