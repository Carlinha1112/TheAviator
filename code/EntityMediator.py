from code.Coin import Coin
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player


class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction1 = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction1 = True
        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction1 = True
        valid_interaction2 = False
        if isinstance(ent1, Player) and isinstance(ent2, Coin):
            valid_interaction2 = True

        if valid_interaction1:  # same as> if valid_interaction == True:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health = 0

        if valid_interaction2:  # same as> if valid_interaction == True:
            if isinstance(ent1, Player) and isinstance(ent2, Coin):
                if (ent1.rect.right >= ent2.rect.left and
                        ent1.rect.left <= ent2.rect.right and
                        ent1.rect.bottom >= ent2.rect.top and
                        ent1.rect.top <= ent2.rect.bottom):
                    ent1.score += 10
                    ent2.health = 0

    @staticmethod
    def __give_score(coin: Coin, entity_list: list[Entity]):
        for ent in entity_list:
            if ent.name == 'Player':
                ent.score += coin.score

    @staticmethod
    def verify_collision(entity_list: [Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                if not (isinstance(entity1, Coin) and isinstance(entity2, Player)):
                    EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: [Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Entity):
                    entity_list.remove(ent)
