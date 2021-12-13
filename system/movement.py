import pygame.transform
import system.system
import system.components
import pygame
from component.components import componentTypes


class movementSystem(system.system.System):
    def main(self, deltaTime, events, systemHandler=None):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for component in self.all_components:
                component.owner.getComponent(componentTypes.transform).location[0] -= component.speed * deltaTime
                component.owner.getComponent(componentTypes.transform).direction = 1
        if keys[pygame.K_d]:
            for component in self.all_components:
                component.owner.getComponent(componentTypes.transform).location[0] += component.speed * deltaTime
                component.owner.getComponent(componentTypes.transform).direction = -1
        if keys[pygame.K_w]:
            for component in self.all_components:
                component.owner.getComponent(componentTypes.transform).location[1] -= component.speed * deltaTime
        if keys[pygame.K_s]:
            for component in self.all_components:
                component.owner.getComponent(componentTypes.transform).location[1] += component.speed * deltaTime
