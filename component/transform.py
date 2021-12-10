from component.componentClass import Component

class transformComponent(Component):
    def __init__(self, owner, type, system_owner, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
        self.owner = owner
        self.location = location
        self.rotation = rotation
        self.scale = scale
        self.type = type
        self.system_owner = system_owner
