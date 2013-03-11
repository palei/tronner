from threading import Thread
import time
import sys

class Event(object):
    def __init__(self, trigger, callback, params):
        self.trigger = trigger
        self.callback = callback
        self.params = params

    def __repr__(self):
        return '<Event %s %s(%s)>' % (self.trigger, 
            self.callback.__name__, ', '.join(self.params))

class Events(list):
    def get(self, trigger):
        """Returns a list of callbacks or None"""
        callbacks = []
        for event in self:
            if event.trigger == trigger:
                callbacks.append(event)
        if len(callbacks) > 0:
            return callbacks
        return None

    def add(self, trigger, callback, params):
        self.append(Event(trigger, callback, params))

class TimedEvent(Thread):
    def __init__(self, trigger, callback, seconds, name=None, periodic=False):
        Thread.__init__(self)
        self.trigger = trigger
        self.callback = callback
        self.seconds = seconds
        self.name = name
        self.periodic = periodic
        self.setDaemon(True) # kill thread when main thread exits

    def run(self):
        self.stopped = False
        while not self.stopped:
            time.sleep(self.time)
            self.callback()
            sys.stdout.flush()
            if not self.periodic:
                break

    def stop(self):
        self.stopped = True

    def restart(self):
        self.stop()
        self.start()

class TimedEvents(Events):
    def add(self, trigger, callback, time, periodic=False):
        self.append(TimedEvent(trigger, callback, time, periodic))
