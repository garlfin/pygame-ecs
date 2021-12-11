class Component:
    def __init__(self, owner, type, system_owner):
        self.owner = owner
        self.type = type
        self.system_owner = system_owner

    def getSystem(self):
        return self.system_owner
