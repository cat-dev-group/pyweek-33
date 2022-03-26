import pyglet

from .constants import HEIGHT, WIDTH
from .level_tools import Flag, Platform, Button
from .menus import menu_batch, pause_text, resume_text
from .player import Player

bg = pyglet.resource.image("bg.png")
bg.width = WIDTH
bg.height = HEIGHT

game_window = pyglet.window.Window(WIDTH, HEIGHT)

game_window.push_handlers(keys := pyglet.window.key.KeyStateHandler())

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


def on():
    ins = Player.entities["platform"].pop((WIDTH // 2, HEIGHT // 6))
    ins.delete()


def off():
    Platform(
        WIDTH // 2, HEIGHT // 6, width=HEIGHT // 3, color=(255, 215, 0), alignment="v"
    )


def on1():
    ins = Player.entities["platform"].pop((WIDTH // 3, HEIGHT // 2 + HEIGHT // 6))
    ins.delete()


def off1():
    Platform(
        WIDTH // 3,
        HEIGHT // 2 + HEIGHT // 6,
        width=HEIGHT // 3,
        color=(255, 215, 0),
        alignment="v",
    )


Platform(
    WIDTH // 3,
    HEIGHT // 2 + HEIGHT // 6,
    width=HEIGHT // 3,
    color=(255, 215, 0),
    alignment="v",
)
Platform(WIDTH // 2, HEIGHT // 6, width=HEIGHT // 3, color=(255, 215, 0), alignment="v")
Platform(
    WIDTH - WIDTH // 3,
    HEIGHT // 6,
    width=HEIGHT // 3,
    color=(255, 215, 0),
    alignment="v",
)
Button(WIDTH // 3 - 22, HEIGHT // 2 + HEIGHT // 6 + HEIGHT // 12, on, off)
Button(WIDTH - WIDTH // 3 - 22, HEIGHT // 6 + HEIGHT // 12, on1, off1)
Platform(0, HEIGHT // 2 + HEIGHT // 6 - 10, width=WIDTH, color=(255, 215, 0))
Platform(0, HEIGHT // 6 - 10, width=WIDTH, color=(255, 215, 0))
# Button(WIDTH - WIDTH//2.5 - 22 , HEIGHT//3 - HEIGHT//12 + 10, on,off)

good_world_flag = Flag(WIDTH - 100, HEIGHT // 2 + HEIGHT // 6)
under_world_flag = Flag(WIDTH - 100, HEIGHT // 6)


def push():
    for i in Player.entities.values():
        for j in i.values():
            if hasattr(j, "key_handler"):
                game_window.push_handlers(j)
                game_window.push_handlers(j.key_handler)


push()
game_window.push_handlers(good_twin)  # to make sure the pause key is tracked


def update(dt):
    running = True
    if good_twin.pause_check["pause"] and running:
        running = False
        menu_batch.draw()
    elif good_twin.pause_check["pause"] and not running:
        running = True
    if running:
        for i, j in Player.entities.items():
            for obj in j.values():
                if i in ("button", "players"):
                    obj.update(dt)


def render_entities():
    for i in Player.entities.values():
        for j in i.values():
            j.draw()
    pause_text.draw()


@game_window.event
def on_draw():
    game_window.clear()
    bg.blit(0, 0)
    render_entities()
    if good_twin.pause_check["pause"]:

        menu_batch.draw()
        resume_text.draw()
