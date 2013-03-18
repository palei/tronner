
class Stats(object):
    def __getattr__(self, attribute):
        """This initiates the accessed attribute to zero if
        it doesn't yet exist."""
        setattr(self, attribute, 0)
        return getattr(self, attribute)

    def __repr__(self):
        stats = []
        for key, value in self.__dict__.items():
            stats.append("%s: %s" % (key.capitalize(), value))
        return '\n'.join(stats)

