from random import randint as rint

class Color(object):
    def __init__(self, r=0xff, g=0xff, b=0xff):
        self.r, self.g, self.b = r, g, b

    def __add__(self, color):
        """Adds color to this color and returns the result."""
        r = minmax(self.r + color.r)
        g = minmax(self.g + color.g)
        b = minmax(self.b + color.b)
        return Color(r, g, b)

    def __sub__(self, color):
        """Subtracts color from this color and returns the result."""
        r = minmax(self.r - color.r)
        g = minmax(self.g - color.g)
        b = minmax(self.b - color.b)
        return Color(r, g, b)

    def __div__(self, number):
        """Divides this color by a number."""
        r = self.r / number
        g = self.g / number
        b = self.b / number
        return Color(r, g, b)

    def __rdiv__(self, number):
        """Called when number is divided by color."""
        return self.__div__(number)

    def __repr__(self):
        return '0x%02x%02x%02x' % (abs(self.r), abs(self.g), abs(self.b))

BLACK     = Color(0, 0, 0)
WHITE     = Color(255, 255, 255)
YELLOW    = Color(255, 255, 0)
RED       = Color(255, 0, 0)
GREEN     = Color(0, 255, 0)
BLUE      = Color(0, 0 , 255)
CYAN      = Color(0, 255, 255) 
RESET     = Color(255, 255, 0x7c)
ORANGE    = Color(0xff, 0x66, 00)
PINK      = Color(0xff, 0x4b, 0xc2)
GRAY      = Color(0x99, 0x99, 0x99)
LIME      = Color(0xba, 0xfb, 0x8b)

def colorize(text, color):
    return "%s%s%s" % (color, text, RESET)

def minmax(value):
    """Makes sure color value stays within boundaries."""
    return min(0xff, max(0, value))

def random_color(light=True):
    low = 0xbb if light else 0
    return Color(rint(low, 0xff), rint(low, 0xff), rint(low, 0xff))

def random_color_text(text, light=True):
    result = ""
    for letter in text:
        result += str(random_color())
        result += letter
    result += str(RESET)
    return result

def gradient(text, start_color, end_color):
    """Gives text a fancy color gradient."""
    length = len(text)

    # the delta of each color
    delta_r = start_color.r - end_color.r
    delta_g = start_color.g - end_color.g
    delta_b = start_color.b - end_color.b

    # the "step" sizes for each of the colors
    step_r = delta_r / length
    step_g = delta_g / length
    step_b = delta_b / length

    print step_r, step_g, step_b

    result = ""
    current_color = start_color

    for character in text:
        result += "%s%s" % (current_color, character)
        current_color -= Color(step_r, step_g, step_b)

    return "%s%s" % (result, RESET)

if __name__ == '__main__':
    print gradient("ABCDE", BLUE, GREEN)

