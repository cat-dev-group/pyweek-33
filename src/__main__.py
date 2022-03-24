import pyglet

from .game import update

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
