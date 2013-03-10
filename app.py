import sys, command
from events import Events, TimedEvents

class App(object):
    L = None

    def __init__(self):
        self.events = Events()
        self.timed_events = TimedEvents()

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

                timed_events = self.timed_events.get(self.L[0])
                if timed_events:
                    for t in timed_events:
                        t.restart()

                sys.stdout.flush()
        except KeyboardInterrupt:
            self.before_exit()

    def stop(self):
        self.running = False

    def event(self, e, **options):
        def decorator(callback, **options):
            self.events.add(e, callback)
            return callback
        return decorator

    def timed_event(self, e, time, periodic=False):
        def decorator(callback):
            self.timed_events.add(e, callback, time, periodic)
            return callback
        return decorator

    def before_exit(self):
        pass

    def register_default_events(self, players):
        pass # TODO

