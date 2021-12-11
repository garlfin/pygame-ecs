from component.components import componentTypes, componentDict
from system.components import componentDict as systemComponentDict


class Entity:
    def __init__(self, system_handler):
        self.owner = None
        self.components = []
        self.tempargs = []
        self.system_handler = system_handler

    def addComponent(self, type, args=[]):
        if not self.getComponent(type):
            self.tempargs = [self, type, self.getSystem(type)]
            for arg in args:
                self.tempargs.append(arg)
            self.components.append(self.getSystem(type).addComponent(componentDict.get(type)(*self.tempargs)))

    def getSystem(self, type_of):
        for system in self.system_handler.all_systems:
            if type(system) == systemComponentDict.get(type_of):
                return system
        return None

    def getComponent(self, type_of):
        for component in self.components:
            if type(component) == componentDict.get(type_of):
                return component
        return None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return None
