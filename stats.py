
class Stats(object):
    def __getattr__(self, attribute):
        setattr(self, attribute, 0)
        return getattr(self, attribute)
