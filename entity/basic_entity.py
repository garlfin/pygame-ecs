import entity.entity
from component.components import componentTypes, componentDict
from system.components import componentDict as systemComponentDict


class basicEntity(entity.entity.Entity):
    def __init__(self, system_handler):
        self.owner = None
        self.components = []
        self.tempargs = []
        self.system_handler = system_handler
        self.addComponent(componentTypes.transform)
        self.addComponent(componentTypes.sprite, ["resources/images/placeholder.png"])
