import sys, command
from events import Events, TimedEvents

class App(object):
    L = None

    def __init__(self):
        self.events = Events()

    def run(self):
        for event in self.events:
            command.command("LADDERLOG_WRITE_%s 1" % event.trigger)
        
        self.running = True
        try:
            while self.running:
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
            self.before_exit()

    def stop(self):
        self.running = False

    def event(self, e, **options):
        if not hasattr(self, 'events'):
            self.events = Events()

        def decorator(callback, **options):
            self.events.add(e, callback)
            return callback
        return decorator

    def timed_event(self, e, time, periodic=False):
        if not hasattr(self, 'timed_events'):
            self.timed_events = TimedEvents()

        def decorator(callback):
            self.timed_events.add(e, callback, time, periodic)
            return callback
        return decorator

    def before_exit():
        pass

