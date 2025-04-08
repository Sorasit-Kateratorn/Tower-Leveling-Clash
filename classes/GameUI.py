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

        title_text = font.render(f'Tower Leveling Clash', True, Config.get("BLACK"))
        title_text2 = font.render(f'Tower Leveling Clash', True, Config.get("DARKBROWN"))

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
        title = title_font.render("Select Your Character",True, Config.get("BLACK"))

        title_text2 = title_font.render(f'Select Your Character', True, Config.get("DARKBROWN"))
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

    def get_battle_background(self, floor):
        if floor == 1:
            return Background("image/Backgroundgrass.png", [0, 0])
        elif floor == 2:
            return Background("image/Backgroundsnow.png", [0, 0])
        
        else:
            return Background("image/Backgroundcastle.png", [0, 0])
        
        
    def draw_battle_screen(self, player, enemies, battle_log="", floor=1):
        self.screen.fill(Config.get('BLACK'))
        font = pg.font.Font("font/PixelifySans-Bold.ttf", 20)
        battle_bg = self.get_battle_background(floor)


        battle_bg.draw(self.screen)
        # Draw player character on the left
        player_img = pg.image.load(player.image)
        player_img = pg.transform.scale(player_img, (120, 120))
        self.screen.blit(player_img, (50, 220))

        player_name = font.render(player.name, True, Config.get("GREEN"))
        self.screen.blit(player_name, (50, 200))
        
        floor_text = font.render(f"Floor: {floor}", True, Config.get("YELLOW"))
        self.screen.blit(floor_text, (375,0))

        # Draw player stats
        stats = f"HP: {player.health}  ATK: {player.attack}  DEF: {player.defense}"
        stats_text = font.render(stats, True, Config.get("GREEN"))
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

        items_per_row = 4
        item_width = 100
        item_height = 150
        padding_x = 40
        padding_y = 30

        start_x = 60
        start_y = 120

        message = ""

        # Helper to truncate long names
        def truncate_text(text, max_length=12):
            return text if len(text) <= max_length else text[:max_length - 3] + "..."

        for i, item in enumerate(shop.items_in_shop):
            row = i // items_per_row
            col = i % items_per_row
            x = start_x + col * (item_width + padding_x)
            y = start_y + row * (item_height + padding_y)

            # Draw item image
            img = pg.image.load(item.image)
            img = pg.transform.scale(img, (80, 80))
            self.screen.blit(img, (x, y))

            # Centered item name
            name_text = truncate_text(item.name)
            name_surface = font.render(name_text, True, Config.get("WHITE"))
            name_rect = name_surface.get_rect(center=(x + 40, y + 90))
            self.screen.blit(name_surface, name_rect)

            # Centered coin cost
            cost_surface = font.render(f"{item.cost} coins", True, Config.get("YELLOW"))
            cost_rect = cost_surface.get_rect(center=(x + 40, y + 115))
            self.screen.blit(cost_surface, cost_rect)

            # clickable item box
            rect = pg.Rect(x, y, 80, 80)
            if rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                if not shop.buy_item(inventory, i):
                    message = "Not enough coins!"

        if message:
            error_surface = font.render(message, True, Config.get("RED"))
            self.screen.blit(error_surface, (50, 480))

        back_button = Button("image/back_to_battle.png", (600, 300), 0.5)
        if back_button.draw(self.screen):
            return "back"


        self.screen.blit(font.render("Click an item to buy. Press [SPACE] or click Back button to start battle.", True, (180, 180, 180)), (50, 550))

    def draw_inventory_screen(self, inventory):
        self.screen.fill(Config.get("DARKBLUE"))
        font = pg.font.Font(None, 28)
        title = font.render("Your Inventory", True, Config.get("WHITE"))
        self.screen.blit(title, (300, 50))


        coin_text = font.render(f"Coins: {inventory.coin}", True, Config.get("YELLOW"))
        self.screen.blit(coin_text, (600, 50))
        
        
        items_per_row = 4
        item_width = 100
        item_height = 150
        padding_x = 40
        padding_y = 30

        start_x = 60
        start_y = 120

        selected_item = None
        # List items in inventory
        for i, item in enumerate(inventory.items):
            row = i // items_per_row
            col = i % items_per_row
            
            x = start_x + col * (item_width + padding_x)
            y = start_y + row * (item_height + padding_y)
            
            img = pg.image.load(item.image)
            img = pg.transform.scale(img, (80, 80))
            self.screen.blit(img, (x, y))
            
            
            name_surface =font.render(item.name, True,Config.get("WHITE"))
            name_rect = name_surface.get_rect(center=(x+40,y+90))
            self.screen.blit(name_surface, name_rect)

            # clickable item box
            rect = pg.Rect(x, y, 80, 80)
            if rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
                selected_item = item  # Save this clicked item
        
        
        
        
        back_button = Button("image/back_to_battle.png", (600, 300), 0.5)
        if back_button.draw(self.screen):
            return "back"

        elif selected_item:
            return selected_item

        self.screen.blit(font.render("Press [SPACE] or click Back button to return to battle.", True, Config.get("GRAY")), (50, 550))
        
    def draw_item_action_popup(self, item):
        self.screen.fill(Config.get("DARKBLUE"))
        font = pg.font.Font("font/PixelifySans-Bold.ttf", 24)

        prompt = font.render(f"Do you want to use this {item.name} or discard it?", True, Config.get("YELLOW"))
        self.screen.blit(prompt, (50, 100))

        item_img = pg.image.load(item.image)
        item_img = pg.transform.scale(item_img, (100, 100))
        self.screen.blit(item_img, (350, 250))

        use_button = Button("image/use_item.png", (150, 400), 0.5)
        discard_button = Button("image/discard_items.png", (550, 400), 0.5)
        back_button = Button("image/inventory.png", (350, 450), 0.5)

        if use_button.draw(self.screen):
            return "use"
        if discard_button.draw(self.screen):
            return "discard"
        if back_button.draw(self.screen):
            return "back"

        return None
