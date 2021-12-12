import pygame.image
import pygame.transform
from component.componentClass import Component


class mouseComponent(Component):
    def __init__(self, owner, type, system_owner):
        self.owner = owner
        self.type = type
        self.system_owner = system_owner