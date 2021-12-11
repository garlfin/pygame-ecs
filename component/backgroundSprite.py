import pygame.image
import pygame.transform
from component.componentClass import Component


class backgroundComponent(Component):
    def __init__(self, owner, type, system_owner, sprite, screen, tile=1):
        self.owner = owner
        self.type = type
        self.screen = screen
        self.system_owner = system_owner
        self.tile = tile
        #self.sprite = pygame.transform.scale(pygame.image.load(sprite), (self.tile, self.tile))
        self.sprite = pygame.image.load(sprite)
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite.get_width()*tile,self.sprite.get_height()*tile))
        self.render_sprite = self.sprite
        self.rect = self.sprite.get_rect()

