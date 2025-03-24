from classes.Player import *
from classes.Enemy import *
from classes.Inventory import *
from classes.Item import *
from classes.GameUI import *
from classes.GameConfig import *
from classes.Background import *
from classes.Shop import *
from classes.GameStats import *
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
        self.current_turn = "player"  # could be "player" or "enemies"
        self.enemy_index = 0          # tracks which enemy is being attacked
        self.battle_log = ""          # message log for attacks
        self.inventory = Inventory()
        self.inventory.add_coin(0)  # Give starter coins
        self.shop = Shop()
        self.stats = GameStats()

        self.ui = GameUI(self.screen)

        self.attack_button = Button("image/attack.png", (50, 450), 0.5)
        self.shop_button = Button("image/shop.png", (650, 450), 0.5)
        self.inventory_button = Button(
            "image/inventory.png", (350, 450), 0.5)
        self.use_item_button = Button("image/use_item.png", (200, 450), 0.5)

    def screen_update(self):
        if self.state == "home":
            result = self.ui.draw_home_screen()
            if result == "start":
                print("start button click")
                self.state = "main_game"

            elif result == "quit":
                self.running = False
                return

        elif self.state == "main_game":
            selected = self.ui.draw_selected_character_screen()
            if selected:
                print("Selected character:", selected.name)
                self.selected_character = selected
                self.generate_enemies()
                self.state = "battle"

        elif self.state == "battle":
            self.ui.draw_battle_screen(
                self.selected_character, self.enemies, self.battle_log)
            if self.current_turn == "player":
                if self.attack_button.draw(self.screen):
                    if self.enemy_index < len(self.enemies):
                        target = self.enemies[self.enemy_index]
                        dmg = self.selected_character.attack_enemy(target)
                        self.battle_log = f"{self.selected_character.name} attacked {target.name} for {dmg} damage!"

                        if dmg == 0:
                            self.battle_log += "(No effect)"

                        if target.health <= 0:
                            self.battle_log += f" {target.name} is defeated!"
                            self.enemies.pop(self.enemy_index)

                            if not self.enemies:
                                self.battle_log = "You defeated all enemies! Victory!"
                                self.state = "victory"
                                return
                        else:
                            self.enemy_index += 1

                    if self.enemy_index >= len(self.enemies):
                        self.enemy_index = 0
                        self.current_turn = "enemies"

                if self.shop_button.draw(self.screen):
                    self.state = "shop"

                if self.inventory_button.draw(self.screen):
                    self.state = "inventory"

                if self.use_item_button.draw(self.screen):
                    pass

            elif self.current_turn == "enemies":
                if self.enemy_index < len(self.enemies):
                    attacker = self.enemies[self.enemy_index]
                    dmg = attacker.attack_enemy(self.selected_character)
                    self.battle_log = f"{attacker.name} attacked {self.selected_character.name} for {dmg} damage!"

                    if self.selected_character.health <= 0:
                        self.battle_log = f"{self.selected_character.name} has fallen! Game Over."
                        self.state = "game_over"

                    self.enemy_index += 1
                else:
                    self.enemy_index = 0
                    self.current_turn = "player"
                    # End game conditions
            if self.selected_character and self.selected_character.health <= 0:
                self.battle_log = f"{self.selected_character.name} has fallen! Game Over."
                self.state = "game_over"

            if self.enemies is not None and not self.enemies:
                self.battle_log = f"You defeated all enemies! Victory!"
                self.state = "victory"

        elif self.state == "shop":
            self.ui.draw_shop_screen(self.shop, self.inventory)

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.state = "battle"

        elif self.state == "inventory":
            result = self.ui.draw_inventory_screen(self.inventory)
            if result == "back":
                self.state = "battle"

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE] or keys[pg.K_ESCAPE]:
                self.state = "battle"

        elif self.state == "game_over":
            self.ui.draw_game_over()

        elif self.state == "victory":
            self.ui.draw_game_victory()

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
