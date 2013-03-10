import sys, command
from events import Events

class App(object):
    L = None

    def __init__(self):
        self.events = Events()

    def run(self):
        for event in self.events:
            command.command("LADDERLOG_WRITE_%s 1" % event.trigger)
        
        try:
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
        except KeyboardInterrupt:
            self.before_quit()

    def event(self, e, **options):
        def decorator(callback, **options):
            self.events.add(e, callback)
            return callback
        return decorator

    def before_quit():
        pass

