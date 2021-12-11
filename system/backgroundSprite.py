import pygame.transform

import system.system
import system.components
import math

class spriteSystem(system.system.System):
    def main(self, deltaTime, events):
        for component in self.all_components:
            self.window_resize = component.screen.get_size()[0] / 1280
            component.render_sprite = pygame.transform.scale(component.sprite, (component.sprite.get_width()*self.window_resize, component.sprite.get_height()*self.window_resize))
            self.repeat_x = int(math.ceil(component.screen.get_width() / component.render_sprite.get_width()))
            self.repeat_y = int(math.ceil(component.screen.get_height() / component.render_sprite.get_height()))
            self.x = 0
            self.y = 0
            for x in range(self.repeat_x):
                self.y = 0
                component.rect.x = self.x
                for y in range(self.repeat_y):
                    component.rect.y = self.y
                    component.screen.blit(component.render_sprite, component.rect)
                    self.y += component.render_sprite.get_height()
                self.x += component.render_sprite.get_width()

