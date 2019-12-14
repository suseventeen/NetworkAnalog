import pygame

class Board():

    def __init__(self, width, height, screen, msg, back_color, text_color, x, y):
        self.screen = screen
        self.width, self.height = width, height
        self.color = back_color
        self.text_color = text_color
        self.font = pygame.font.SysFont(None,24)
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_board(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)