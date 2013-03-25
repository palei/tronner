#!/usr/bin/env python
from tronner import App, command, color
from tronner import Players, Player

app = App()
app.players = Players()

@app.event('PLAYER_ENTERED <name> <ip> <screen_name>')
def player_entered(name, ip, screen_name):
    p = Player(name, ip, screen_name)
    app.players.append(p)

@app.event('PLAYER_RENAMED <old_name> <new_name> <ip> <screen_name>')
def player_renamed(old_name, new_name, ip, screen_name):
    p = app.players.get(old_name)
    if p:
        p.name = new_name
        p.screen_name = screen_name

@app.event('PLAYER_LEFT <name> <ip>')
def player_left(name, ip):
    app.players.safe_remove(name)

@app.event('DEATH_FRAG <killed> <killer>')
def death_frag(killed, killer):
    app.players.get(killed).stats.deaths += 1
    app.players.get(killer).stats.kills += 1

@app.event('DEATH_SUICIDE <name>')
def death_suicide(name):
    app.players.get(name).stats.suicides += 1

@app.event('NEW_ROUND')
def new_round():
    for player in app.players:
        command.pm(player.name, player.stats)

if __name__ == '__main__':
    app.run(debug=True)

