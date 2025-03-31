#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME, EVENT_COIN, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, SPAWN_TIME_LEVEL1, SPAWN_TIME_LEVEL2, WIN_WIDTH, C_RED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Menu import Menu
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player')
        player.score = player_score[0]
        self.entity_list.append(player)
        self.timeout = TIMEOUT_LEVEL

        if self.name == "Level 1":
            enemy_spawn_time = SPAWN_TIME_LEVEL1
        elif self.name == "Level 2":
            enemy_spawn_time = SPAWN_TIME_LEVEL2
        else:
            enemy_spawn_time = SPAWN_TIME

        pygame.time.set_timer(EVENT_ENEMY, enemy_spawn_time)
        pygame.time.set_timer(EVENT_COIN, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if ent.name == 'Player':
                    self.level_text(14, f'Player - Score: {ent.score}', C_WHITE, (10, 20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    if self.name == "Level 1":
                        choice = random.choice(('Enemy1Lv1', 'Enemy2Lv1', 'Enemy3Lv1'))
                    elif self.name == "Level 2":
                        choice = random.choice(('Enemy1Lv2', 'Enemy2Lv2', 'Enemy3Lv2', 'Enemy4Lv2'))
                    else:
                        choice = random.choice(('Enemy1Lv1', 'Enemy2Lv1', 'Enemy3Lv1'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_COIN:
                    choice = 'Coin'
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                player_score[0] = ent.score
                        return True  # Level ends

            # Check if player is alive
            found_player = any(isinstance(ent, Player) for ent in self.entity_list)
            if not found_player:
                return self.game_over()  # Game over when player dies

            # Printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def game_over(self):
        game_over_image = pygame.image.load('./asset/GameOver.png').convert_alpha()
        game_over_rect = game_over_image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

        while True:
            self.window.fill((0, 0, 0))  # Black background
            self.window.blit(game_over_image, game_over_rect)

            # Centered "GAME OVER" text
            self.draw_centered_text("GAME OVER", 100, C_RED, WIN_HEIGHT // 3)

            # Centered "Press ENTER to return to the menu" text
            self.draw_centered_text("Press ENTER to return to the menu", 50, C_WHITE, WIN_HEIGHT // 3 + 100)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menu = Menu(self.window)  # Return to menu
                        return None

    def draw_centered_text(self, text: str, size: int, color: tuple, y_position: int):
        """Helper function to draw text centered on the screen."""
        font = pygame.font.Font("./asset/BradyBunchRemastered.ttf", size)
        text_surf = font.render(text, True, color).convert_alpha()
        text_rect = text_surf.get_rect(center=(WIN_WIDTH // 2, y_position))
        self.window.blit(text_surf, text_rect)
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/BradyBunchRemastered.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
