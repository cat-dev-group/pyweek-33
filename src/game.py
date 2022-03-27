import pyglet
from .constants import HEIGHT, WIDTH

bg = pyglet.resource.image("bg.png")
bg.width = WIDTH
bg.height = HEIGHT


levels = {
    "tutorial": "from .tutorial import evil_twin, game_window, good_twin, update",
    "level1": "from .level1 import evil_twin, game_window, good_twin, update",
    "level2": "from .level2 import evil_twin, game_window, good_twin, update",
    "level3": "from .level3 import evil_twin, game_window, good_twin, update",
    "level4": "from .level4 import evil_twin, game_window, good_twin, update",
}

exec(levels[tutorial"])


# creating and pushing objects to the screen
game_window.push_handlers(good_twin)
game_window.push_handlers(evil_twin)
game_window.push_handlers(good_twin.key_handler)
game_window.push_handlers(evil_twin.key_handler)


# driver code
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
