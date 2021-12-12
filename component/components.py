from enum import Enum
from component import transform, sprite, movement, backgroundSprite, mouseFollower


class componentTypes(Enum):
    transform = 1,
    physics = 2,
    sprite = 3,
    movement = 4,
    background = 5,
    mouseFollow = 6


componentDict = {
    componentTypes.transform: transform.transformComponent,
    componentTypes.sprite: sprite.spriteComponent,
    componentTypes.movement: movement.movementComponent,
    componentTypes.background: backgroundSprite.backgroundComponent,
    componentTypes.mouseFollow: mouseFollower.mouseComponent
}
