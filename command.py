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