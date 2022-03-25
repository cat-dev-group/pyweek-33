import pyglet
from .level_tools import Player  # , platform, flag, button
from .constants import WIDTH, HEIGHT

bg = pyglet.resource.image("bg.png")

game_window = pyglet.window.Window(WIDTH, HEIGHT)

# creating and pushing objects to the screen

good_twin = Player(
    x=0, y=HEIGHT // 6, ground=HEIGHT // 6, width=40, height=40, color=(0, 0, 128)
)
evil_twin = Player(
    x=0,
    y=HEIGHT // 2 + HEIGHT // 6,
    ground=HEIGHT // 6 + HEIGHT // 2,
    width=40,
    height=40,
    color=(235, 64, 52),
)


# def on():
#     Player.entities["platform"][WIDTH // 2, HEIGHT // 2 + HEIGHT // 6].y = -100


# def off():
#     Player.entities["platform"][WIDTH // 2, HEIGHT // 2 + HEIGHT // 6].y = (
#         HEIGHT // 6 + HEIGHT // 2
#     )


game_window.push_handlers(good_twin)
game_window.push_handlers(evil_twin)
game_window.push_handlers(good_twin.key_handler)
game_window.push_handlers(evil_twin.key_handler)
# platform(
#     WIDTH - WIDTH // 3, HEIGHT // 4.5, width=WIDTH // 6, color=(165, 42, 42)
# )
# platform(
#     WIDTH - WIDTH // 2, HEIGHT // 4, width=WIDTH // 6, color=(165, 42, 42)
# )
# platform(
#     WIDTH // 2,
#     HEIGHT // 2 + HEIGHT // 6,
#     width=HEIGHT // 2,
#     color=(165, 42, 42),
#     alignment="v",
# )

# flag(WIDTH - 100, HEIGHT // 2 + HEIGHT // 6)
# flag(WIDTH - 100, HEIGHT // 6)
# button(WIDTH // 3, HEIGHT // 6 + 50, on, off)


def render_entities():

    for i in Player.entities.values():
        for j in i.values():
            j.draw()


@game_window.event
def on_draw():
    game_window.clear()
    bg.blit(0, 0)

    render_entities()


def update(dt):
    for i, j in Player.entities.items():
        for obj in j.values():
            if i in ("button", "players"):
                obj.update(dt)


# driver code

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
