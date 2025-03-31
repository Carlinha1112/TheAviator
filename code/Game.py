#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()  # Player chooses an option

            if menu_return in MENU_OPTION[0]:
                player_score = [0, 0]
                level = Level(self.window, 'Level 1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level 2', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)

                if not level_return:  # Player died in Level 2, return to menu
                    continue  # Restart from menu


            elif menu_return == MENU_OPTION[1]:
                score.show()
            elif menu_return == MENU_OPTION[2]:  # "Exit" Selected
                pygame.quit()
                quit()
            else:
                pygame.quit()
                quit()
