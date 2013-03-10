
Event Handling and Scripting Framework for Armagetron Advanced
==============================================================

# Examples
## A mininal greeter program
    :::python
    #!/usr/bin/env python
    from tronner import App
    app = App()

    @app.event('PLAYER_ENTERED')
    def player_entered():
        print "Greetings, program."

    app.run()

## Command functions
    :::python
    from tronner import command
    @app.event('PLAYER_LEFT')
    def goodbye(name):
        command.say("Good bye, %s" % name)

## An event with parameters
    :::python
    @app.event('DEATH_FRAG killed killer')
    def death_frag():
        print "%s killed %s for 1 point." % (killer, killed)


# Installation
First you will need to have [Python](http://python.org) installed on your server. Clone the repository to your scripts folder.
    git clone git@bitbucket.org:noob13/tronner.git
Alternatively, you can blah blah
## Requirements

