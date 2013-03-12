#!/usr/bin/env python
from tronner import App, command
from tronner.color import *

app = App()

@app.event("NEW_ROUND")
def new_round():
    colors = []
    colors.append(colorize("Blue", BLUE))
    colors.append(colorize("Red", RED))
    colors.append(colorize("Green", GREEN))
    colors.append(colorize("Yellow", YELLOW))
    colors.append(colorize("Cyan", CYAN))
    colors.append(colorize("White", WHITE))
    colors.append(colorize("Reset", RESET))

    command.say(', '.join(colors))
    command.say(gradient("This text goes from cyan to green.", CYAN, GREEN))

if __name__ == '__main__':
    app.run()
