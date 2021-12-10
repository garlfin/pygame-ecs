from component.componentClass import Component
import pygame

class spriteComponent(Component):
    def __init__(self, owner, type, system_owner, sprite, screen):
        self.owner = owner
        self.type = type
        self.system_owner = system_owner
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
        self.screen = screen


    def changeImage(self, sprite):
        self.sprite = pygame.image.load(sprite)
        self.rect = self.sprite.get_rect()
