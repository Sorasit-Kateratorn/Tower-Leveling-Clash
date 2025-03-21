# เปิดการด์เรียก pygameเเล้วเรียกfunction take damage ของคลาส enermyของเรา
import pygame as pg
from classes.Background import *
from classes.GameConfig import *
from classes.Button import *
from classes.Sound import *


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
        f'Tower Leveling Clash', True, Config.get("DarkBrown"))

    home_bg.draw(screen)
    start_button.draw(screen)
    quit_button.draw(screen)
    screen.blit(title_text, (158, 200))
    screen.blit(title_text2, (155, 200))
    # sound.play()
