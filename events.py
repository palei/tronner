
class Event(object):
    def __init__(self, trigger, callback):
        self.trigger = trigger
        self.callback = callback

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
