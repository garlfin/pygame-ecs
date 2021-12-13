import pygame
import sys

import entity.entity
import entity.basic_entity
import system.system_handler
from component.components import componentTypes
from map_loader.map import mapLoader
from pygame.time import Clock as GameClock



def hexToColor(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    size = width, height = 1280, 720
    fps = 60
    flags = pygame.RESIZABLE
    screen = pygame.display.set_mode(size, flags, vsync=1)
    fill_color = hexToColor('FFFFFF')
    pygame.display.set_caption("Garlfin's Game")
    pygame.display.set_icon(pygame.image.load("resources/images/smiley.png"))

    system_handler = system.system_handler.systemHandler()
    system_handler.registerAllSystems()

    test_map = mapLoader("map_loader/maps/map1.json", system_handler=system_handler)
    pygame.mouse.set_visible(False)
    mouse_entity = entity.basic_entity.basicEntity(system_handler)
    mouse_entity.getComponent(componentTypes.sprite).changeImage("resources/images/cursor.png")
    mouse_entity.addComponent(componentTypes.mouseFollow)

    ticksLastFrame = 0
    screen_size = (width, height)
    window_resize = 1
    gameClock = GameClock()
    while True:
        dt = gameClock.tick_busy_loop(fps) / 1000
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h),
                                                 pygame.RESIZABLE)
                for item in system_handler.getSystem(componentTypes.sprite).all_components:
                    item.changeImage(item.image_path)
                screen_size = (screen.get_width(), screen.get_height())
            window_resize = screen.get_size()[0] / 1280
        ticks = pygame.time.get_ticks()
        ticksLastFrame = ticks
        screen.fill(fill_color)
        system_handler.iterateAllSystems(dt, events)
        pygame.display.flip()
