
class Player(object):
    def __init__(self, name, gid, ip):
        self.name = name
        self.gid = gid # normalized name before authentication
        self.ip = ip

    def __repr__(self):
        return '<Player %s %s %s>' % (self.name, self.gid, self.ip)

class Players(list):

    def add(self, name, gid, ip):
        p = Player(name, gid, ip)
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
    player = Player('noob13', 'noob13@forums', '127.0.0.1')
    print player
