from code.Const import WINDOW_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.passed = False

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]