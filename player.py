
class Player(object):
    def __init__(self, name, ip=None, screen_name=None):
        self.name = name # becomes GID once authenticated
        self.ip = ip
        self.screen_name = screen_name

    def __repr__(self):
        return '<Player %s %s %s>' % (self.name, self.ip, self.screen_name)

class Players(list):

    def add(self, name, ip=None, screen_name=None):
        p = Player(name, ip, screen_name)
        self.append(p)

    def safe_remove(self, name):
        """Unlike inherited remove function this removes by name and 
        doesn't crash the program if the player doesn't exist"""
        for player in self:
            if player.name == name:
                try:
                    self.remove(player)
                except ValueError:
                    pass # player doesn't exist

    def get(self, name):
        for player in self:
            if player.name == name:
                return player

if __name__ == '__main__':
    player = Player('albert', '127.0.0.1', 'Albert')
    print player
