import pygame.transform
import system.system
import system.components
import pygame
from component.components import componentTypes


class mouseSystem(system.system.System):
    def main(self, deltaTime, events, systemHandler=None):
        self.mouse = pygame.mouse
        for component in self.all_components:
            component.owner.getComponent(componentTypes.sprite).use_window_size = False
            if abs(self.mouse.get_rel()[0]+self.mouse.get_rel()[1]) > 0:
                component.owner.getComponent(componentTypes.transform).location = self.mouse.get_pos()