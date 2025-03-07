from code.Const import WINDOW_HEIGHT, WINDOW_WIDTH
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.velocity_y = 0
        self.velocity_x = 0
        self.gravity = 0.25
        self.jump_speed = -10
        self.speed = 3
        self.on_ground = False
        self.facing_right = True
        self.walk_frames = []
        self.current_frame = 0

    def move(self):
        self.rect.x += self.velocity_x

        self.rect.x += self.velocity_x

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.y >= WINDOW_HEIGHT - self.rect.height:
            self.rect.y = WINDOW_HEIGHT - self.rect.height
            self.velocity_y = 0
            self.on_ground = True

        self.update_animation()

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

    def move_left(self):
        self.velocity_x = -self.speed
        self.facing_right = False

    def move_right(self):
        self.velocity_x = self.speed
        self.facing_right = True

    def stop(self):
        self.velocity_x = 0

    def update_animation(self):
        pass
