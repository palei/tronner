import sys
from events import Events
from command import Command

class App(object):
    L = None

    def __init__(self):
        self.events = Events()

    def run(self):
        for event in self.events:
            Command.command("LADDER_LOG_WRITE_%s 1" % event.trigger)
        
        while True:
            s = sys.stdin.readline()
            if not s:
                pass
            self.L = s.strip().split()
            events = self.events.get(self.L[0])
            if events:
                for event in events:
                    event.callback()
            sys.stdout.flush()


    def event(self, e):
        def decorator(callback):
            self.events.add(e, callback)
            return callback
        return decorator

