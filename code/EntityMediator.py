import pygame

from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(entity: Entity):
        if isinstance(entity, Enemy):
            if entity.rect.right < 0:
                entity.health = 0

    @staticmethod
    def __verify_collision_entity(entity_one, entity_two):
        if not isinstance(entity_one, Enemy) and isinstance(entity_two, Enemy):
            current_time = pygame.time.get_ticks()
            time_since_last_damage = (current_time - entity_one.last_damage) / 1000

            if time_since_last_damage >= 2:
                if (entity_one.rect.right >= entity_two.rect.left and
                        entity_one.rect.left <= entity_two.rect.right and
                        entity_one.rect.bottom >= entity_two.rect.top and
                        entity_one.rect.top <= entity_two.rect.bottom):
                    entity_one.health -= entity_two.damage
                    entity_one.last_damage = current_time

    @staticmethod
    def __give_score(player: Player, enemy: Enemy):
        if player.rect.left > enemy.rect.right and not enemy.passed:
            player.score += enemy.score
            enemy.passed = True

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_one = entity_list[i]
            EntityMediator.__verify_collision_window(entity_one)
            for j in range(i + 1, len(entity_list)):
                entity_two = entity_list[j]
                EntityMediator.__verify_collision_entity(entity_one, entity_two)
                if isinstance(entity_one, Player) and isinstance(entity_two, Enemy):
                    EntityMediator.__give_score(entity_one, entity_two)
                elif isinstance(entity_two, Player) and isinstance(entity_one, Enemy):
                    EntityMediator.__give_score(entity_two, entity_one)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        entity_list[:] = [
            entity for entity in entity_list
            if not (entity.health <= 0 and isinstance(entity, (Enemy, Player)))
        ]
