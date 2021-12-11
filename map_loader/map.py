import json

import entity.basic_entity
from component.components import componentTypes
import entity.entity

jsonToMap = {
    'transform': componentTypes.transform,
    'movement': componentTypes.movement,
    'sprite': componentTypes.sprite
}


class mapLoader:
    def __init__(self, file, system_handler, screen):
        self.system_handler = system_handler
        self.screen = screen
        self.all_entity = []
        with open(file) as f:
            self.data = json.load(f)
            for map_part in self.data:
                if self.data[map_part]['type'] == "basic_entity":
                    with entity.basic_entity.basicEntity(system_handler, screen) as iteration_entity:
                        iteration_entity.getComponent(componentTypes.transform).location = self.data[map_part][
                            'transform'].get('location')
                        iteration_entity.getComponent(componentTypes.transform).scale = self.data[map_part][
                            'transform'].get('scale')
                        iteration_entity.getComponent(componentTypes.sprite).changeImage(
                            self.data[map_part]['sprite'] if self.data[map_part][
                                'sprite'] else "resources/images/placeholder.png")
                        if self.data[map_part].get('sprite_custom_size'):
                            iteration_entity.getComponent(componentTypes.sprite).setCustomSize(
                                self.data[map_part]['sprite_custom_size'])
                        self.all_entity.append(iteration_entity)
                        if self.data[map_part].get('components'):
                            for component in self.data[map_part].get('components'):
                                iteration_entity.addComponent(jsonToMap.get(component.get("type")),
                                                              component.get('args'))
                elif self.data[map_part]['type'] == "background":
                    with entity.entity.Entity(system_handler) as iteration_entity:
                        iteration_entity = entity.entity.Entity(system_handler)
                        iteration_entity.addComponent(componentTypes.background,
                                                      [self.data[map_part]['sprite'], screen, self.data[map_part]['tile']])