#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Coin import Coin
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name.replace(' ', ''):
            case 'Level1Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Level2Bg':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player', (10, WIN_HEIGHT/3))
            case 'Enemy1Lv1':
                return Enemy('Enemy1Lv1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2Lv1':
                return Enemy('Enemy2Lv1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3Lv1':
                return Enemy('Enemy3Lv1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy1Lv2':
                return Enemy('Enemy1Lv2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2Lv2':
                return Enemy('Enemy2Lv2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy3Lv2':
                return Enemy('Enemy3Lv2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy4Lv2':
                return Enemy('Enemy4Lv2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Coin':
                return Coin('Coin', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
