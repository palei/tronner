
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

class TimedEvent(Event):
    def __init__(self, trigger, callback, time, periodic=False):
        super(TimedEvent, self).__init__(trigger, callback)
        self.time = time
        self.periodic = periodic

