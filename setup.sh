#!/usr/bin/sh

mkdir venv
python3 -m venv ./venv
source ./venv/bin/activate
pip install sounddevice, soundfile, pyxhook, numpy