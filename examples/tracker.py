from tronner import App, Players, Player

app = App()
app.players = Players()

@app.event('PLAYER_ENTERED <name> <ip> <screen_name>')
def player_entered(name, ip, screen_name):
    p = Player(name, ip, screen_name)
    app.players.append(p)

@app.event('PLAYER_RENAMED <old_name> <new_name>')
def player_renamed(old_name, new_name):
    p = app.players.get(old_name)
    if p: p.name = new_name

@app.event('PLAYER_LEFT <name>')
def player_left(name):
    app.players.safe_remove(name)

if __name__ == '__main__':
    app.run()
