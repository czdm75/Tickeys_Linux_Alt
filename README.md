![Tickeys Icon](http://img.blog.csdn.net/20150802103616846)

# Introduce

Tickeys is an powerful keyboard sound effect tool。Tickeys now brings seven sound styles，include Bubble, Typewriter, Mechanical, Sword, etc.

This tool have Windows and Mac version，Mac Version:([GitHub](https://github.com/yingDev/Tickeys))

---------------

Originally forked from [Tickeys-linux](https://github.com/BillBillBillBill/Tickeys-linux) by [BillBillBillBill](https://github.com/BillBillBillBill) . (Thanks A Lot!)

In this very early version 0.1.0, I simply ported the CLI version to Python3 and fixed lot of typos in the source code. I'm new to Python, so feel free to make an Issue or a PR, Especially help me to write the setup shell script.

# Project Website
http://www.yingdev.com/projects/tickeys

# Installation & Usage

Very early version, so not packed yet. First, make sure you have python >= 3.4 installed.

### Use Venv

**Recommended**, Since I haven't started the GUI part, so the dependency is not settled.

After cloning this repo, run setup.sh, or in the terminal:

```sh
mkdir venv
python3 -m venv ./venv
source ./venv/bin/activate
pip install sounddevice, soundfile, pyxhook, numpy
```

Then simply `python3 CLI.py` should work.

### System-Wide Python

**Not Recommended**.

Since `pyxhook` is not in most of the Distros, (even AUR! ) yet, simply downloading the `pyxhook.py` [here](https://github.com/JeffHoogland/pyxhook) and put it in the same folder that `CLI.py` in would be great.

# TODO

Re-implement the GUI. 

# Dependencies

* numpy==1.14.0
* pyxhook==1.0.0
* sounddevice==0.3.10
* SoundFile==0.9.0.post1