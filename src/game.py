import pyglet

from .tutorial import evil_twin, game_window, good_twin, update

# creating and pushing objects to the screen
game_window.push_handlers(good_twin)
game_window.push_handlers(evil_twin)
game_window.push_handlers(good_twin.key_handler)
game_window.push_handlers(evil_twin.key_handler)


# driver code
if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
