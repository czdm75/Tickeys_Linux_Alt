#!/bin/env python3

from Player import Player
from pyxhook import HookManager
import threading


class TickeysCore:

    hot_key_list = [24, 38, 52, 10, 11, 12]  # QAZ123
    hot_key_list2 = [24, 38, 52, 87, 88, 89]  # QAZ123 with 123 in side keyboard

    # Hook Function
    def play_sound(self, event):
        self.player.play_sound(event.ScanCode)
        self.check_show_window(event.ScanCode)

    # Check If QAZ123 Is Pushed, GUI Related
    def check_show_window(self, scan_code):
        pass

    # Start And Stop
    def start(self):
        self.hm_thread = threading.Thread(target=self.hook_man.start, args=())
        self.hm_thread.start()

    def stop(self):
        self.hook_man.cancel()

    def __init__(self):
        self.player = Player()
        self.hook_man = HookManager()
        self.hook_man.KeyDown = self.play_sound
