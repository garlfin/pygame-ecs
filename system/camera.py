import pygame.transform
import system.system
import system.components
from component.components import componentTypes



class cameraSystem(system.system.System):

    def __init__(self):
        self.all_components = []
        self.current_camera = None

    def setCamera(self, reference):
        self.current_camera = reference

    def main(self, deltaTime, events, systemHandler=None):
        return None
