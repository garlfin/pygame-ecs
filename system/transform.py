import pygame.transform
import system.system
import system.components
from component.components import componentTypes

class transformSystem(system.system.System):
    def main(self, deltaTime):
       for component in self.all_components:
           self.temp_sprite_item = component.owner.getComponent(componentTypes.sprite)
           self.window_resize = self.temp_sprite_item.screen.get_size()[0]/1280
           # self.temp_sprite_item.sprite = pygame.transform.rotate(self.temp_sprite_item.sprite, component.rotation[0])
           self.temp_sprite_item.sprite = pygame.transform.scale(self.temp_sprite_item.sprite,
                                                                 (self.temp_sprite_item.original_size[0] *
                                                                  component.scale[0] * self.window_resize,
                                                                  self.temp_sprite_item.original_size[1] *
                                                                  component.scale[1] * self.window_resize))
           self.temp_sprite_item.rect = self.temp_sprite_item.sprite.get_rect()
           self.temp_sprite_item.rect.x, self.temp_sprite_item.rect.y = component.location[0] - \
                                                                        self.temp_sprite_item.rect.size[0] / 2, \
                                                                        component.location[1] - \
                                                                        self.temp_sprite_item.rect.size[1] / 2
