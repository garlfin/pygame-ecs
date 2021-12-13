import pygame.transform
from component.components import componentTypes
import system.system
import system.components
import math

class spriteSystem(system.system.System):
    def main(self, deltaTime, events, systemHandler=None):
        if systemHandler.getSystem(componentTypes.camera).current_camera:
            self.currentCameraPos = systemHandler.getSystem(
                componentTypes.camera).current_camera.owner.getComponent(componentTypes.transform).location
        else:
            self.currentCameraPos = [0, 0]
        self.window_resize = 1
        for event in events:
            if event.type == pygame.VIDEORESIZE:
                self.window_resize = pygame.display.get_surface().get_size()[0] / 1280
        for component in self.all_components:
            component.render_sprite = pygame.transform.scale(component.sprite, (component.sprite.get_width()*self.window_resize, component.sprite.get_height()*self.window_resize))
            self.repeat_x = int(math.ceil(component.screen.get_width() / component.render_sprite.get_width()))
            self.repeat_y = int(math.ceil(component.screen.get_height() / component.render_sprite.get_height()))
            self.x = 0
            self.y = 0
            self.temp_sprite = pygame.surface.Surface(pygame.display.get_surface().get_size())
            for x in range(self.repeat_x):
                self.y = 0
                component.rect.x = (self.x - self.currentCameraPos[0]) % (pygame.display.get_surface().get_size()[0]/2)
                for y in range(self.repeat_y):
                    component.rect.y = (self.y - self.currentCameraPos[1]) % (pygame.display.get_surface().get_size()[1])
                    self.temp_sprite.blit(component.render_sprite, component.rect)
                    self.y += component.render_sprite.get_height()
                self.x += component.render_sprite.get_width()
            component.screen.blit(self.temp_sprite, self.temp_sprite.get_rect())
