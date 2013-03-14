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
            self.callback.__name__, ', '.join([p.strip('<>') for p in self.params]))

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
    def __init__(self, trigger, seconds, callback, periodic=False, name=None):
        Thread.__init__(self)
        self.trigger = trigger
        self.callback = callback
        self.seconds = seconds
        self.name = name
        self.periodic = periodic
        self.setDaemon(True) # kill thread when main thread exits

    def run(self):
        self.idle = False
        while True:
            time.sleep(self.seconds)
            if self.idle:
                continue
            self.callback()
            sys.stdout.flush()
            if not self.periodic:
                break

    def stop(self):
        self.idle = True

    def restart(self):
        if self.isAlive():
            self.idle = False
            return
        self.start()

    def __repr__(self):
        return '<TimedEvent %s %d %s periodic=%s name=%s>' % (self.trigger, self.seconds, 
            self.callback.__name__, self.periodic, self.name)

class TimedEvents(Events):
    def add(self, trigger, seconds, callback, periodic=False, name=None):
        self.append(TimedEvent(trigger, seconds, callback, periodic, name))

    def get(self, trigger=None, name=None):
        if not name:
            return super(TimedEvents, self).get(trigger)
        for event in self:
            if event.name == name:
                return event
