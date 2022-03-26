import pyglet

# creating and pushing objects to the screen


from .tutorial import game_window, update, good_twin, evil_twin

game_window.push_handlers(good_twin)
game_window.push_handlers(evil_twin)
game_window.push_handlers(good_twin.key_handler)
game_window.push_handlers(evil_twin.key_handler)


# driver code

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
