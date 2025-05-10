import pygame as pg


class Button(pg.sprite.Sprite):
    def __init__(self, image_file, location, scale):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(image_file)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.image = pg.transform.scale(
            self.image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = location
        self.clicked = False

    def draw(self, screen):
        # get mouse position
        mouse_pos = pg.mouse.get_pos()
        action = False

        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
