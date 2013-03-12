
def colorize(text, color):
    return "%s%s%s" % (color, text, RESET)

class Color(object):
    def __init__(self, r=0xff, g=0xff, b=0xff):
        self.r, self.g, self.b = abs(r), abs(g), abs(b)

    def __add__(self, color):
        r = (self.r + color.r) % 0x100
        g = (self.g + color.g) % 0x100
        b = (self.b + color.b) % 0x100
        return Color(r, g, b)

    def __sub__(self, color):
        r = self.r - color.r
        g = self.g - color.g
        b = self.b - color.b
        return Color(abs(r), abs(g), abs(b))

    def __repr__(self):
        return '0x%02x%02x%02x' % (self.r, self.g, self.b)

WHITE   = Color(255, 255, 255)
YELLOW  = Color(255, 255, 0)
RED     = Color(255, 0, 0)
GREEN   = Color(0, 255, 0)
BLUE    = Color(0, 0 , 255)
CYAN    = Color(0, 255, 255) 
BLACK   = Color(0, 0, 0)
RESET   = Color(255, 255, 0x7c)

def gradient(text, start_color, end_color):
    text_length = len(text)
    offset_r = (start_color.r - end_color.r) / text_length
    offset_g = (start_color.g - end_color.g) / text_length
    offset_b = (start_color.b - end_color.b) / text_length
    colored_text = "%s%s" % (start_color, text[0])
    current_color = start_color
    for letter in text[1:-1]:
        current_color -= Color(offset_r, offset_g, offset_b)
        colored_text += "%s%s" % (current_color, letter)
    colored_text += "%s%s" % (end_color, text[-1])
    return "%s%s" % (colored_text, RESET)


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 0xff, 0)
    yellow = red + green

    print yellow

