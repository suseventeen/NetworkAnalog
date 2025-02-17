import pygame
import sys
from pygame.sprite import Group
from computer import Computer
from router import Router
from board import Board

router_list = []
computer_list = []
boards_put = []


def update_screen(ai_settings, screen, computers, routers, button1, button2, button3, boards, stats):
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
    for board in boards_put:
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
    draw_con(screen, stats)

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


def create_board(ai_settings, screen, stats):
    boards = []
    #  创建输入输出窗口
    board_input = Board(402, 150, screen, stats.input_msg, ai_settings.board_color, ai_settings.text_color, 0, 499)
    board_output = Board(402, 150, screen, stats.output_msg, ai_settings.board_color, ai_settings.text_color, 0, 650)
    boards_put.append(board_input)
    boards_put.append(board_output)

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


def draw_con(screen, stats):
    pygame.draw.line(screen, stats.line_color[0], (90, 210), (300, 210), 3)  # Alice-D
    pygame.draw.line(screen, stats.line_color[1], (910, 210), (1100, 210), 3)  # F-Bob
    if router_list[0].con[3] == 1:
        pygame.draw.line(screen, stats.line_color[2], (350, 60), (580, 60), 3)  # A-B
    if router_list[0].con[4] == 1:
        pygame.draw.line(screen, stats.line_color[3], (325, 40), (400, 20), 3)
        pygame.draw.line(screen, stats.line_color[3], (400, 20), (810, 20), 3)
        pygame.draw.line(screen, stats.line_color[3], (810, 20), (885, 40), 3)  # A-C
    if router_list[0].con[5] == 1:
        pygame.draw.line(screen, stats.line_color[4], (325, 80), (325, 190), 3)  # A-D
    if router_list[0].con[6] == 1:
        pygame.draw.line(screen, stats.line_color[5], (350, 80), (580, 190), 3)  # A-E
    if router_list[0].con[7] == 1:
        pygame.draw.line(screen, stats.line_color[6], (350, 80), (860, 190), 3)  # A-F
    if router_list[0].con[8] == 1:
        pygame.draw.line(screen, stats.line_color[7], (300, 60), (280, 135), 3)
        pygame.draw.line(screen, stats.line_color[7], (280, 135), (280, 285), 3)
        pygame.draw.line(screen, stats.line_color[7], (280, 285), (300, 360), 3)  # A-G
    if router_list[0].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[8], (350, 80), (580, 340), 3)  # A-H
    if router_list[0].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[9], (350, 80), (400, 85), 3)
        pygame.draw.line(screen, stats.line_color[9], (400, 85), (855, 310), 3)
        pygame.draw.line(screen, stats.line_color[9], (855, 310), (860, 340), 3)  # A-I
    if router_list[1].con[4] == 1:
        pygame.draw.line(screen, stats.line_color[10], (630, 60), (860, 60), 3)  # B-C
    if router_list[1].con[5] == 1:
        pygame.draw.line(screen, stats.line_color[11], (580, 80), (350, 190), 3)  # B-D
    if router_list[1].con[6] == 1:
        pygame.draw.line(screen, stats.line_color[12], (605, 80), (605, 190), 3)  # B-E
    if router_list[1].con[7] == 1:
        pygame.draw.line(screen, stats.line_color[13], (630, 80), (860, 190), 3)  # B-F
    if router_list[1].con[8] == 1:
        pygame.draw.line(screen, stats.line_color[14], (580, 80), (350, 340), 3)  # B-G
    if router_list[1].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[15], (605, 80), (565, 115), 3)
        pygame.draw.line(screen, stats.line_color[15], (565, 115), (565, 310), 3)
        pygame.draw.line(screen, stats.line_color[15], (565, 310), (605, 340), 3)  # B-H
    if router_list[1].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[16], (630, 80), (860, 340), 3)  # B-I
    if router_list[2].con[5] == 1:
        pygame.draw.line(screen, stats.line_color[17], (860, 80), (350, 190), 3)  # C-D
    if router_list[2].con[6] == 1:
        pygame.draw.line(screen, stats.line_color[18], (860, 80), (630, 190), 3)  # C-E
    if router_list[2].con[7] == 1:
        pygame.draw.line(screen, stats.line_color[19], (885, 80), (885, 190), 3)  # C-F
    if router_list[2].con[8] == 1:
        pygame.draw.line(screen, stats.line_color[20], (860, 80), (800, 85), 3)
        pygame.draw.line(screen, stats.line_color[20], (800, 85), (355, 310), 3)
        pygame.draw.line(screen, stats.line_color[20], (355, 310), (350, 340), 3)  # C-G
    if router_list[2].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[21], (860, 80), (630, 340), 3)  # C-H
    if router_list[2].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[22], (910, 60), (930, 135), 3)
        pygame.draw.line(screen, stats.line_color[22], (930, 135), (930, 285), 3)
        pygame.draw.line(screen, stats.line_color[22], (930, 285), (910, 360), 3)  # C-I
    if router_list[3].con[6] == 1:
        pygame.draw.line(screen, stats.line_color[23], (350, 210), (580, 210), 3)  # D-E
    if router_list[3].con[7] == 1:
        pygame.draw.line(screen, stats.line_color[24], (350, 210), (370, 250), 3)
        pygame.draw.line(screen, stats.line_color[24], (370, 250), (840, 250), 3)
        pygame.draw.line(screen, stats.line_color[24], (840, 250), (860, 210), 3)  # D-F
    if router_list[3].con[8] == 1:
        pygame.draw.line(screen, stats.line_color[25], (325, 230), (325, 340), 3)  # D-G
    if router_list[3].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[26], (350, 230), (580, 340), 3)  # D-H
    if router_list[3].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[27], (350, 230), (860, 340), 3)  # D-I
    if router_list[4].con[7] == 1:
        pygame.draw.line(screen, stats.line_color[28], (630, 210), (860, 210), 3)  # E-F
    if router_list[4].con[8] == 1:
        pygame.draw.line(screen, stats.line_color[29], (580, 230), (350, 340), 3)  # E-G
    if router_list[4].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[30], (605, 230), (605, 340), 3)  # E-H
    if router_list[4].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[31], (630, 230), (860, 340), 3)  # E-I
    if router_list[5].con[8] == 1:
        pygame.draw.line(screen, stats.line_color[32], (860, 230), (350, 340), 3)  # F-G
    if router_list[5].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[33], (860, 230), (630, 340), 3)  # F-H
    if router_list[5].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[34], (885, 230), (885, 340), 3)  # F-I
    if router_list[6].con[9] == 1:
        pygame.draw.line(screen, stats.line_color[35], (350, 360), (580, 360), 3)  # G-H
    if router_list[6].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[36], (325, 380), (400, 400), 3)
        pygame.draw.line(screen, stats.line_color[36], (400, 400), (810, 400), 3)
        pygame.draw.line(screen, stats.line_color[36], (810, 400), (885, 380), 3)  # G-I
    if router_list[7].con[10] == 1:
        pygame.draw.line(screen, stats.line_color[37], (630, 360), (860, 360), 3)  # H-I


def set_form(ai_settings, screen, stats):
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
    create_board(ai_settings, screen, stats)
    if sign > 0:
        set_form(ai_settings, screen, stats)
    clean_color(stats, ai_settings)
    return


def send(pack, next, stats, ai_setting):
    if next == 'A':
        router_list[0].recv(pack, stats, ai_setting)
    elif next == 'B':
        router_list[1].recv(pack, stats, ai_setting)
    elif next == 'C':
        router_list[2].recv(pack, stats, ai_setting)
    elif next == 'D':
        router_list[3].recv(pack, stats, ai_setting)
    elif next == 'E':
        router_list[4].recv(pack, stats, ai_setting)
    elif next == 'F':
        router_list[5].recv(pack, stats, ai_setting)
    elif next == 'G':
        router_list[6].recv(pack, stats, ai_setting)
    elif next == 'H':
        router_list[7].recv(pack, stats, ai_setting)
    elif next == 'I':
        router_list[8].recv(pack, stats, ai_setting)
    elif next == 'Alice':
        stats.input_msg = computer_list[0].output(pack)
    elif next == 'Bob':
        stats.output_msg = computer_list[1].output(pack)
    return


def check_event(button_draw_line, button_get_table, button_clean, screen, ai_settings, stats):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if stats.button_draw_stat == 'off':
                check_mouse(mouse_x, mouse_y, button_draw_line, button_get_table, button_clean, screen, ai_settings, stats)
            else:
                draw_lines(button_draw_line, screen, stats, ai_settings, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            com_input(event, stats, ai_settings)
    return


def check_mouse(mouse_x, mouse_y, button_draw_line, button_get_table, button_clean, screen, ai_settings, stats):
    """响应鼠标事件"""
    button1_clicked = button_draw_line.rect.collidepoint(mouse_x, mouse_y)
    button2_clicked = button_get_table.rect.collidepoint(mouse_x, mouse_y)
    button3_clicked = button_clean.rect.collidepoint(mouse_x, mouse_y)
    if button1_clicked:
        button_draw_line.button_color = ai_settings.inbutton_color
        button_draw_line.prep_msg("draw line")
        stats.button_draw_stat = 'on'
    elif button2_clicked:
        set_form(ai_settings, screen, stats)
    elif button3_clicked:
        clean_all(stats, ai_settings)

    return


def com_input(event, stats, ai_setting):
    msg = stats.input_msg
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            msg = msg + 'a'
        elif event.key == pygame.K_b:
            msg = msg + 'b'
        elif event.key == pygame.K_c:
            msg = msg + 'c'
        elif event.key == pygame.K_d:
            msg = msg + 'd'
        elif event.key == pygame.K_e:
            msg = msg + 'e'
        elif event.key == pygame.K_f:
            msg = msg + 'f'
        elif event.key == pygame.K_g:
            msg = msg + 'g'
        elif event.key == pygame.K_h:
            msg = msg + 'h'
        elif event.key == pygame.K_i:
            msg = msg + 'i'
        elif event.key == pygame.K_j:
            msg = msg + 'j'
        elif event.key == pygame.K_k:
            msg = msg + 'k'
        elif event.key == pygame.K_l:
            msg = msg + 'l'
        elif event.key == pygame.K_m:
            msg = msg + 'm'
        elif event.key == pygame.K_n:
            msg = msg + 'n'
        elif event.key == pygame.K_o:
            msg = msg + 'o'
        elif event.key == pygame.K_p:
            msg = msg + 'p'
        elif event.key == pygame.K_q:
            msg = msg + 'q'
        elif event.key == pygame.K_r:
            msg = msg + 'r'
        elif event.key == pygame.K_s:
            msg = msg + 's'
        elif event.key == pygame.K_t:
            msg = msg + 't'
        elif event.key == pygame.K_u:
            msg = msg + 'u'
        elif event.key == pygame.K_v:
            msg = msg + 'v'
        elif event.key == pygame.K_w:
            msg = msg + 'w'
        elif event.key == pygame.K_x:
            msg = msg + 'x'
        elif event.key == pygame.K_y:
            msg = msg + 'y'
        elif event.key == pygame.K_z:
            msg = msg + 'z'
        elif event.key == pygame.K_SPACE :
            msg = msg + ' '
        elif event.key == pygame.K_F1:
            computer_list[0].input(stats.input_msg, stats, ai_setting)
        elif event.key == pygame.K_1:
            msg = msg + '1'
        elif event.key == pygame.K_BACKSPACE:
            msg = msg[:-1]

        stats.input_msg = msg


def clean_all(stats, ai_setting):
    for router in router_list:
        router.form = {'Alice': [999, 'none'], 'Bob': [999, 'none']}
        stats.output_msg = ''
        stats.input_msg = ''
    clean_color(stats, ai_setting)
    set_con()


def draw_lines(button, screen, stats, ai_settings, mouse_x, mouse_y):
    if button.rect.collidepoint(mouse_x, mouse_y):
        button.button_color = ai_settings.unbutton_color
        button.prep_msg("draw line")
        stats.button_draw_stat = 'off'
    elif stats.source_dot == '':
        if router_list[0].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'A'
        elif router_list[1].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'B'
        elif router_list[2].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'C'
        elif router_list[3].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'D'
        elif router_list[4].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'E'
        elif router_list[5].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'F'
        elif router_list[6].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'G'
        elif router_list[7].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'H'
        elif router_list[8].rect.collidepoint(mouse_x, mouse_y):
            stats.source_dot = 'I'
    elif stats.dest_dot == '':
        if router_list[0].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'A':
            stats.dest_dot = 'A'
        elif router_list[1].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'B':
            stats.dest_dot = 'B'
        elif router_list[2].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'C':
            stats.dest_dot = 'C'
        elif router_list[3].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'D':
            stats.dest_dot = 'D'
        elif router_list[4].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'E':
            stats.dest_dot = 'E'
        elif router_list[5].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'F':
            stats.dest_dot = 'F'
        elif router_list[6].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'G':
            stats.dest_dot = 'G'
        elif router_list[7].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'H':
            stats.dest_dot = 'H'
        elif router_list[8].rect.collidepoint(mouse_x, mouse_y) and stats.source_dot != 'I':
            stats.dest_dot = 'I'
    if stats.source_dot != '' and stats.dest_dot != '':
        dots = []
        dots.append(stats.source_dot)
        dots.append(stats.dest_dot)
        make_line(dots)
        stats.source_dot = ''
        stats.dest_dot = ''



def make_line(dots):
    if 'A' in dots:
        if 'B' in dots:
            router_list[0].con[3] = 1
            router_list[1].con[2] = 1
        elif 'C' in dots:
            router_list[0].con[4] = 1
            router_list[2].con[2] = 1
        elif 'D' in dots:
            router_list[0].con[5] = 1
            router_list[3].con[2] = 1
        elif 'E' in dots:
            router_list[0].con[6] = 1
            router_list[4].con[2] = 1
        elif 'F' in dots:
            router_list[0].con[7] = 1
            router_list[5].con[2] = 1
        elif 'G' in dots:
            router_list[0].con[8] = 1
            router_list[6].con[2] = 1
        elif 'H' in dots:
            router_list[0].con[9] = 1
            router_list[7].con[2] = 1
        elif 'I' in dots:
            router_list[0].con[10] = 1
            router_list[8].con[2] = 1
    elif 'B' in dots:
        if 'C' in dots:
            router_list[1].con[4] = 1
            router_list[2].con[3] = 1
        elif 'D' in dots:
            router_list[1].con[5] = 1
            router_list[3].con[3] = 1
        elif 'E' in dots:
            router_list[1].con[6] = 1
            router_list[4].con[3] = 1
        elif 'F' in dots:
            router_list[1].con[7] = 1
            router_list[5].con[3] = 1
        elif 'G' in dots:
            router_list[1].con[8] = 1
            router_list[6].con[3] = 1
        elif 'H' in dots:
            router_list[1].con[9] = 1
            router_list[7].con[3] = 1
        elif 'I' in dots:
            router_list[1].con[10] = 1
            router_list[8].con[3] = 1
    elif 'C' in dots:
        if 'D' in dots:
            router_list[2].con[5] = 1
            router_list[3].con[4] = 1
        elif 'E' in dots:
            router_list[2].con[6] = 1
            router_list[4].con[4] = 1
        elif 'F' in dots:
            router_list[2].con[7] = 1
            router_list[5].con[4] = 1
        elif 'G' in dots:
            router_list[2].con[8] = 1
            router_list[6].con[4] = 1
        elif 'H' in dots:
            router_list[2].con[9] = 1
            router_list[7].con[4] = 1
        elif 'I' in dots:
            router_list[2].con[10] = 1
            router_list[8].con[4] = 1
    elif 'D' in dots:
        if 'E' in dots:
            router_list[3].con[6] = 1
            router_list[4].con[5] = 1
        elif 'F' in dots:
            router_list[3].con[7] = 1
            router_list[5].con[5] = 1
        elif 'G' in dots:
            router_list[3].con[8] = 1
            router_list[6].con[5] = 1
        elif 'H' in dots:
            router_list[3].con[9] = 1
            router_list[7].con[5] = 1
        elif 'I' in dots:
            router_list[3].con[10] = 1
            router_list[8].con[5] = 1
    elif 'E' in dots:
        if 'F' in dots:
            router_list[4].con[7] = 1
            router_list[5].con[6] = 1
        elif 'G' in dots:
            router_list[4].con[8] = 1
            router_list[6].con[6] = 1
        elif 'H' in dots:
            router_list[4].con[9] = 1
            router_list[7].con[6] = 1
        elif 'I' in dots:
            router_list[4].con[10] = 1
            router_list[8].con[6] = 1
    elif 'F' in dots:
        if 'G' in dots:
            router_list[5].con[8] = 1
            router_list[6].con[7] = 1
        elif 'H' in dots:
            router_list[5].con[9] = 1
            router_list[7].con[7] = 1
        elif 'I' in dots:
            router_list[5].con[10] = 1
            router_list[8].con[7] = 1
    elif 'G' in dots:
        if 'H' in dots:
            router_list[6].con[9] = 1
            router_list[7].con[8] = 1
        elif 'I' in dots:
            router_list[6].con[10] = 1
            router_list[8].con[8] = 1
    elif 'H' in dots:
        if 'I' in dots:
            router_list[7].con[10] = 1
            router_list[8].con[9] = 1
    return


def clean_color(stats, ai_setting):
    """重置所有路由器和路径的颜色"""
    for router in router_list:
        router.image = pygame.image.load('images/router_un.png')
    for i in range(38):
        stats.line_color[i] = ai_setting.unline_color
    return


def change_line_color(name1, name2, stats, ai_setting):
    stats.line_color[0] = [60, 179, 113]
    stats.line_color[1] = [60, 179, 113]
    name = [name1, name2]
    if 'A' in name :
        if 'B' in name:
            stats.line_color[2] = [60, 179, 113]
        elif 'C' in name:
            stats.line_color[3] = [60, 179, 113]
        elif 'D' in name:
            stats.line_color[4] = [60, 179, 113]
        elif 'E' in name:
            stats.line_color[5] = [60, 179, 113]
        elif 'F' in name:
            stats.line_color[6] = [60, 179, 113]
        elif 'G' in name:
            stats.line_color[7] = [60, 179, 113]
        elif 'H' in name:
            stats.line_color[8] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[9] = [60, 179, 113]
    elif 'B' in name :
        if 'C' in name:
            stats.line_color[10] = [60, 179, 113]
        elif 'D' in name:
            stats.line_color[11] = [60, 179, 113]
        elif 'E' in name:
            stats.line_color[12] = [60, 179, 113]
        elif 'F' in name:
            stats.line_color[13] = [60, 179, 113]
        elif 'G' in name:
            stats.line_color[14] = [60, 179, 113]
        elif 'H' in name:
            stats.line_color[15] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[16] = [60, 179, 113]
    elif 'C' in name :
        if 'D' in name:
            stats.line_color[17] = [60, 179, 113]
        elif 'E' in name:
            stats.line_color[18] = [60, 179, 113]
        elif 'F' in name:
            stats.line_color[19] = [60, 179, 113]
        elif 'G' in name:
            stats.line_color[20] = [60, 179, 113]
        elif 'H' in name:
            stats.line_color[21] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[22] = [60, 179, 113]
    elif 'D' in name :
        if 'E' in name:
            stats.line_color[23] = [60, 179, 113]
        elif 'F' in name:
            stats.line_color[24] = [60, 179, 113]
        elif 'G' in name:
            stats.line_color[25] = [60, 179, 113]
        elif 'H' in name:
            stats.line_color[26] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[27] = [60, 179, 113]
    elif 'E' in name :
        if 'F' in name:
            stats.line_color[28] = [60, 179, 113]
        elif 'G' in name:
            stats.line_color[29] = [60, 179, 113]
        elif 'H' in name:
            stats.line_color[30] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[31] = [60, 179, 113]
    elif 'F' in name :
        if 'G' in name:
            stats.line_color[32] = [60, 179, 113]
        elif 'H' in name:
            stats.line_color[33] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[34] = [60, 179, 113]
    elif 'G' in name :
        if 'H' in name:
            stats.line_color[35] = [60, 179, 113]
        elif 'I' in name:
            stats.line_color[36] = [60, 179, 113]
    elif 'H' in name :
        if 'I' in name:
            stats.line_color[37] = [60, 179, 113]

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
