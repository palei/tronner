import sys
from events import Events

class App(object):
    L = None

    def __init__(self):
        self.events = Events()

    def run(self):
        for key, value in self.events:
            Command.command("LADDER_LOG_WRITE_%s" % key)
        while True:
            s = sys.stdin.readline()
            if not s:
                break
            self.L = s.strip().split()
            fn = self.events.get(self.L[0])
            if fn:
                fn()
                sys.stdin.flush()

    def event(self, e):
        def decorator(callback):
            self.events.add(e, callback)
            return callback
        return decorator

