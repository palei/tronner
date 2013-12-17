Tronner
=======

Tronner is a python powered event handling and scripting framework for [Armagetron Advanced](http://armagetronad.net). 

This is still work in progress and many things are subject to change.

## Getting started

The most basic application structure looks like this.

```python
#!/usr/bin/env python
from tronner import App
app = App()

@app.event('PLAYER_ENTERED')
def player_entered():
    print "Greetings, program."

app.run()
```

### Events with parameters

Variables from ladder log can be passed as keyword arguments to the callback function.

```python
@app.event('DEATH_FRAG <killed> <killer>')
def death_frag(killed, killer):
    print "%s killed %s for 1 point." % (killer, killed)
```

To store the entire rest of the line in one variable you can add `...` to the end of it.

```python
@app.event('CHAT <name> <text...>')
def chat_handler(name, text):
    print "%s said: %s" % (name, text)
```

If you're expecting the variable to be something other than string, you can use the following syntax.

```python
@app.event('ROUND_SCORE <int:score> <name>')
def round_score(name, score):
    total_score += score
```

The part before the colon will be evaluated as python and should map to an actual function.

### Timed events

Timed events are triggered a number of seconds after a ladder log event occurs. The following function is called 5 minutes after a round starts.

```python
@app.timed_event('NEW_ROUND', 300)
def sudden_death():
    print 'CYCLE_RUBBER 0.1'
    print 'CYCLE_BRAKE -100'
```

If you want the function to be triggered periodically, you can set the last parameter to `True`.

```python
@app.timed_event('NEW_ROUND', 30, periodic=True)
def spawn_random_deathzone():
    pass
```

The timer for periodic events is reset after every new occurance of the specified event.

Timed events accept an additional `name` argument, which can be useful if you ever need to stop or restart the it. 

```python
some_timed_event = app.timed_events.get(name="something")
some_timed_event.stop()
some_timed_event.restart()
```

### Command functions

The command module contains helper function for easier interaction with the server.

```python
from tronner import command

@app.event('PLAYER_LEFT <name>')
def goodbye(name):
    command.say("%s has left the server." % name)
```

For a full list of available command functions, take a look at the command module in the source files.

The commands are written to standard output by default. Depending on how you run your server, this may not be suitable for you. For example, if you're not using `SPAWN_SCRIPT` or piping the output of your script to the server directly, you may need to override the main command function.

```python
from tronner import command
def custom_command(s):
    """Untested example. Appends s to end of input.txt"""
    with fopen('input.txt', 'a') as fh:
        fh.write(s) 

command.command = custom_command
```

### Tracking players

Tronner comes with some helper classes that let you keep track of stuff that happens on the grid.

```python
from tronner import Players
players = Players()

@app.event('PLAYER_ENTERED <name> <gid> <ip>')
def player_entered(name, gid, ip):
    players.add(name, gid, ip)

@app.event('PLAYER_LEFT <name>')
def player_left(name):
    players.safe_remove(name)

@app.event('PLAYER_RENAMED <old_name> <new_name> <ip> <screen_name>)
def player_renamed(old_name, new_name, ip, screen_name):
    player = players.get(old_name)
    if player:
        player.name = new_name
        player.screen_name = screen_name
```

The player objects have a built in `stats` attribute which is an instance of `Stats` class. You can use it to store some statistics.

```python
@app.event('DEATH_FRAG <killed> <killer>')
def death_frag(killed, killer):
    players.get(killed).stats.deaths += 1
    players.get(killer).stats.kills += 1
```

The attributes in `Stats` are automatically initiated to `0` if they do not yet exist.

## Color module

Probably the most useless thing in this package lets you add some color to your messages.

```python
from tronner.color import YELLOW, RED, BLUE, LIME, colorize, gradient, Color
orange = Color(0xff, 0x66, 0)
colorize("Hello!", BLUE)
gradient("This is some text", LIME, BLUE)
```

### More examples

More example applications can be found in the `examples` directory. To try them out, can import the `app` object in your script and run it.

```python
from tronner.examples import greeter
greeter.app.run()
```

# Planned features

- SQLite bindings for saving statistics

# Available Ladder Log Events

```
AUTHORITY_BLURB <blurb> <player> <text>
BASEZONE_CONQUERED <team> <cx> <cy>
BASEZONE_CONQUERER <player>
CHAT <chatter> [/me] <chat string>
COMMAND <command> <player> <text>
DEATH_FRAG <prey> <predator>
DEATH_SUICIDE <player>
DEATH_TEAMKILL <prey> <predator>
ENCODING <charset>
GAME_END <date and time>
GAME_TIME <time>
MATCH_WINNER <team> <players>
NEW_MATCH <date and time>
NEW_ROUND <date and time>
NUM_HUMANS <number of humans>
ONLINE_PLAYER <name> [<ping> [<team>]]
PLAYER_ENTERED <name> <IP> <screen name>
PLAYER_LEFT <name> <IP>
PLAYER_RENAMED <old name> <new name> <ip> <screen name>
POSITIONS <team> <player1 player2 ...>
ROUND_SCORE <score difference> <player> [<team>]
ROUND_SCORE_TEAM <score difference> <team>
ROUND_WINNER <team> <players>
SACRIFICE <hole user> <hole maker> <wall owner>
TEAM_CREATED <team name>
TEAM_DESTROYED <team name>
TEAM_PLAYER_ADDED <team name> <player>
TEAM_PLAYER_REMOVED <team name> <player>
TEAM_RENAMED <old team name> <new team name>
```

## Installation

Clone the repository to a directory on your server.

```bash
$ git clone git@bitbucket.org:noob13/tronner.git
```
Create a symlink to tronner in your `data/scripts` directory.

```bash
$ ln -s /path/to/tronner/ tronner
```

Also make sure your version of python is at least 2.6!
