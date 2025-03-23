from classes.Player import *
from classes.Enemy import *
from classes.Inventory import *
from classes.Item import *
from classes.GameUI import *
from classes.GameConfig import *
from classes.Background import *
import pygame as pg
import random


class GamePlay:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            (Config.get('WIN_SIZE_W'), Config.get('WIN_SIZE_H')))
        # draw_home_screen(self.screen)
        # draw_selected_character_screen(self.screen)
        self.clock = pg.time.Clock()
        self.running = True
        self.state = "home"
        self.selected_character = None
        self.enemies = []

    def screen_update(self):
        if self.state == "home":
            result = draw_home_screen(self.screen)
            if result == "start":
                print("start button click")
                self.state = "main_game"

            elif result == "quit":
                self.running = False
                return

        elif self.state == "main_game":
            selected = draw_selected_character_screen(self.screen)
            if selected:
                print("Selected character:", selected.name)
                self.selected_character = selected
                self.generate_enemies()
                self.state = "battle"

        elif self.state == "battle":
            draw_battle_screen(
                self.screen, self.selected_character, self.enemies)

        self.clock.tick(10)
        pg.display.update()

    def generate_enemies(self):
        enemy_classes = [Clayman, Skull, Dragon, Stealer, DarkKnight]
        self.enemies = [random.choice(enemy_classes)() for _ in range(3)]

    def user_event(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                self.running = False

    def game_loop(self):

        while self.running:
            self.user_event()
            self.screen_update()

    def game_reset(self):
        self.__game_over = False
