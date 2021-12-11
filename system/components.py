from enum import Enum

import system.movement
from system.transform import *
from system.sprite import *
from component.components import componentTypes

componentDict = {
    componentTypes.transform: system.transform.transformSystem,
    componentTypes.sprite: system.sprite.spriteSystem,
    componentTypes.movement: system.movement.movementSystem
}
