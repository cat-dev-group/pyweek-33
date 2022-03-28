import pyglet


from .constants import HEIGHT, WIDTH

menu_batch = pyglet.graphics.Batch()
lose_menu_batch = pyglet.graphics.Batch()
win_menu_batch = pyglet.graphics.Batch()
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
    group=foreground,
)

resume_text = Text(
    text="Press 'P' to resume",
    size=20,
    x=WIDTH // 2,
    y=HEIGHT // 2,
    batch=menu_batch,
    group=foreground,
)

pause = Pause(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    width=800,
    height=300,
    color=(100, 0, 100),
    batch=menu_batch,
    group=background,
)

pause.opacity = 125

lose_screen = Pause(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    width=WIDTH // 2,
    height=HEIGHT // 2,
    color=(255, 0, 0),
    batch=lose_menu_batch,
    group=background,
)

lose_text = Text(
    text="You Lost :(",
    size=20,
    x=WIDTH // 2,
    y=HEIGHT // 2,
    batch=lose_menu_batch,
    group=foreground,
)

try_again = Text(
    text="Hit Enter to try again",
    size=20,
    x=WIDTH // 2,
    y=HEIGHT // 3,
)

lose_screen.opacity = 125

win_screen = Pause(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    width=WIDTH // 2,
    height=HEIGHT // 2,
    color=(0, 255, 0),
    batch=win_menu_batch,
    group=background,
)

win_text = Text(
    text="You Won :D",
    size=20,
    x=WIDTH // 2,
    y=HEIGHT // 2,
    batch=win_menu_batch,
    group=foreground,
)

next_level = Text(
    text="Hit Enter to move on to the next level!",
    size=20,
    x=WIDTH // 2,
    y=HEIGHT // 3,
)

win_screen.opacity = 125
