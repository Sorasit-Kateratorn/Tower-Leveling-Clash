import pygame as pg


class Background(pg.sprite.Sprite):
    def __init__(self, image_file, location):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.topleft = location

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
