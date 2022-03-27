import pyglet

from .constants import HEIGHT, WIDTH
from .level_tools import Flag, Platform
from .menus import (
    menu_batch,
    pause_text,
    resume_text,
    lose_menu_batch,
    try_again,
    lose_text,
    win_menu_batch,
    win_text,
)
from .player import Player

bg = pyglet.resource.image("bg.png")
bg.width = WIDTH
bg.height = HEIGHT
game_window = pyglet.window.Window(WIDTH, HEIGHT)
game_window.running = True
game_window.state = -1
game_window.push_handlers(keys := pyglet.window.key.KeyStateHandler())


def initial():

    global evil_twin, good_twin, under_world_flag, good_world_flag, label, label2, label3, Text
    evil_twin = Player(
        x=0, y=HEIGHT // 6, ground=HEIGHT // 6, width=40, height=40, color=(0, 0, 128)
    )
    good_twin = Player(
        x=0,
        y=HEIGHT // 2 + HEIGHT // 6,
        ground=HEIGHT // 6 + HEIGHT // 2,
        width=40,
        height=40,
        color=(235, 64, 52),
    )

    class Text(pyglet.text.Label):
        ins = []

        def __init__(self, text, size, x, y, edits=1):
            super().__init__(
                text,
                font_name="comic sans",
                font_size=size,
                x=x,
                y=y,
                anchor_x="center",
                anchor_y="center",
            )
            # Player.entities["labels"][x, y] = self
            self.edits = [False] * edits
            Text.ins.append(self)

    label = Text(
        "Welcome to the game!",
        size=20,
        x=WIDTH // 2,
        y=HEIGHT - 100,
    )

    label2 = Text(
        "Use D to move right",
        size=20,
        x=WIDTH // 6 - 200,
        y=HEIGHT // 2 + HEIGHT // 3,
        edits=3,
    )

    label3 = Text("Maybe try this ?", size=20, x=WIDTH // 2, y=HEIGHT // 4.5 + 100)

    Platform(WIDTH // 2, HEIGHT // 4.5, width=WIDTH // 6, color=(255, 215, 0))
    Platform(
        WIDTH // 2 + WIDTH // 6,
        HEIGHT // 4.5,
        width=WIDTH // 6,
        color=(255, 215, 0),
        alignment="v",
    )
    Platform(0, HEIGHT // 2 + HEIGHT // 6 - 10, width=WIDTH, color=(255, 215, 0))
    Platform(0, HEIGHT // 6 - 10, width=WIDTH, color=(255, 215, 0))

    good_world_flag = Flag(WIDTH - 100, HEIGHT // 2 + HEIGHT // 6)
    under_world_flag = Flag(WIDTH - 100, HEIGHT // 6)

    def push():
        for i in Player.entities.values():
            if i == "players":
                continue
            for j in i.values():
                if hasattr(j, "key_handler"):
                    game_window.push_handlers(j)
                    game_window.push_handlers(j.key_handler)

    push()
    game_window.push_handlers(good_twin)  # to make sure the pause key is tracked


initial()


def update(dt):
    if keys[pyglet.window.key.D] and not label2.edits[0]:
        label2.text = "Use A to move left"
        label2.edits[0] = True
    elif keys[pyglet.window.key.A] and not label2.edits[1] and label2.edits[0]:
        label2.text = "Use W to Jump"
        label2.edits[1] = True
    elif keys[pyglet.window.key.W] and not label2.edits[2] and all(label2.edits[:2]):
        label2.text = "Perfect!"
        label2.edits[2] = True
        label.text = "Your evil twin from underworld will copy your moves D:"
    if Player.entities["players"][0, HEIGHT // 6].x > WIDTH // 2 and not label.edits[0]:
        label.text = "You have to reach the flag of your world WITHOUT letting your twin reach it"
        label.edits[0] = True

    game_window.running = True
    if good_twin.pause_check["pause"] and game_window.running:
        game_window.running = False

        menu_batch.draw()
    elif good_twin.pause_check["pause"] and not game_window.running:
        game_window.running = True
    if game_window.running and game_window.state == -1:
        for i, j in Player.entities.items():
            for obj in j.values():
                if i in ("button", "players"):
                    obj.update(dt)
    if under_world_flag.collision_check(evil_twin):
        for i in Text.ins:
            i.delete()
        game_window.state = False

    elif good_world_flag.collision_check(good_twin):
        for i in Text.ins:
            i.delete()
        game_window.state = True


def render_entities():
    label.draw()
    label2.draw()
    for i in Player.entities.values():
        for j in i.values():
            j.draw()
    if label.edits[0]:
        label3.draw()
    pause_text.draw()
    if keys[pyglet.window.key.ENTER] and not game_window.state:
        for j in Player.entities.values():
            j.clear()
        game_window.state = -1
        game_window.running = True
        initial()


@game_window.event
def on_draw():
    game_window.clear()
    bg.blit(0, 0)
    render_entities()
    if good_twin.pause_check["pause"]:
        menu_batch.draw()
        resume_text.draw()
    if not game_window.state:
        lose_menu_batch.draw()
        lose_text.draw()
        try_again.draw()
    if game_window.state == 1:
        win_menu_batch.draw()
        win_text.draw()
        # next_level.draw()
