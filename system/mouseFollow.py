import pygame.transform
import system.system
import system.components
import pygame
from component.components import componentTypes


class mouseSystem(system.system.System):
    def main(self, deltaTime, events):
        for component in self.all_components:
            component.owner.getComponent(componentTypes.transform).location = pygame.mouse.get_pos()