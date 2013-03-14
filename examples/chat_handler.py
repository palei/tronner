#!/usr/bin/env python
from tronner import App

app = App()

@app.event('CHAT <name> <text+>')
def chat_handler(name, text):
    print "%s said: %s" % (name, text)

if __name__ == '__main__':
    app.run()
