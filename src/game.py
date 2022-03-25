import pyglet

from .constants import HEIGHT, WIDTH
from .menus import menu_batch
from .player import Player


game_window = pyglet.window.Window(WIDTH, HEIGHT)

player = Player(
    x=0, y=HEIGHT // 6, ground=HEIGHT // 6, width=40, height=40, color=(0, 0, 128)
)
player2 = Player(
    x=0,
    y=HEIGHT // 2 + HEIGHT // 6,
    ground=HEIGHT // 6 + HEIGHT // 2,
    width=40,
    height=40,
    color=(235, 64, 52),
)

game_window.push_handlers(player2)
game_window.push_handlers(player)
game_window.push_handlers(player2.key_handler)
game_window.push_handlers(player.key_handler)


@game_window.event
def on_draw():
    game_window.clear()
    pyglet.shapes.Rectangle(
        x=0, y=0, width=WIDTH, height=HEIGHT // 6, color=(0, 128, 0)
    ).draw()
    pyglet.shapes.Rectangle(
        x=0, y=HEIGHT // 6, width=WIDTH, height=HEIGHT // 3, color=(0, 255, 255)
    ).draw()

    pyglet.shapes.Rectangle(
        x=0, y=HEIGHT // 2, width=WIDTH, height=HEIGHT // 6, color=(0, 128, 0)
    ).draw()
    pyglet.shapes.Rectangle(
        x=0,
        y=HEIGHT // 6 + HEIGHT // 2,
        width=WIDTH,
        height=HEIGHT // 3,
        color=(0, 255, 255),
    ).draw()

    player.draw()
    player2.draw()

    if player.keys["pause"]:
        menu_batch.draw()


def update(dt):
    running = True
    if player.keys["pause"] and running:
        running = False
    elif player.keys["pause"] and not running:
        running = True
    if running:
        player.update(dt)
        player2.update(dt)
