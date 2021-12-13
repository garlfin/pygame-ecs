class System:
    def __init__(self):
        self.all_components = []

    def addComponent(self, component_to_add):
        self.all_components.append(component_to_add)
        return component_to_add

    def removeComponent(self, component_to_remove):
        self.all_components.remove(component_to_remove)
        return component_to_remove

