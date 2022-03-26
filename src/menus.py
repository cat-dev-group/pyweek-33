import pyglet

from .constants import HEIGHT, WIDTH

menu_batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)
foreground = pyglet.graphics.OrderedGroup(1)


class Text(pyglet.text.Label):
    def __init__(self, text, size, x, y, edits=1, *args, **kwargs):
        super().__init__(
            text,
            font_name="comic sans",
            font_size=size,
            x=x,
            y=y,
            anchor_x="center",
            anchor_y="center",
        )


class Pause(pyglet.shapes.Rectangle):
    def __init__(self, x, y, width, height, *args, **kwargs):
        super().__init__(x, y, width, height, *args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.anchor_x = width // 2
        self.anchor_y = height // 2


pause_text = Text(
    text="Press 'P' to pause",
    size=20,
    x=WIDTH // 2,
    y=round(HEIGHT * 0.05),
    batch=menu_batch,
    group=foreground
)

resume_text = Text(
    text="Press 'P' to resume",
    size=20,
    x=WIDTH // 2,
    y=HEIGHT // 2,
    batch=menu_batch,
    group=foreground
)

pause = Pause(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    width=800,
    height=300,
    color=(100, 0, 100),
    batch=menu_batch,
    group=background
)

pause.opacity = 125
