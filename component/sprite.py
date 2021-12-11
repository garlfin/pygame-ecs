from component.componentClass import Component
import pygame

class spriteComponent(Component):
    def __init__(self, owner, type, system_owner, sprite, screen, alpha=True):
        self.owner = owner
        self.type = type
        self.image_path = sprite
        self.system_owner = system_owner
        self.sprite = pygame.image.load(sprite).convert_alpha() if alpha else pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.sprite.get_width()/2, self.sprite.get_height()/2)
        self.screen = screen
        self.original_size = (self.sprite.get_height(), self.sprite.get_height())


    def changeImage(self, sprite, alpha=True):
        self.sprite = pygame.image.load(sprite).convert_alpha() if alpha else pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
