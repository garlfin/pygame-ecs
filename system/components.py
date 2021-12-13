from enum import Enum
import system.mouseFollow
import system.movement
from system.transform import *
from system.sprite import *
from component.components import componentTypes
from system.backgroundSprite import *
from system.camera import *

componentDict = {
    componentTypes.camera: system.camera.cameraSystem,
    componentTypes.background: system.backgroundSprite.spriteSystem,
    componentTypes.transform: system.transform.transformSystem,
    componentTypes.sprite: system.sprite.spriteSystem,
    componentTypes.movement: system.movement.movementSystem,
    componentTypes.mouseFollow: system.mouseFollow.mouseSystem
}
