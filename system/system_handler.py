from system.components import componentDict as systemComponentDict
import component.components

class systemHandler:
    def __init__(self):
        self.all_systems = []

    def createSystem(self, type):
        self.all_systems.append(systemComponentDict.get(type)())

    def registerAllSystems(self):
        for system in systemComponentDict.items():
            self.createSystem(system[0])

    def getSystem(self, type_of):
        for system in self.all_systems:
            if type(system) == systemComponentDict.get(type_of):
                return system

    def iterateAllSystems(self, deltaTime, events):
        for system in self.all_systems:
            system.main(deltaTime, events)