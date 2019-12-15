class Stats():

    def __init__(self):
        self.input_msg = ''
        self.output_msg = ''
        self.button_draw_color = (0, 0, 0)
        self.line_color = []
        for i in range(38):
            self.line_color.append((128, 0, 128))