from __future__ import print_function
import sys

def command(command):
    print(command)

def say(message):
    command("SAY %s" % message)

def pm(player, message):
    command("PLAYER_MESSAGE %s %s" % (player, message))

def kick(player, reason="You have been kicked by tronner."):
    command("KICK %s %s" % (player, reason))

def silence(player):
    command("SILENCE %s" % player)

def voice(player):
    command("VOICE %s" % player)

def center_message(message):
    command("CENTER_MESSAGE %s" % message)

def suspend(player, rounds=5):
    command("SUSPEND %s %d" % (player, rounds))

def kill(player):
    command("KILL %s" % player)

def console_message(message):
    command("CONSOLE_MESSAGE %s" % message)

def comment(message):
    command("# %s" % message)

def include(config):
    command('INCLUDE %s'% config)

def sinclude(config):
    command('SINCLUDE %s' % config)
