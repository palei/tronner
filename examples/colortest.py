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
    colors.append(colorize("Pink", PINK))
    colors.append(colorize("Gray", GRAY))
    colors.append(colorize("Lime", LIME))

    command.say(', '.join(colors))
    command.say(gradient("This goes from cyan to green.", CYAN, GREEN))
    command.say(gradient("This from white to blue.", WHITE, BLUE))
    command.say(gradient("And this to red from yellow.", YELLOW, RED))

    command.say(random_color_text("This should be color quite randomly."))

if __name__ == '__main__':
    app.run()
