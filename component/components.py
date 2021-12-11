from enum import Enum
from component import transform, sprite, movement

class componentTypes(Enum):
    transform = 1,
    physics = 2,
    sprite = 3,
    movement = 4


componentDict = {
    componentTypes.transform: transform.transformComponent,
    componentTypes.sprite: sprite.spriteComponent,
    componentTypes.movement: movement.movementComponent
}
