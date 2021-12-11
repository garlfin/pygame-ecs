import entity.basic_entity
import system.system_handler
from component.components import componentTypes
import sys, pygame


def hexToColor(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    fill_color = hexToColor('FFFFFF')
    pygame.display.set_caption("Garlfins Game")
    pygame.display.set_icon(pygame.image.load("resources/images/smiley.png"))

    system_handler = system.system_handler.systemHandler()
    system_handler.registerAllSystems()
    test_entity_1 = entity.basic_entity.basicEntity(system_handler, screen)
    test_entity_1.getComponent(componentTypes.transform).location = [screen.get_width() / 2, screen.get_height() / 2, 0]
    test_entity_1.getComponent(componentTypes.transform).scale = [1, 1]
    test_entity_1.getComponent(componentTypes.sprite).changeImage("resources/images/smiley.png")
    test_entity_1.getComponent(componentTypes.sprite).setCustomSize((269, 188))
    test_entity_1.addComponent(componentTypes.movement, [100])

    with entity.basic_entity.basicEntity(system_handler, screen) as tree_entity:
        tree_entity.getComponent(componentTypes.transform).location = [100, 300]
        tree_entity.getComponent(componentTypes.transform).scale = [0.5, 0.5]
        tree_entity.getComponent(componentTypes.sprite).changeImage("resources/images/tree.png")

    ticksLastFrame = 0
    screen_size = (width, height)
    window_resize = 1
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                # There's some code to add back window content here.
                screen = pygame.display.set_mode((event.w, event.h),
                                                  pygame.RESIZABLE)
                # test_entity_1.getComponent(componentTypes.transform).location = [
                # screen.get_width() / 2, screen.get_height() / 2]
                for item in system_handler.getSystem(componentTypes.sprite).all_components:
                    item.changeImage(item.image_path)
                screen_size = (screen.get_width(), screen.get_height())
            window_resize = screen.get_size()[0] / 1280
        ticks = pygame.time.get_ticks()
        dt = (ticks - ticksLastFrame) / 1000.0
        ticksLastFrame = ticks
        screen.fill(fill_color)
        system_handler.iterateAllSystems(dt, events)
        pygame.display.flip()
