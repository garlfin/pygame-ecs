from enum import Enum
from component import transform, sprite

class componentTypes(Enum):
    transform = 1,
    physics = 2,
    sprite = 3


componentDict = {
    componentTypes.transform: transform.transformComponent,
    componentTypes.sprite: sprite.spriteComponent
}
