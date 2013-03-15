#!/usr/bin/env python
from tronner import App
from tronner import command

app = App()

command.command('INTERCEPT_COMMANDS /stats')

@app.event('COMMAND <cmd> <name> <args>')
def command(cmd, name, args):
    if cmd == '/stats':
        command.say("%s used command: %s %s" % (name, cmd, args))


if __name__ == '__main__':
    app.run(debug=True)
