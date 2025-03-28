import pygame as pg
from classes.Background import *
from classes.GameConfig import *
from classes.Button import *
from classes.Sound import *
from classes.Player import *


class GameUI:

    def __init__(self, screen):
        self.screen = screen
        self.character_buttons = []
        self.characters = [Wonderwoman(), Wizard(), Omen(), Hulk(), Predator()]
        positions = [(80, 200), (220, 200), (360, 200), (500, 200), (640, 200)]
        self.character_buttons = [
            Button(char.image, pos, 1.0) for char, pos in zip(self.characters, positions)]

    def draw_home_screen(self):
        self.screen.fill(Config.get('WHITE'))
        font = pg.font.Font("font/PixelifySans-Bold.ttf", 50)
        home_bg = Background("image/Backgroundcastle.png", [0, 0])
        start_button = Button("image/playbutton.png", [325, 300], 0.5)
        quit_button = Button("image/quitbutton.png", [325, 400], 0.5)
        # sound = Sound("sound/adventure-music-229534.mp3", -1, 0, 0.1)

        title_text = font.render(
            f'Tower Leveling Clash', True, Config.get("BLACK"))
        title_text2 = font.render(
            f'Tower Leveling Clash', True, Config.get("DARKBROWN"))

        home_bg.draw(self.screen)
        start_click = start_button.draw(self.screen)
        quit_click = quit_button.draw(self.screen)
        self.screen.blit(title_text, (158, 200))
        self.screen.blit(title_text2, (155, 200))
        # sound.play()

        if start_click:
            return "start"

        elif quit_click:
            return "quit"

    def draw_selected_character_screen(self):
        self.screen.fill(Config.get('WHITE'))
        title_font = pg.font.Font("font/PixelifySans-Bold.ttf", 50)
        name_font = pg.font.Font("font/PixelifySans-Bold.ttf", 20)
        home_bg = Background("image/Backgroundcastle.png", [0, 0])
        title = title_font.render("Select Your Character",
                                  True, Config.get("BLACK"))

        title_text2 = title_font.render(
            f'Select Your Character', True, Config.get("DARKBROWN"))
        home_bg.draw(self.screen)
        self.screen.blit(title, (158, 100))
        self.screen.blit(title_text2, (155, 100))

        selected_character = None

        for i, button in enumerate(self.character_buttons):
            if button.draw(self.screen):  # If clicked
                selected_character = self.characters[i]

            name_text = name_font.render(
                self.characters[i].name, True, Config.get("BLACK"))
            name_rect = name_text.get_rect(
                center=(button.rect.centerx, button.rect.bottom + 10))
            self.screen.blit(name_text, name_rect)
        return selected_character

    def draw_battle_screen(self, player, enemies, battle_log=""):
        self.screen.fill(Config.get('BLACK'))
        font = pg.font.Font("font/PixelifySans-Bold.ttf", 20)
        battle_bg = Background("image/Backgroundgrass.png", [0, 0])

        battle_bg.draw(self.screen)
        # Draw player character on the left
        player_img = pg.image.load(player.image)
        player_img = pg.transform.scale(player_img, (120, 120))
        self.screen.blit(player_img, (50, 220))

        player_name = font.render(player.name, True, Config.get("WHITE"))
        self.screen.blit(player_name, (50, 200))

        # Draw player stats
        stats = f"HP: {player.health}  ATK: {player.attack}  DEF: {player.defense}"
        stats_text = font.render(stats, True, (255, 255, 255))
        self.screen.blit(stats_text, (50, 350))

        # Draw enemies
        for i, enemy in enumerate(enemies):
            x = 400 + i * 140
            enemy_img = pg.image.load(enemy.image)
            enemy_img = pg.transform.scale(enemy_img, (100, 100))
            self.screen.blit(enemy_img, (x, 220))

            enemy_name = font.render(enemy.name, True, Config.get("RED"))
            self.screen.blit(enemy_name, (x, 200))

            stats_health = f"HP: {enemy.health}"
            stats_attack = f"ATK: {enemy.attack}"
            stats_defence = f"DEF: {enemy.defense}"
            stats_text1 = font.render(stats_health, True, Config.get("RED"))
            stats_text2 = font.render(stats_attack, True, Config.get("RED"))
            stats_text3 = font.render(stats_defence, True, Config.get("RED"))
            self.screen.blit(stats_text1, (x, 330))
            self.screen.blit(stats_text2, (x, 375))
            self.screen.blit(stats_text3, (x, 410))
            # Draw battle log
        log_text = font.render(battle_log, True, Config.get("YELLOW"))
        self.screen.blit(log_text, (50, 100))

    def draw_game_over(self):
        self.screen.fill(Config.get("BLACK"))
        font = pg.font.Font("font/PixelifySans-Bold.ttf", 60)
        text = font.render("GAME OVER", True, Config.get("RED"))
        self.screen.blit(text, (300, 250))

    def draw_game_victory(self):
        self.screen.fill(Config.get("WHITE"))
        font = pg.font.Font("font/PixelifySans-Bold.ttf", 60)
        text = font.render("VICTORY!", True,  Config.get("RED"))
        self.screen.blit(text, (300, 250))

    def draw_shop_screen(self, shop, inventory):
        self.screen.fill(Config.get("DARKBLUE"))
        font = pg.font.Font(None, 28)
        title = font.render("Welcome to the Shop!", True, Config.get("YELLOW"))
        self.screen.blit(title, (300, 50))

        # Display coins
        coin_text = font.render(
            f"Coins: {inventory.coin}", True, Config.get("WHITE"))
        self.screen.blit(coin_text, (600, 50))

        for i, item in enumerate(shop.items_in_shop):
            x = 50 + i * 180
            y = 120
            img = pg.image.load(item.image)
            img = pg.transform.scale(img, (80, 80))
            self.screen.blit(img, (x, y))
            self.screen.blit(font.render(item.name, True,
                                         (255, 255, 255)), (x, y + 85))
            self.screen.blit(font.render(f"{item.cost} coins",
                                         True, (200, 200, 0)), (x, y + 110))

            # clickable item box
            rect = pg.Rect(x, y, 80, 80)
            if rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                shop.buy_item(inventory, i)

                # Draw "back" button
        back_button = Button("image/back_to_battle.png", (50, 300), 0.5)
        if back_button.draw(self.screen):
            return "back"

        # Instruction
        self.screen.blit(font.render(
            "Click an item to buy. Press [SPACE] to start battle.", True, (180, 180, 180)), (50, 400))

    def draw_inventory_screen(self, inventory):
        self.screen.fill(Config.get("DARKBLUE"))
        font = pg.font.Font(None, 28)
        title = font.render("Your Inventory", True, Config.get("WHITE"))
        self.screen.blit(title, (300, 50))

        # Display coins
        coin_text = font.render(
            f"Coins: {inventory.coin}", True, Config.get("YELLOW"))
        self.screen.blit(coin_text, (600, 50))

        # List items in inventory
        for i, item in enumerate(inventory.items):
            x = 50
            y = 120 + i * 100
            img = pg.image.load(item.image)
            img = pg.transform.scale(img, (80, 80))
            self.screen.blit(img, (x, y))
            self.screen.blit(font.render(item.name, True,
                                         Config.get("WHITE")), (x + 90, y + 20))

        # Draw "back" button
        back_button = Button("image/back_to_battle.png", (50, 300), 0.5)
        if back_button.draw(self.screen):
            return "back"

        self.screen.blit(font.render(
            "Press [SPACE] or click Back to return to battle.", True, Config.get("GRAY")), (50, 450))
