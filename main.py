import entity.entity
import system.system_handler
from component.components import componentTypes
import sys, pygame


def hexToColor(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size, pygame.RESIZABLE, vsync=1)

    fill_color = hexToColor('FFFFFF')
    pygame.display.set_caption("game lolz")

    system_handler = system.system_handler.systemHandler()
    system_handler.registerAllSystems()
    test_entity_1 = entity.entity.Entity(system_handler)
    test_entity_1.addComponent(componentTypes.transform)
    test_entity_1.getComponent(componentTypes.transform).location = (screen.get_width() / 2, screen.get_height() / 2, 0)
    test_entity_1.getComponent(componentTypes.transform).scale = (2, 2, 0)
    test_entity_1.getComponent(componentTypes.transform).rotation = (1, 0, 0)
    test_entity_1.addComponent(componentTypes.sprite, ["resources/images/smiley.png", screen, True])
    test_entity_1.getComponent(componentTypes.sprite).original_size = (269, 188)

    ticksLastFrame = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                screen = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                test_entity_1.getComponent(componentTypes.transform).location = (
                screen.get_width() / 2, screen.get_height() / 2, 0)
        ticks = pygame.time.get_ticks()
        dt = (ticks - ticksLastFrame) / 1000.0
        ticksLastFrame = ticks
        screen.fill(fill_color)
        system_handler.iterateAllSystems(dt)
        pygame.display.flip()
