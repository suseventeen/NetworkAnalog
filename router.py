import pygame
from pygame.sprite import Sprite


class Router(Sprite):
    """表示单个路由器的类"""

    def __init__(self, ai_settings, screen, x, y, name='name_unknown'):
        """初始化属性"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.name = name  # 定义路由器的名称
        self.form = {'Alice': [999, 'none'], 'Bob': [999, 'none']}  # 路由表
        self.con = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Alice,Bob,A,B,C,D,E,F,G,H,I
        self.image = pygame.image.load('images/router_blue.png')
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)

    def recv(self, pack):
        import function as f
        des = pack['des']  # 从包中提取目的地址
        next = self.form[des][1]  # 从路由表中查找下一跳地址
        f.send(pack, next)  # 转发给下一跳


    def update_form(self, source, form):
        sign = 0
        if (form['Alice'][0] + 1) < self.form['Alice'][0]:
            self.form['Alice'] = [form['Alice'][0] + 1, source]
            sign = 1
        if (form['Bob'][0] + 1) < self.form['Bob'][0]:
            self.form['Bob'] = [form['Bob'][0] + 1, source]
            sign = 1
        return sign

    def blitme(self):
        self.screen.blit(self.image, self.rect)
