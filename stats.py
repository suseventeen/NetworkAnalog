class Stats():

    def __init__(self, ai_settings):
        self.input_msg = ''
        self.output_msg = ''

        self.button_draw_color = ai_settings.unbutton_color

        self.button_draw_stat = 'off'  # draw按键的状态
        self.source_dot = ''
        self.dest_dot = ''

        self.line_color = []
        for i in range(38):
            self.line_color.append(ai_settings.unline_color)