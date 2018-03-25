#!/bin/env python3

from json import load, dump
from sounddevice import play
from soundfile import read
from random import randrange
import os

# Constants
config_path = os.environ["HOME"] + '/.local/share/tickeys_alt/config.json'
scheme_path = './Resources/data/schemes.json'


class Player:

    def play_sound(self, key):
        key = str(key)
        if key in self.key_audio_map.keys():
            sound_no = self.key_audio_map[key]
        else:
            sound_no = randrange(0, self.non_unique_count)
        if self.caching == False :
            data, sf = self.wav_data[sound_no]
            play(data, sf)

    # Set Options
    def set_theme(self, theme):
        self.config['theme'] = theme
        self.dump_config()
        self.cache_sound_effect()

    def set_volume(self, volume):
        self.config['volume'] = volume
        self.dump_config()
        self.cache_sound_effect()

    def set_pitch(self, pitch):
        self.config['pitch'] = pitch
        self.dump_config()
        self.cache_sound_effect()

    # Read Sound, enable volume and Pitch, Cache in RAM
    def cache_sound_effect(self):
        self.caching = True
        # Load Sound Themes
        with open(scheme_path) as f:
            json_obj = load(f)
            scheme = dict((i['name'], i) for i in json_obj)
            self.theme_list = list(i['name'] for i in json_obj)
        self.key_audio_map = scheme[self.config['theme']]['key_audio_map']
        self.non_unique_count = scheme[self.config['theme']]['non_unique_count']

        self.wav_data = []
        for filename in scheme[self.config['theme']]['files']:
            sound_file_path = './Resources/data/%s/%s' % (self.config['theme'], filename)
            wave, sample_rate = read(sound_file_path)
            self.wav_data.append((wave * self.config['volume'], sample_rate * self.config['pitch']))
        self.caching = False

    def load_config(self):
        if os.path.isfile(config_path):
            with open(config_path, 'r') as file:
                self.config = load(file)
        else:
            self.config = {'theme': 'typewriter', 'volume': 1, 'pitch': 1}
            self.dump_config()

    def dump_config(self):
        if not os.path.exists(os.environ["HOME"] + '/.local/share/tickeys_alt'):
            os.makedirs(os.environ["HOME"] + '/.local/share/tickeys_alt')
        if not os.path.isfile(config_path):
            os.system(r'touch %s' % 'config.json')

        with open(config_path, 'w') as f:
            dump(self.config, f)

    def __init__(self):
        self.theme_list = []
        self.wav_data = []  # Stores (Byte, SampleRate that is already volume and pitch enabled)
        self.key_audio_map = {}  # Unique Sounds
        self.non_unique_count = 0  # Normal Sound Count
        self.config = {}
        self.load_config()
        self.caching = False
        self.cache_sound_effect()

