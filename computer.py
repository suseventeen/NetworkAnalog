import pygame
from pygame.sprite import Sprite



class Computer(Sprite):
    """表示单个主机的类"""

    def __init__(self, ai_settings, screen, x, y, name='name_unknown'):
        """初始化属性"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.name = name  # 定义主机名

        self.image = pygame.image.load('images/computer_blue.png')  # 定义主机图像
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)

    def package(self, data, des):
        """模拟数据包的封装，只添加源地址和目的地址"""
        pack = {}
        pack['data'] = data
        pack['source'] = self.name
        pack['des'] = des
        return pack


    def input(self, msg, stats):
        import function as f
        data = msg
        if self.name == 'Alice':
            pack = self.package(data, 'Bob')
            f.send(pack, 'D', stats)
        elif self.name == 'Bob':
            pack = self.package(data, 'Alice')
            f.send(pack, 'F', stats)


    def output(self, pack):
        data = pack['data']
        return data

    def blitme(self):
        self.screen.blit(self.image, self.rect)

