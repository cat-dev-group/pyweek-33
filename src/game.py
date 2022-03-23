import pyglet

WIDTH, HEIGHT = 1920, 1080
game_window = pyglet.window.Window(WIDTH, HEIGHT)


class Player(pyglet.shapes.Rectangle):
    def __init__(self, x, y, ground, *args, **kwargs):
        super().__init__(x, y, *args, **kwargs)
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.x = x
        self.y = y
        self.event_handlers = [self, self.key_handler]
        self.ground = ground
        self.max_jump_height_reached = False

    def update(self, dt):
        # movements
        if self.key_handler[pyglet.window.key.A]:
            self.x -= 250 * dt

        if self.key_handler[pyglet.window.key.D]:
            self.x += 250 * dt

        # jump logic
        if self.key_handler[pyglet.window.key.W]:
            self.y += 250 * dt if not self.max_jump_height_reached else 0

        if self.y - self.ground > 100:
            self.max_jump_height_reached = True
        if self.y - self.ground <= 0:
            self.max_jump_height_reached = False

        self.y -= (
            250 * dt
            if (self.y - self.ground > 0 and not self.key_handler[pyglet.window.key.W])
            or self.max_jump_height_reached
            else 0
        )

        # restriction to leave screen
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

        if self.x < 0:
            self.x = 0


# creating and pushing objects to the screen


player = Player(
    x=0, y=HEIGHT // 6, ground=HEIGHT // 6, width=40, height=40, color=(235, 64, 52)
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

# event handling


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


def update(dt):
    player.update(dt)
    player2.update(dt)


# driver code

if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
