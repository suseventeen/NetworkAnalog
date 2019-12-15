import pygame
import sys
from pygame.sprite import Group
from computer import Computer
from router import Router
from board import Board

router_list = []
computer_list = []
boards = []


def update_screen(ai_settings, screen, computers, routers, button1, button2, button3, boards):
    """刷新屏幕"""
    #  每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)

    #  重绘所有computer、router、board
    for computer in computers.sprites():
        computer.blitme()
    for router in routers.sprites():
        router.blitme()
    for board in boards:
        board.draw_board()
    pygame.draw.line(screen, (130, 210, 255), (0, 498), (1200, 498), 8)
    pygame.draw.line(screen, (130, 210, 255), (0, 650), (402, 650), 8)
    pygame.draw.line(screen, (130, 210, 255), (402, 600), (1200, 600), 8)
    pygame.draw.line(screen, (130, 210, 255), (402, 700), (1200, 700), 8)
    pygame.draw.line(screen, (130, 210, 255), (0, 798), (1200, 798), 8)
    pygame.draw.line(screen, (130, 210, 255), (402, 498), (402, 800), 8)
    pygame.draw.line(screen, (130, 210, 255), (668, 498), (668, 800), 8)
    pygame.draw.line(screen, (130, 210, 255), (934, 498), (934, 800), 8)
    button1.draw_button()
    button2.draw_button()
    button3.draw_button()
    draw_con(screen)

    #  让最近绘制的屏幕可见
    pygame.display.flip()


def create_computers(ai_settings, screen):
    """创建计算机组"""
    computers = Group()
    # for rate in range(4):
    #     computer_l = Computer(ai_settings, screen, 40, 40+160*rate)
    #     computer_r = Computer(ai_settings, screen, 1100, 40 + 160 * rate)
    #     computers.add(computer_l)
    #     computers.add(computer_r)
    computer_l = Computer(ai_settings, screen, 40, 190, 'Alice')
    computer_r = Computer(ai_settings, screen, 1100, 190, 'Bob')
    computers.add(computer_l)
    computers.add(computer_r)
    computer_list.append(computer_l)
    computer_list.append(computer_r)
    return computers


def create_routers(ai_settings, screen):
    """创建路由器组"""
    routers = Group()
    router_1 = Router(ai_settings, screen, 300, 40, 'A')
    router_2 = Router(ai_settings, screen, 580, 40, 'B')
    router_3 = Router(ai_settings, screen, 860, 40, 'C')
    router_4 = Router(ai_settings, screen, 300, 190, 'D')
    router_5 = Router(ai_settings, screen, 580, 190, 'E')
    router_6 = Router(ai_settings, screen, 860, 190, 'F')
    router_7 = Router(ai_settings, screen, 300, 340, 'G')
    router_8 = Router(ai_settings, screen, 580, 340, 'H')
    router_9 = Router(ai_settings, screen, 860, 340, 'I')
    routers.add(router_1)
    routers.add(router_2)
    routers.add(router_3)
    routers.add(router_4)
    routers.add(router_5)
    routers.add(router_6)
    routers.add(router_7)
    routers.add(router_8)
    routers.add(router_9)
    router_list.append(router_1)
    router_list.append(router_2)
    router_list.append(router_3)
    router_list.append(router_4)
    router_list.append(router_5)
    router_list.append(router_6)
    router_list.append(router_7)
    router_list.append(router_8)
    router_list.append(router_9)

    return routers, router_list


def create_board(ai_settings, screen):
    boards = []
    #  创建输入输出窗口
    board_input = Board(402, 150, screen, 'test', ai_settings.board_color, ai_settings.text_color, 0, 499)
    board_output = Board(402, 150, screen, 'test', ai_settings.board_color, ai_settings.text_color, 0, 650)
    boards.append(board_input)
    boards.append(board_output)

    #  创建路由表表格窗口
    i = 0
    name = 'Alice'
    for x in [403, 670, 937]:
        for y in [498, 549, 600, 651, 702, 753]:
            if x == 403:
                if y == 498:
                    i = 0
                    name = 'Alice'
                elif y == 549:
                    i = 0
                    name = 'Bob'
                elif y == 600:
                    i = 3
                    name = 'Alice'
                elif y == 651:
                    i = 3
                    name = 'Bob'
                elif y == 702:
                    i = 6
                    name = 'Alice'
                elif y == 753:
                    i = 6
                    name = 'Bob'
            elif x == 670:
                if y == 498:
                    i = 1
                    name = 'Alice'
                elif y == 549:
                    i = 1
                    name = 'Bob'
                elif y == 600:
                    i = 4
                    name = 'Alice'
                elif y == 651:
                    i = 4
                    name = 'Bob'
                elif y == 702:
                    i = 7
                    name = 'Alice'
                elif y == 753:
                    i = 7
                    name = 'Bob'
            elif x == 937:
                if y == 498:
                    i = 2
                    name = 'Alice'
                elif y == 549:
                    i = 2
                    name = 'Bob'
                elif y == 600:
                    i = 5
                    name = 'Alice'
                elif y == 651:
                    i = 5
                    name = 'Bob'
                elif y == 702:
                    i = 8
                    name = 'Alice'
                elif y == 753:
                    i = 8
                    name = 'Bob'
            msg = name + '   ' + str(router_list[i].form[name][0]) + '   ' + router_list[i].form[name][1]
            board = Board(266, 50, screen, msg, ai_settings.board_color, ai_settings.text_color, x, y)
            boards.append(board)

    return boards


def set_con():
    router_list[0].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[1].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[2].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[3].con = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[4].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[5].con = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[6].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[7].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    router_list[8].con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    router_list[3].form['Alice'] = [1, 'Alice']
    router_list[5].form['Bob'] = [1, 'Bob']
    return


def draw_con(screen):
    pygame.draw.line(screen, (128, 0, 128), (90, 210), (300, 210), 3)  # Alice-D
    pygame.draw.line(screen, (128, 0, 128), (910, 210), (1100, 210), 3)  # F-Bob
    if router_list[0].con[3] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 60), (580, 60), 3)  # A-B
    if router_list[0].con[4] == 1:
        pygame.draw.line(screen, (128, 0, 128), (325, 40), (400, 20), 3)
        pygame.draw.line(screen, (128, 0, 128), (400, 20), (810, 20), 3)
        pygame.draw.line(screen, (128, 0, 128), (810, 20), (885, 40), 3)  # A-C
    if router_list[0].con[5] == 1:
        pygame.draw.line(screen, (128, 0, 128), (325, 80), (325, 190), 3)  # A-D
    if router_list[0].con[6] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 80), (580, 190), 3)  # A-E
    if router_list[0].con[7] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 80), (860, 190), 3)  # A-F
    if router_list[0].con[8] == 1:
        pygame.draw.line(screen, (128, 0, 128), (300, 60), (280, 135), 3)
        pygame.draw.line(screen, (128, 0, 128), (280, 135), (280, 285), 3)
        pygame.draw.line(screen, (128, 0, 128), (280, 285), (300, 360), 3)  # A-G
    if router_list[0].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 80), (580, 340), 3)  # A-H
    if router_list[0].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 80), (400, 85), 3)
        pygame.draw.line(screen, (128, 0, 128), (400, 85), (855, 310), 3)
        pygame.draw.line(screen, (128, 0, 128), (855, 310), (860, 340), 3)  # A-I
    if router_list[1].con[4] == 1:
        pygame.draw.line(screen, (128, 0, 128), (630, 60), (860, 60), 3)  # B-C
    if router_list[1].con[5] == 1:
        pygame.draw.line(screen, (128, 0, 128), (580, 80), (350, 190), 3)  # B-D
    if router_list[1].con[6] == 1:
        pygame.draw.line(screen, (128, 0, 128), (605, 80), (605, 190), 3)  # B-E
    if router_list[1].con[7] == 1:
        pygame.draw.line(screen, (128, 0, 128), (630, 80), (860, 190), 3)  # B-F
    if router_list[1].con[8] == 1:
        pygame.draw.line(screen, (128, 0, 128), (580, 80), (350, 340), 3)  # B-G
    if router_list[1].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (605, 80), (565, 115), 3)
        pygame.draw.line(screen, (128, 0, 128), (565, 115), (565, 310), 3)
        pygame.draw.line(screen, (128, 0, 128), (565, 310), (605, 340), 3)  # B-H
    if router_list[1].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (630, 80), (860, 340), 3)  # B-I
    if router_list[2].con[5] == 1:
        pygame.draw.line(screen, (128, 0, 128), (860, 80), (350, 190), 3)  # C-D
    if router_list[2].con[6] == 1:
        pygame.draw.line(screen, (128, 0, 128), (860, 80), (630, 190), 3)  # C-E
    if router_list[2].con[7] == 1:
        pygame.draw.line(screen, (128, 0, 128), (885, 80), (885, 190), 3)  # C-F
    if router_list[2].con[8] == 1:
        pygame.draw.line(screen, (128, 0, 128), (860, 80), (800, 85), 3)
        pygame.draw.line(screen, (128, 0, 128), (800, 85), (355, 310), 3)
        pygame.draw.line(screen, (128, 0, 128), (355, 310), (350, 340), 3)  # C-G
    if router_list[2].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (860, 80), (630, 340), 3)  # C-H
    if router_list[2].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (910, 60), (930, 135), 3)
        pygame.draw.line(screen, (128, 0, 128), (930, 135), (930, 285), 3)
        pygame.draw.line(screen, (128, 0, 128), (930, 285), (910, 360), 3)  # C-I
    if router_list[3].con[6] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 210), (580, 210), 3)  # D-E
    if router_list[3].con[7] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 210), (370, 250), 3)
        pygame.draw.line(screen, (128, 0, 128), (370, 250), (840, 250), 3)
        pygame.draw.line(screen, (128, 0, 128), (840, 250), (860, 210), 3)  # D-F
    if router_list[3].con[8] == 1:
        pygame.draw.line(screen, (128, 0, 128), (325, 230), (325, 340), 3)  # D-G
    if router_list[3].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 230), (580, 340), 3)  # D-H
    if router_list[3].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 230), (860, 340), 3)  # D-I
    if router_list[4].con[7] == 1:
        pygame.draw.line(screen, (128, 0, 128), (630, 210), (860, 210), 3)  # E-F
    if router_list[4].con[8] == 1:
        pygame.draw.line(screen, (128, 0, 128), (580, 230), (350, 340), 3)  # E-G
    if router_list[4].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (605, 230), (605, 340), 3)  # E-H
    if router_list[4].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (630, 230), (860, 340), 3)  # E-I
    if router_list[5].con[8] == 1:
        pygame.draw.line(screen, (128, 0, 128), (860, 230), (350, 340), 3)  # F-G
    if router_list[5].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (860, 230), (630, 340), 3)  # F-H
    if router_list[5].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (885, 230), (885, 340), 3)  # F-I
    if router_list[6].con[9] == 1:
        pygame.draw.line(screen, (128, 0, 128), (350, 360), (580, 360), 3)  # G-H
    if router_list[6].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (325, 380), (400, 400), 3)
        pygame.draw.line(screen, (128, 0, 128), (400, 400), (810, 400), 3)
        pygame.draw.line(screen, (128, 0, 128), (810, 400), (885, 380), 3)  # G-I
    if router_list[7].con[10] == 1:
        pygame.draw.line(screen, (128, 0, 128), (630, 360), (860, 360), 3)  # H-I


def set_form(ai_settings, screen):
    form = []
    for router in router_list:
        form.append(router.form)
    j = 0
    sign = 0  # 记录路由是否有改变
    for router in router_list:
        j = j + 1
        for i in range(9):
            if router.con[i + 2] == 1:
                sign = sign + router_list[i].update_form(router.name, form[j - 1])
    create_board(ai_settings, screen)
    if sign > 0:
        set_form(ai_settings, screen)
    return


def send(pack, next):
    if next == 'A':
        router_list[0].recv(pack)
    elif next == 'B':
        router_list[1].recv(pack)
    elif next == 'C':
        router_list[2].recv(pack)
    elif next == 'D':
        router_list[3].recv(pack)
    elif next == 'E':
        router_list[4].recv(pack)
    elif next == 'F':
        router_list[5].recv(pack)
    elif next == 'G':
        router_list[6].recv(pack)
    elif next == 'H':
        router_list[7].recv(pack)
    elif next == 'I':
        router_list[8].recv(pack)
    elif next == 'Alice':
        computer_list[0].output(pack)
    elif next == 'Bob':
        computer_list[1].output(pack)
    return


def check_event(button_draw_line, button_get_table, button_clean, screen, ai_settings):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_mouse(mouse_x, mouse_y, button_draw_line, button_get_table, button_clean, screen, ai_settings)
    return


def check_mouse(mouse_x, mouse_y, button_draw_line, button_get_table, button_clean, screen, ai_settings):
    """响应鼠标事件"""
    com1_click = computer_list[0].rect.collidepoint(mouse_x, mouse_y)
    button1_clicked = button_draw_line.rect.collidepoint(mouse_x, mouse_y)
    button2_clicked = button_get_table.rect.collidepoint(mouse_x, mouse_y)
    button3_clicked = button_clean.rect.collidepoint(mouse_x, mouse_y)
    if button1_clicked:
        draw_lines(button_draw_line, screen)
    elif button2_clicked:
        set_form(ai_settings, screen)
    elif button3_clicked:
        clean_all()

    return


def clean_all():
    for router in router_list:
        router.form = {'Alice': [999, 'none'], 'Bob': [999, 'none']}
    set_con()


def draw_lines(button, screen):
    sourse = ' '
    dest = ' '
    dots = []
    while 1:
        if sourse == ' ':
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sou_x, sou_y = pygame.mouse.get_pos()
                    if router_list[0].rect.collidepoint(sou_x, sou_y):
                        sourse = 'A'
                    elif router_list[1].rect.collidepoint(sou_x, sou_y):
                        sourse = 'B'
                    elif router_list[2].rect.collidepoint(sou_x, sou_y):
                        sourse = 'C'
                    elif router_list[3].rect.collidepoint(sou_x, sou_y):
                        sourse = 'D'
                    elif router_list[4].rect.collidepoint(sou_x, sou_y):
                        sourse = 'E'
                    elif router_list[5].rect.collidepoint(sou_x, sou_y):
                        sourse = 'F'
                    elif router_list[6].rect.collidepoint(sou_x, sou_y):
                        sourse = 'G'
                    elif router_list[7].rect.collidepoint(sou_x, sou_y):
                        sourse = 'H'
                    elif router_list[8].rect.collidepoint(sou_x, sou_y):
                        sourse = 'I'
                    elif button.rect.collidepoint(sou_x, sou_y):
                        return
        elif dest == ' ':
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    des_x, des_y = pygame.mouse.get_pos()
                    if router_list[0].rect.collidepoint(des_x, des_y):
                        dest = 'A'
                    elif router_list[1].rect.collidepoint(des_x, des_y):
                        dest = 'B'
                    elif router_list[2].rect.collidepoint(des_x, des_y):
                        dest = 'C'
                    elif router_list[3].rect.collidepoint(des_x, des_y):
                        dest = 'D'
                    elif router_list[4].rect.collidepoint(des_x, des_y):
                        dest = 'E'
                    elif router_list[5].rect.collidepoint(des_x, des_y):
                        dest = 'F'
                    elif router_list[6].rect.collidepoint(des_x, des_y):
                        dest = 'G'
                    elif router_list[7].rect.collidepoint(des_x, des_y):
                        dest = 'H'
                    elif router_list[8].rect.collidepoint(des_x, des_y):
                        dest = 'I'
                    elif button.rect.collidepoint(des_x, des_y):
                        return
        else:
            dots.append(sourse)
            dots.append(dest)
            break
    make_line(dots, screen)


def make_line(dots, screen):
    if 'A' in dots:
        if 'B' in dots:
            router_list[0].con[3] = 1
            router_list[1].con[2] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 60), (580, 60), 3)  # A-B
        if 'C' in dots:
            router_list[0].con[4] = 1
            router_list[2].con[2] = 1
        if 'D' in dots:
            router_list[0].con[5] = 1
            router_list[3].con[2] = 1
            pygame.draw.line(screen, (128, 0, 128), (325, 80), (325, 190), 3)  # A-D
        if 'E' in dots:
            router_list[0].con[6] = 1
            router_list[4].con[2] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 80), (580, 190), 3)  # A-E
        if 'F' in dots:
            router_list[0].con[7] = 1
            router_list[5].con[2] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 80), (860, 190), 3)  # A-F
        if 'G' in dots:
            router_list[0].con[8] = 1
            router_list[6].con[2] = 1
        if 'H' in dots:
            router_list[0].con[9] = 1
            router_list[7].con[2] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 80), (580, 340), 3)  # A-H
        if 'I' in dots:
            router_list[0].con[10] = 1
            router_list[8].con[2] = 1
    if 'B' in dots:
        if 'C' in dots:
            router_list[1].con[4] = 1
            router_list[2].con[3] = 1
            pygame.draw.line(screen, (128, 0, 128), (630, 60), (860, 60), 3)  # B-C
        if 'D' in dots:
            router_list[1].con[5] = 1
            router_list[3].con[3] = 1
            pygame.draw.line(screen, (128, 0, 128), (580, 80), (350, 190), 3)  # B-D
        if 'E' in dots:
            router_list[1].con[6] = 1
            router_list[4].con[3] = 1
            pygame.draw.line(screen, (128, 0, 128), (605, 80), (605, 190), 3)  # B-E
        if 'F' in dots:
            router_list[1].con[7] = 1
            router_list[5].con[3] = 1
            pygame.draw.line(screen, (128, 0, 128), (630, 80), (860, 190), 3)  # B-F
        if 'G' in dots:
            router_list[1].con[8] = 1
            router_list[6].con[3] = 1
            pygame.draw.line(screen, (128, 0, 128), (580, 80), (350, 340), 3)  # B-G
        if 'H' in dots:
            router_list[1].con[9] = 1
            router_list[7].con[3] = 1
        if 'I' in dots:
            router_list[1].con[10] = 1
            router_list[8].con[3] = 1
            pygame.draw.line(screen, (128, 0, 128), (630, 80), (860, 340), 3)  # B-I
    if 'C' in dots:
        if 'D' in dots:
            router_list[2].con[5] = 1
            router_list[3].con[4] = 1
            pygame.draw.line(screen, (128, 0, 128), (860, 80), (350, 190), 3)  # C-D
        if 'E' in dots:
            router_list[2].con[6] = 1
            router_list[4].con[4] = 1
            pygame.draw.line(screen, (128, 0, 128), (860, 80), (630, 190), 3)  # C-E
        if 'F' in dots:
            router_list[2].con[7] = 1
            router_list[5].con[4] = 1
            pygame.draw.line(screen, (128, 0, 128), (885, 80), (885, 190), 3)  # C-F
        if 'G' in dots:
            router_list[2].con[8] = 1
            router_list[6].con[4] = 1
        if 'H' in dots:
            router_list[2].con[9] = 1
            router_list[7].con[4] = 1
            pygame.draw.line(screen, (128, 0, 128), (860, 80), (630, 340), 3)  # C-H
        if 'I' in dots:
            router_list[2].con[10] = 1
            router_list[8].con[4] = 1
    if 'D' in dots:
        if 'E' in dots:
            router_list[3].con[6] = 1
            router_list[4].con[5] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 210), (580, 210), 3)  # D-E
        if 'F' in dots:
            router_list[3].con[7] = 1
            router_list[5].con[5] = 1
        if 'G' in dots:
            router_list[3].con[8] = 1
            router_list[6].con[5] = 1
            pygame.draw.line(screen, (128, 0, 128), (325, 230), (325, 340), 3)  # D-G
        if 'H' in dots:
            router_list[3].con[9] = 1
            router_list[7].con[5] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 230), (580, 340), 3)  # D-H
        if 'I' in dots:
            router_list[3].con[10] = 1
            router_list[8].con[5] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 230), (860, 340), 3)  # D-I
    if 'E' in dots:
        if 'F' in dots:
            router_list[4].con[7] = 1
            router_list[5].con[6] = 1
            pygame.draw.line(screen, (128, 0, 128), (630, 210), (860, 210), 3)  # E-F
        if 'G' in dots:
            router_list[4].con[8] = 1
            router_list[6].con[6] = 1
            pygame.draw.line(screen, (128, 0, 128), (580, 230), (350, 340), 3)  # E-G
        if 'H' in dots:
            router_list[4].con[9] = 1
            router_list[7].con[6] = 1
            pygame.draw.line(screen, (128, 0, 128), (605, 230), (605, 340), 3)  # E-H
        if 'I' in dots:
            router_list[4].con[10] = 1
            router_list[8].con[6] = 1
            pygame.draw.line(screen, (128, 0, 128), (630, 230), (860, 340), 3)  # E-I
    if 'F' in dots:
        if 'G' in dots:
            router_list[5].con[8] = 1
            router_list[6].con[7] = 1
            pygame.draw.line(screen, (128, 0, 128), (860, 230), (350, 340), 3)  # F-G
        if 'H' in dots:
            router_list[5].con[9] = 1
            router_list[7].con[7] = 1
            pygame.draw.line(screen, (128, 0, 128), (860, 230), (630, 340), 3)  # F-H
        if 'I' in dots:
            router_list[5].con[10] = 1
            router_list[8].con[7] = 1
            pygame.draw.line(screen, (128, 0, 128), (885, 230), (885, 340), 3)  # F-I
    if 'G' in dots:
        if 'H' in dots:
            router_list[6].con[9] = 1
            router_list[7].con[8] = 1
            pygame.draw.line(screen, (128, 0, 128), (350, 360), (580, 360), 3)  # G-H
        if 'I' in dots:
            router_list[6].con[10] = 1
            router_list[8].con[8] = 1
    if 'H' in dots:
        if 'I' in dots:
            router_list[7].con[10] = 1
            router_list[8].con[9] = 1
            pygame.draw.line(screen, (128, 0, 128), (630, 360), (860, 360), 3)  # H-I
    return

# def ip_pack(msg):
#     """将数据封装成模拟ip数据包"""
#     head = []
#     version = 'ipv4'  # 版本
#     h_length = '20'  # 首部长度
#     DS = ''  # 区分服务
#     length = ''  # 总长度
#     identification = ''  # 标识
#     flag = ''  # 标志
#     pianyi = ''  # 片偏移
#     TTL = ''  # 生存时间
#     xieyi = ''  # 协议
#     jiaoyanhe = ''  # 首部校验和
#     source = ''
#     dest = ''
#
#     pack = []
#     return pack
