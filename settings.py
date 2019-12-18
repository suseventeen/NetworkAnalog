class Settings():
    """存储所有设置"""

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (88, 140, 140)

        #  board设置
        self.board_color = (0, 0, 0)
        self.text_color = (255, 255, 255)

        # line设置
        self.unline_color = (107, 45, 34)  # 未经过的line颜色
        self.inline_color = (26, 250, 41)  # 数据经过的line颜色

        # button设置
        self.unbutton_color = (1, 28, 38)  # 未选中的button颜色
        self.inbutton_color = (109, 12, 34)  # 选中的button颜色
        self.button_text_color = (255, 255, 255)  # button字符颜色
