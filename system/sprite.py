import system.system
import system.components
import pygame.transform
from component.components import componentTypes

def center(sprite, transform):
    return transform[0] - sprite.get_width() / 2, transform[1] - sprite.get_height() / 2


class spriteSystem(system.system.System):
    def main(self, deltaTime, events):
        for component in self.all_components:
            self.transform_component = component.owner.getComponent(componentTypes.transform)
            self.window_resize = component.screen.get_size()[0] / 1280
            # component.sprite = pygame.transform.rotate(component.sprite, component.rotation[0]
            # * component.direction
            component.sprite = pygame.transform.scale(component.sprite,
                                                                  (component.original_size[0] *
                                                                   self.transform_component.scale[0] * self.window_resize,
                                                                   component.original_size[1] *
                                                                   self.transform_component.scale[1] * self.window_resize))
            component.rect = component.sprite.get_rect()
            component.rect.center = (
                component.sprite.get_width() / 2, component.sprite.get_height() / 2)
            component.rect.x, component.rect.y = center(component.sprite, [
                self.transform_component.location[0] * self.window_resize, self.transform_component.location[1] * self.window_resize])
            component.screen.blit(component.sprite, component.rect)
