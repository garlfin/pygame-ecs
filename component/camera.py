from component.componentClass import Component


class cameraComponent(Component):
    def __init__(self, owner, type, system_owner):
        self.owner = owner
        self.type = type
        self.system_owner = system_owner