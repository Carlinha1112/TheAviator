#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.Background import Background
from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Enemy import Enemy
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT/3))
            case 'Enemy1Lv1':
                return Enemy('Enemy1Lv1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2Lv1':
                return Enemy('Enemy2Lv1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3Lv1':
                return Enemy('Enemy3Lv1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))