#!/bin/env python3

from __init__ import __version__
from TickeysCore import TickeysCore as Core
import Player

from cmd import Cmd
import sys


class CLI(Cmd):

    def __init__(self):
        super().__init__()
        self.intro = 'Tickeys_Alt %s - Linux\nType \'help\' for help' % __version__
        self.prompt = '>>> '

    def default(self, line):
        print('unknown command, try \'help\' for help')

    @staticmethod
    def help_theme():
        print('set sound theme from: ' + str(core.player.theme_list))

    @staticmethod
    def help_volume():
        print('set volume, from 0 to 100')

    @staticmethod
    def help_pitch():
        print('set sound pitch, from 0 to 30')

    @staticmethod
    def do_theme(arg):
        if arg in core.player.theme_list:
            core.player.set_theme(arg)
        else:
            print('unknown theme \"%s\". try \'help theme\' for help' % arg)

    @staticmethod
    def do_volume(arg):
        if 0 <= int(arg) <= 100:
            core.player.set_volume(int(arg) / 100.0)
        else:
            print('volume should be between 0 and 100')

    @staticmethod
    def do_pitch(arg):
        if 0 <= int(arg) <= 30:
            core.player.set_pitch(int(arg) / 30.0)
        else:
            print('pitch should be between 0 and 30')

    @staticmethod
    def do_exit(arg):
        try:
            core.stop()
        except Exception:
            pass
        finally:
            sys.exit(0)

core = Core()
if __name__ == '__main__':
    cli = CLI()
    core.start()
    cli.cmdloop()
