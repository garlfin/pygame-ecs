import pygame.image
import pygame.transform
from component.componentClass import Component


class backgroundComponent(Component):
    def __init__(self, owner, type, system_owner, sprite, tile=1):
        self.owner = owner
        self.type = type
        self.screen = pygame.display.get_surface()
        self.system_owner = system_owner
        self.tile = 1 / tile
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width()*self.tile,self.sprite.get_height()*self.tile))
        self.render_sprite = self.sprite
        self.rect = self.sprite.get_rect()

