from __future__ import print_function
import sys

class Command(object):
    @staticmethod
    def say(message):
        print("SAY %s\n" % message)

    @staticmethod
    def pm(player, message):
        print("PLAYER_MESSAGE %s %s\n" % (player, message))

    @staticmethod
    def kick(player, reason="You have been kicked by tronner."):
        print("KICK %s %s\n" % (player, reason))

    @staticmethod
    def silence(player):
        print("SILENCE %s\n" % player)

    @staticmethod
    def voice(player):
        print("VOICE %s\n" % player)

    @staticmethod
    def command(command):
        print(command)
