import entity.entity
from component.components import componentTypes, componentDict
from system.components import componentDict as systemComponentDict


class basicEntity(entity.entity.Entity):
    def __init__(self, system_handler, screen):
        self.owner = None
        self.components = []
        self.tempargs = []
        self.system_handler = system_handler
        self.addComponent(componentTypes.transform)
        self.screen = screen
        self.addComponent(componentTypes.sprite, ["resources/images/placeholder.png", self.screen])

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return None