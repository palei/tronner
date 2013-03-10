
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

The `spam` function will be executed every 10 seconds after round start.

## Command functions
    :::python
    from tronner import command
    @app.event('PLAYER_LEFT')
    def goodbye(name):
        command.say("Good bye, %s" % name)

## Custom command function
By default, the `command` function simply prints to stdout. If you're not using `SPAWN_SCRIPT` to run your script you may need a different way of interacting with the server console.
The following example demonstrates how you can override the function.
    
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

# Installation
Clone the repository to some directory on your server.

    :::bash
    git clone git@bitbucket.org:noob13/tronner.git

Create a symlink to tronner to your `data/scripts` directory.

    :::bash
    ln -s /path/to/tronner/ tronner

Alternatively, you can add the folder to your `PYTHONPATH` by adding a line like this to your `.bashrc`.

    :::bash
    export PYTHONPATH=$PYTHONPATH:/path/under/tronner/

## Requirements

