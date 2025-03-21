import pygame as pg


class Sound:
    def __init__(self, sound_file, loop, start, volume):
        self.sound_file = sound_file
        self.loop = loop
        self.start = start
        self.volume = volume

    def play(self):
        pg.mixer.init()
        pg.mixer.music.load(self.sound_file)
        pg.mixer.music.set_volume(self.volume)
        pg.mixer.music.play(self.loop, self.start)
