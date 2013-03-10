
Event Handling and Scripting Framework for Armagetron Advanced
==============================================================

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

## An event with parameters
    :::python
    @app.event('DEATH_FRAG <killed> <killer>')
    def death_frag(killed, killer):
        print "%s killed %s for 1 point." % (killer, killed)

## Timed events
    :::python
    @app.timed_event('NEW_ROUND', 10, periodic=True)
    def spam():
        command.center_message("You're being spammed by tronner")

The `spam` function is executed every 10 seconds after round start, and the timer resets after every occurance of trigger (`NEW ROUND` in this case).

## Command functions
    :::python
    from tronner import command
    @app.event('PLAYER_LEFT <name>')
    def goodbye(name):
        command.say("%s has left the building." % name)

## Custom command function
The commmands in the `command`-module write to standard output by default. If you're not using `SPAWN_SCRIPT`, or piping your script output to the server manually, you may need a different way of interacting with the server.

The following example demonstrates how one can override the function.
    
    :::python
    from tronner import command

    def custom_command(s):
        try:
            fh = fopen('input.txt', 'a')
            fh.write("%s\n" % s)
        except IOError:
            print "Could not write to input file"
        finally:
            fh.close()

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

You can also use the convenience function `register_default_events` which sets all the common events
for player tracking.

# Installation
Clone the repository to some directory on your server.

    :::bash
    git clone git@bitbucket.org:noob13/tronner.git

Create a symlink to tronner in your `data/scripts` directory.

    :::bash
    ln -s /path/to/tronner/ tronner

Alternatively, you can add the folder to your `PYTHONPATH` by adding a line like this to your `.bashrc`.

    :::bash
    export PYTHONPATH=$PYTHONPATH:/path/under/tronner/

## Requirements

- [Python](http://python.org) 2.7+

Tronner has not not been tested with earlier versions of python.

