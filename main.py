import pygame
from pygame.sprite import Group
from settings import Settings
from computer import Computer
from button import Button
from stats import Stats
import function as f
import sys


def main():

    # 初始化pygame
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Network Analog")

    #  创建computers组和routers组
    computers = f.create_computers(ai_settings, screen)
    routers, router_list = f.create_routers(ai_settings, screen)

    stats = Stats(ai_settings)

    #  创建board组
    boards = f.create_board(ai_settings, screen, stats)

    #  创建按钮
    button_draw_line = Button(ai_settings, screen, "draw line", 100, 440)
    button_get_table = Button(ai_settings, screen, "get table", 250, 440)
    button_clean = Button(ai_settings, screen, "clean all", 400, 440)

    f.set_con()

    while True:
        boards = f.create_board(ai_settings, screen, stats)
        f.check_event(button_draw_line, button_get_table, button_clean, screen, ai_settings, stats)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        f.update_screen(ai_settings, screen, computers, routers, button_draw_line, button_get_table, button_clean, boards, stats)


main()