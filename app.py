import sys, command
from events import Events, TimedEvents

class App(object):
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
                self.line = s.strip().split()
                events = self.events.get(self.line[0])
                if events:
                    for event in events:
                        param_count = len(event.params)
                        if param_count > 0:
                            params = self.line[1:1+param_count]
                            event.callback(*params)
                        else:
                            event.callback()

                timed_events = self.timed_events.get(self.line[0])
                if timed_events:
                    for t in timed_events:
                        t.restart()

                sys.stdout.flush()
        except KeyboardInterrupt:
            self.before_exit()

    def stop(self):
        self.running = False

    def event(self, e):
        def decorator(callback, *args, **kwargs):
            args = [s.strip('<>') for s in e.split()]
            self.events.add(args[0], callback, args[1:])
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

