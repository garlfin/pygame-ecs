import json

import entity.basic_entity
from component.components import componentTypes
import entity.entity
import pygame.mixer

jsonToMap = {
    'transform': componentTypes.transform,
    'movement': componentTypes.movement,
    'sprite': componentTypes.sprite,
    'camera': componentTypes.camera
}


class mapLoader:
    def __init__(self, file, system_handler):
        self.system_handler = system_handler
        self.all_entity = []
        with open(file) as f:
            self.data = json.load(f)
            for map_part in self.data:
                if self.data[map_part]['type'] == "basic_entity":
                    with entity.basic_entity.basicEntity(system_handler) as iteration_entity:
                        iteration_entity.getComponent(componentTypes.transform).location = self.data[map_part][
                            'transform'].get('location')
                        iteration_entity.getComponent(componentTypes.transform).scale = self.data[map_part][
                            'transform'].get('scale')
                        iteration_entity.getComponent(componentTypes.sprite).changeImage(
                            self.data[map_part]['sprite'] if self.data[map_part].get(
                                'sprite') else "resources/images/placeholder.png")
                        if self.data[map_part].get('sprite_custom_size'):
                            iteration_entity.getComponent(componentTypes.sprite).setCustomSize(
                                self.data[map_part]['sprite_custom_size'])
                        self.all_entity.append(iteration_entity)
                        if self.data[map_part].get('components'):
                            for component in self.data[map_part].get('components'):
                                iteration_entity.addComponent(jsonToMap.get(component.get("type")),
                                                              component.get('args'))
                                if component.get("type") == "camera":
                                    system_handler.getSystem(componentTypes.camera).setCamera(iteration_entity.getComponent(componentTypes.camera))
                elif self.data[map_part]['type'] == "background":
                    with entity.entity.Entity(system_handler) as iteration_entity:
                        iteration_entity = entity.entity.Entity(system_handler)
                        iteration_entity.addComponent(componentTypes.background,
                                                      [self.data[map_part]['sprite'] if self.data[map_part].get("sprite") else "resources/images/placeholder.png",
                                                       self.data[map_part]['tile']])
                        self.background_music = pygame.mixer.Sound(self.data[map_part]['background_music'])
                        self.background_music.set_volume(self.data[map_part]['background_music_volume']/100)
                        self.background_music.play(-1)  # On Loop, Forever  >:)
