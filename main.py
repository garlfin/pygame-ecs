import entity.entity
import system.system_handler
from component.components import componentTypes
import sys, pygame


def hexToColor(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size, vsync=1)

    white = hexToColor('FFFFFF')
    pygame.display.set_caption("game lolz")

    system_handler = system.system_handler.systemHandler()
    system_handler.registerAllSystems()
    test_entity_1 = entity.entity.Entity(system_handler)
    test_entity_1.addComponent(componentTypes.transform)
    test_entity_1.getComponent(componentTypes.transform).location = (1280/2, 720/2, 0)
    test_entity_1.addComponent(componentTypes.sprite, ["test.jpg", screen])
    print(test_entity_1.getComponent(componentTypes.transform).getSystem())

    ticksLastFrame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ticks = pygame.time.get_ticks()
        dt = (ticks - ticksLastFrame) / 1000.0
        ticksLastFrame = ticks
        screen.fill(white)
        system_handler.iterateAllSystems(dt)
        pygame.display.flip()
