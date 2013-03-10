from threading import Thread
import time
import sys

class Event(object):
    def __init__(self, trigger, callback):
        self.trigger = trigger
        self.callback = callback

    def __repr__(self):
        return '<Event %r>' % self.trigger

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

    def add(self, trigger, callback):
        self.append(Event(trigger, callback))

class TimedEvent(Thread):
    def __init__(self, trigger, callback, time, periodic=False):
        Thread.__init__(self)
        self.trigger = trigger
        self.callback = callback
        self.time = time
        self.periodic = periodic
        self.setDaemon(True)

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
