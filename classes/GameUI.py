# เปิดการด์เรียก pygameเเล้วเรียกfunction take damage ของคลาส enermyของเรา
import pygame as pg
from classes.Background import *
from classes.GameConfig import *
from classes.Button import *
from classes.Sound import *
from classes.Player import *

# TODO gameUI uml


def draw_home_screen(screen):
    screen.fill(Config.get('WHITE'))
    font = pg.font.Font("font/PixelifySans-Bold.ttf", 50)
    home_bg = Background("image/Backgroundcastle.png", [0, 0])
    start_button = Button("image/playbutton.png", [325, 300], 0.5)
    quit_button = Button("image/quitbutton.png", [325, 400], 0.5)
    # sound = Sound("sound/adventure-music-229534.mp3", -1, 0, 0.1)

    title_text = font.render(
        f'Tower Leveling Clash', True, Config.get("BLACK"))
    title_text2 = font.render(
        f'Tower Leveling Clash', True, Config.get("DARKBROWN"))

    home_bg.draw(screen)
    start_click = start_button.draw(screen)
    quit_click = quit_button.draw(screen)
    screen.blit(title_text, (158, 200))
    screen.blit(title_text2, (155, 200))
    # sound.play()

    if start_click:
        return "start"

    elif quit_click:
        return "quit"


characters = [Wonderwoman(), Wizard(), Omen(), Hulk(), Predator()]
positions = [(50, 200), (250, 200), (450, 200), (650, 200), (850, 200)]

# Create buttons ONCE (outside the function)
character_buttons = [Button(char.image, pos, 1.0)
                     for char, pos in zip(characters, positions)]


def draw_selected_character_screen(screen):
    screen.fill(Config.get('WHITE'))
    title_font = pg.font.Font("font/PixelifySans-Bold.ttf", 50)
    name_font = pg.font.Font("font/PixelifySans-Bold.ttf", 20)
    home_bg = Background("image/Backgroundcastle.png", [0, 0])
    title = title_font.render("Select Your Character",
                              True, Config.get("BLACK"))

    title_text2 = title_font.render(
        f'Select Your Character', True, Config.get("DARKBROWN"))
    home_bg.draw(screen)
    screen.blit(title, (158, 100))
    screen.blit(title_text2, (155, 100))

    selected_character = None

    for i, button in enumerate(character_buttons):
        if button.draw(screen):  # If clicked
            selected_character = characters[i]

        name_text = name_font.render(
            characters[i].name, True, Config.get("BLACK"))
        name_rect = name_text.get_rect(
            center=(button.rect.centerx, button.rect.bottom + 10))
        screen.blit(name_text, name_rect)
    return selected_character


def draw_battle_screen(screen, player, enemies, battle_log=""):
    screen.fill(Config.get('BLACK'))
    font = pg.font.Font("font/PixelifySans-Bold.ttf", 20)
    battle_bg = Background("image/Backgroundgrass.png", [0, 0])

    battle_bg.draw(screen)
    # Draw player character on the left
    player_img = pg.image.load(player.image)
    player_img = pg.transform.scale(player_img, (120, 120))
    screen.blit(player_img, (50, 220))

    player_name = font.render(player.name, True, Config.get("WHITE"))
    screen.blit(player_name, (50, 200))

    # Draw player stats
    stats = f"HP: {player.health}  ATK: {player.attack}  DEF: {player.defense}"
    stats_text = font.render(stats, True, (255, 255, 255))
    screen.blit(stats_text, (50, 350))

    # Draw enemies
    for i, enemy in enumerate(enemies):
        x = 400 + i * 140
        enemy_img = pg.image.load(enemy.image)
        enemy_img = pg.transform.scale(enemy_img, (100, 100))
        screen.blit(enemy_img, (x, 220))

        enemy_name = font.render(enemy.name, True, Config.get("RED"))
        screen.blit(enemy_name, (x, 200))

        stats_health = f"HP: {enemy.health}"
        stats_attack = f"ATK: {enemy.attack}"
        stats_defence = f"DEF: {enemy.defense}"
        stats_text1 = font.render(stats_health, True, Config.get("RED"))
        stats_text2 = font.render(stats_attack, True, Config.get("RED"))
        stats_text3 = font.render(stats_defence, True, Config.get("RED"))
        screen.blit(stats_text1, (x, 330))
        screen.blit(stats_text2, (x, 375))
        screen.blit(stats_text3, (x, 410))
        # Draw battle log
    log_text = font.render(battle_log, True, Config.get("YELLOW"))
    screen.blit(log_text, (50, 100))


def draw_game_over(screen):
    screen.fill(Config.get("BLACK"))
    font = pg.font.Font("font/PixelifySans-Bold.ttf", 60)
    text = font.render("GAME OVER", True, Config.get("RED"))
    screen.blit(text, (300, 250))


def draw_game_victory(screen):
    screen.fill(Config.get("WHITE"))
    font = pg.font.Font("font/PixelifySans-Bold.ttf", 60)
    text = font.render("VICTORY!", True,  Config.get("RED"))
    screen.blit(text, (300, 250))
