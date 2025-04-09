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

# ก็คือเริ่มเกมมาก็เก็บstart time
# เสร็จเเล้วก็เรียกเกมstatมาเก็บค่าไปอีกที

class GamePlay:

    def __init__(self):
        pg.init()
        self.music = Sound("sound/adventure-music-229534.mp3", -1,0,0.2)
        self.music.play()
        self.screen = pg.display.set_mode((Config.get('WIN_SIZE_W'), Config.get('WIN_SIZE_H')))
        self.clock = pg.time.Clock()
        self.running = True
        self.state = "home"
        self.selected_character = None
        self.enemies = []
        self.current_turn = "player"  # could be "player" or "enemies"
        self.enemy_index = 0          # tracks which enemy is being attacked
        self.battle_log = ""          # message log for attacks
        self.inventory = Inventory()
        self.inventory.add_coin(100)  # Give starter coins
        self.shop = Shop()
        self.stats = GameStats()
        self.floor = 1
        self.using_item = False
        self.selected_item = None
        
        

        self.ui = GameUI(self.screen)

        self.attack_button = Button("image/attack.png", (50, 450), 0.5)
        self.shop_button = Button("image/shop.png", (650, 10), 0.5)
        self.inventory_button = Button("image/inventory.png", (650, 450), 0.5)
        self.use_skill_button = Button("image/special_ability.png", (200, 500), 0.5)

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
            self.ui.draw_battle_screen(self.selected_character, self.enemies, self.battle_log, self.floor)
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

                if self.use_skill_button.draw(self.screen):
                    if not self.selected_character.ability_used:
                        if self.enemies:
                            # Use ability (pass enemies list)
                            self.battle_log = self.selected_character.use_ability(self.enemies)
                            self.selected_character.ability_used = True
                            self.current_turn = "enemies"  # End turn after using skill
                        else:
                            self.battle_log = "No enemies to use skill on!"
                    
                    else:
                        self.battle_log = "Skill already used this floor!"

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
                  
            if self.selected_character and self.selected_character.health <= 0:
                self.battle_log = f"{self.selected_character.name} has fallen! Game Over."
                self.state = "game_over"

            if self.enemies is not None and not self.enemies:
                self.battle_log = f"You defeated all enemies! Victory!"
                self.state = "victory"

        
        
        elif self.state == "shop":
            result = self.ui.draw_shop_screen(self.shop, self.inventory)
            if result == "back":
                self.state = "battle"

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.state = "battle"

        elif self.state == "inventory":
            result = self.ui.draw_inventory_screen(self.inventory)
            if result == "back":
                self.state = "battle"
                
            elif isinstance(result, Item):
                self.selected_item = result
                self.state = "inventory_action"

            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE] or keys[pg.K_ESCAPE]:
                self.state = "battle"

        
        elif self.state == "inventory_action":
            result = self.ui.draw_item_action_popup(self.selected_item)
            if result == "use":
                self.selected_item.apply_effect(self.selected_character, self.inventory)
                self.inventory.remove_item(self.selected_item)
                self.selected_item = None
                self.state = "inventory"

            elif result == "discard":
                self.inventory.add_coin(self.selected_item.cost // 2)
                self.inventory.remove_item(self.selected_item)
                self.selected_item = None
                self.state = "inventory"

            elif result == "back":
                self.selected_item = None
                self.state = "inventory"
        
        
        
        
        elif self.state == "game_over":
            pg.mixer.music.stop() 
            self.ui.draw_game_over()
            
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                self.game_reset()
            

        elif self.state == "victory":
            if self.floor >= 3:
                self.ui.draw_game_victory()
                keys = pg.key.get_pressed()
                if keys[pg.K_SPACE]:
                    self.game_reset()
            
            else:
                font = pg.font.Font("font/PixelifySans-Bold.ttf", 40)
                self.screen.fill(Config.get("WHITE"))
                text = font.render(f"Floor {self.floor} Cleared! +15 Coins", True, Config.get("BLACK"))
                self.screen.blit(text, (200, 250))     
            

                self.inventory.add_coin(15)

                pg.display.update()
                pg.time.delay(2000)  # Wait 2 sec to show message

                self.next_floor()
                self.state = "battle"
            

        self.clock.tick(10)
        pg.display.update()

    def generate_enemies(self):
        enemy_classes = [Clayman, Skull, Dragon, Stealer, DarkKnight]
        self.enemies = []
        for _ in range(3):
            enemy = random.choice(enemy_classes)()
            enemy.scale_to_level(self.floor)
            self.enemies.append(enemy)

    def user_event(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit()
                self.running = False

    def game_loop(self):

        while self.running:
            self.user_event()
            self.screen_update()
            
    def next_floor(self):
        self.floor += 1
        self.enemy_index = 0
        self.current_turn = "player"
        
        self.selected_character.level_up()
        self.selected_character.vampire_mode = False
        self.selected_character.critical_chance = 0
        self.selected_character.ability_used = False
        
        self.generate_enemies()

    def game_reset(self):
        self.floor = 1
        self.enemy_index = 0
        self.current_turn = "player"
        self.selected_character = None
        self.enemies = []
        self.battle_log = ""
        self.inventory = Inventory()
        self.inventory.add_coin(100)
        self.shop = Shop()
        self.state = "home"  # <-- Go back to character selection or home screen
        self.music.play()    # Optional: restart music
