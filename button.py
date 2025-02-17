import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg, x, y):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 90,40
        self.button_color = ai_settings.unbutton_color
        self.text_color = ai_settings.button_text_color
        self.font = pygame.font.SysFont(None, 30)

        # 创建按钮的rect对象
        self.rect = pygame.Rect(x, y, self.width, self.height)

        # 按钮的标签只需创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg渲染为图像，并使其在按钮上居中"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """绘制一个用颜色填充的按钮，再绘制文本"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)