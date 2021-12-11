import pygame
import sys

import entity.entity
import system.system_handler
from component.components import componentTypes
from map_loader.map import mapLoader


def hexToColor(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    fill_color = hexToColor('FFFFFF')
    pygame.display.set_caption("Garlfin's Game")
    pygame.display.set_icon(pygame.image.load("resources/images/smiley.png"))

    system_handler = system.system_handler.systemHandler()
    system_handler.registerAllSystems()
    test_map = mapLoader("map_loader/maps/map1.json", system_handler=system_handler, screen=screen)

    ticksLastFrame = 0
    screen_size = (width, height)
    window_resize = 1
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
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
