from classes.Player import *
from classes.Enemy import *
from classes.Inventory import *
from classes.Item import *
from classes.GameUI import *
from classes.GameConfig import *
from classes.Background import *
import pygame as pg


class GamePlay:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            (Config.get('WIN_SIZE_W'), Config.get('WIN_SIZE_H')))
        draw_home_screen(self.screen)
        self.__clock = pg.time.Clock()
        self.__running = True

    def user_event(self):
        pass

    def screen_update(self):
        draw_home_screen(self.screen)
        self.__clock.tick(10)
        pg.display.update()

    def user_event(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                self.__running = False

    def game_loop(self):

        while self.__running:
            self.user_event()
            self.screen_update()

    def game_reset(self):
        self.__game_over = False
