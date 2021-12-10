import system.components
from component.components import componentTypes

class transformSystem(system.system.System):
    def main(self, deltaTime):
       for component in self.all_components:
            self.temp_sprite_item = component.owner.getComponent(componentTypes.sprite)
            self.temp_sprite_item.rect.x, self.temp_sprite_item.rect.y = component.location[0] - self.temp_sprite_item.rect.size[0]/2, component.location[1] - self.temp_sprite_item.rect.size[1]/2
