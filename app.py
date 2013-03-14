import sys, command
from events import Events, TimedEvents
from datetime import datetime

class App(object):
    def __init__(self):
        self.events = Events()
        self.timed_events = TimedEvents()

    def run(self, debug=False):
        for event in self.events + self.timed_events:
            command.command("LADDERLOG_WRITE_%s 1" % event.trigger)
        
        self.running = True
        try:
            while self.running:
                s = sys.stdin.readline()
                if not s:
                    break

                self.line = s.strip().split()
                events = self.events.get(self.line[0])
                
                if events:
                    for event in events:
                        params = self.parse_callback_params(event, self.line)
                        event.callback(**params)

                timed_events = self.timed_events.get(self.line[0])
                
                if timed_events:
                    for t in timed_events:
                        t.restart()

                if debug:
                    self.print_debug_info()

                sys.stdout.flush()
            self.before_exit()
        except KeyboardInterrupt:
            self.before_exit()

    def parse_callback_params(self, event, line):
        params = dict()
        for param, value in zip(event.params, line[1:]):
            param = a.strip('<>')
            params[param] = value
        return params


    def print_debug_info(self):
        """Prints the attributes of this object to the console"""
        command.command("# %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        for key, value in self.__dict__.items():
            command.comment("%s: %s" % (key, value))

    def stop(self):
        self.running = False

    def event(self, e):
        """Decorator for adding LadderLog events to the App."""
        def decorator(callback, *args, **kwargs):
            args = e.split()
            trigger, params = args[0], args[1:]
            self.events.add(trigger, callback, params)
            return callback
        return decorator

    def timed_event(self, e, seconds, periodic=False, name=None):
        """Decorator for adding timed events to the App."""
        def decorator(callback):
            self.timed_events.add(e, seconds, callback, periodic, name)
            return callback
        return decorator

    def before_exit(self):
        pass
