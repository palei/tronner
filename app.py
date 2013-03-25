import sys
from datetime import datetime
from .events import Events, TimedEvents
from . import command

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

                self._line = s.strip().split()
                trigger, args = self._line[0], self._line[1:]

                events = self.events.get(trigger)
                
                if events:
                    for event in events:
                        params = self.parse_callback_params(event, args)
                        event.callback(**params)

                timed_events = self.timed_events.get(trigger)
                
                if timed_events:
                    for t in timed_events:
                        t.restart()

                if debug:
                    self.print_debug_info()

                sys.stdout.flush()
            self.before_exit()
        except KeyboardInterrupt:
            self.before_exit()

        except TypeError as e:
            command.comment("TypeError: %s " % e)

    def parse_callback_params(self, event, args):
        params = dict()
        i = 0
        for param, value in zip(event.params, args):

            param = param.strip('<>')
            parts = param.split(':')

            if len(parts) > 1:
                eval(parts[0])

            if param.endswith('...'):
                params[param.strip('...')] = ' '.join(args[i:])
                break

            # TODO this shit

            #if ':' in param:
            #    parts = param.split(':', 2)
            #    fn, param = parts[0], param[1]
            #    eval(fn)(param)

            if param.startswith('int'):
                param = param.split(':')[1]
                value = parse_int(value)
            
            params[param] = value

            i += 1
        return params

    def get_line(self):
        return self._line

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


def parse_int(string):
    """Returns 0 if string can't be converted to int."""
    try:
        return int(string)
    except ValueError:
        return 0
