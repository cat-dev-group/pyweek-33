import pyglet

WIDTH, HEIGHT = 800, 600
game_window = pyglet.window.Window(WIDTH, HEIGHT)


def create_level():
    segments = []
    for i in range(0, WIDTH, round(WIDTH / 10)):
        x = 0 + i
        y = HEIGHT / 2
        width = round(WIDTH / 11)
        height = HEIGHT / 50
        new_segment = pyglet.shapes.Rectangle(x, y, width, height)
        segments.append(new_segment)
    return segments


level = create_level()


class Player(pyglet.shapes.Circle):
    def __init__(self, x, y, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.x = x
        self.y = y
        self.event_handlers = [self, self.key_handler]

    def update(self, dt):
        # super(Player, self).update(dt)

        if self.key_handler[pyglet.window.key.A]:
            self.x -= 250 * dt

        if self.key_handler[pyglet.window.key.D]:
            self.x += 250 * dt


player = Player(x=0, y=HEIGHT / 2 + 40, radius=15, color=(255, 0, 0))
game_window.push_handlers(player)
game_window.push_handlers(player.key_handler)


@game_window.event
def on_draw():
    game_window.clear()
    for piece in level:
        piece.draw()
    player.draw()


def update(dt):
    player.update(dt)


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
