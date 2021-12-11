from component.componentClass import Component


class movementComponent(Component):
    def __init__(self, owner, type, system_owner, speed=3):
        self.owner = owner
        self.type = type
        self.system_owner = system_owner
        self.speed = speed
