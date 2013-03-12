Tronner
=======

Tronner is a python powered event handling and scripting framework for [Armagetron Advanced](http://armagetronad.net). It makes writing external scripts easy and fun!


# Examples
## A minimal application
    :::python
    #!/usr/bin/env python
    from tronner import App
    app = App()

    @app.event('PLAYER_ENTERED')
    def player_entered():
        print "Greetings, program."

    app.run()

The function can be called anything and does not have to be named after the actual event. For every ladderlog event, multiple event handlers can be defined.

## An event with parameters

The event variables can be split into tokens and sent to the handler function.

    :::python
    @app.event('DEATH_FRAG <killed> <killer>')
    def death_frag(killed, killer):
        print "%s killed %s for 1 point." % (killer, killed)

If the number of variables doesn't match the expected number of parameters, the last parameter will always contain the rest of the string.

    :::python
    @app.event('CHAT <name> <text>')
    def handle_chat(name, text):
        pass

## Timed events
The event timer is started after a ladderlog event occurs, and the function is called some seconds later.

    :::python
    # start sudden death after 5 minutes
    @app.timed_event('NEW_ROUND', 300)
    def sudden_death():
        print 'CYCLE_RUBBER 0.1'
        print 'CYCLE_BRAKE -100'

To make periodical events a third parameter can be used.

    :::python
    @app.timed_event('NEW_ROUND', 30, periodic=True)
    def spawn_random_deathzone():
        pass

The timer for periodic events is reset after every new occurance of the specified ladderlog event.

An optional keyword argument `name` can be given to timed events. This can be useful if you want to stop and restart the event at some point.
    
    :::python
    some_timed_event = app.timed_events.get(name="something")
    some_timed_event.stop()
    some_timed_event.restart()

## Command functions
The command module contains helper function for easier interaction with the server.

    :::python
    from tronner import command

    @app.event('PLAYER_LEFT <name>')
    def goodbye(name):
        command.say("%s has left the server." % name)

The currently available commands are

    :::python
    command.say(text)                    # SAY <text>
    command.kick(player, reason)         # KICK <player> <reason>
    command.ban(player, time, reason)    # BAN <player> <time> <reason>
    command.center_message(text)         # CENTER_MESSAGE <text>
    command.silence(player)              # SILENCE <player>
    command.voice(player)                # VOICE <player>
    command.suspend(player, rounds)      # SUSPEND <player>
    command.include(config)              # INCLUDE <config>

The commands in the command-module write to standard output by default. If you're not using `SPAWN_SCRIPT`, or piping your script output to the server manually, you may need a different way of interacting with the server.

The following example demonstrates how one can override the function.
    
    :::python
    from tronner import command

    def custom_command(s):
        with fopen('input.txt', 'a') as fh:
            fh.write(s) 

    command.command = custom_command

## Tracking players

Tronner comes with some helper classes that help you keep track of the players on the grid.

    :::python
    from tronner import Players
    players = Players()

    @app.event('PLAYER_ENTERED <name> <gid> <ip>')
    def player_entered(name, gid, ip):
        players.add(name, gid, ip)

    @app.event('PLAYER_LEFT <name>')
    def player_left(name):
        players.safe_remove(name)

    @app.event('PLAYER_RENAMED <old_name> <new_name>)
    def player_renamed(old_name, new_name):
        players.get(old_name).name = new_name

The player objects have a built in `stats` attribute which is an instance of `Stats` class. You can use it to store some statistics.

    :::python
    @app.event('DEATH_FRAG <killed> <killer>')
    def death_frag(killed, killer):
        players.get(killed).stats.deaths += 1
        players.get(killer).stats.kills += 1

The attributes in `Stats` are automatically initiated to `0` if they do not yet exist.

## More examples
More example applications can be found in the `examples` module. To try them out you can simply import the `app` object in your script and run it.

    :::python
    from tronner.examples import greeter
    greeter.app.run()

# Installation
Clone the repository to a directory on your server.

    :::bash
    $ git clone git@bitbucket.org:noob13/tronner.git

Create a symlink to tronner in your `data/scripts` directory.

    :::bash
    $ ln -s /path/to/tronner/ tronner

Or, alternatively, add the directory containing tronner to your `PYTHONPATH` by adding a line like this to your `.bashrc`.

    :::bash
    $ export PYTHONPATH=$PYTHONPATH:/path/under/tronner/

# Requirements

- [Python](http://python.org) 2.6+

