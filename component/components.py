from enum import Enum
from component import transform, sprite, movement, backgroundSprite


class componentTypes(Enum):
    transform = 1,
    physics = 2,
    sprite = 3,
    movement = 4,
    background = 5


componentDict = {
    componentTypes.transform: transform.transformComponent,
    componentTypes.sprite: sprite.spriteComponent,
    componentTypes.movement: movement.movementComponent,
    componentTypes.background: backgroundSprite.backgroundComponent
}
