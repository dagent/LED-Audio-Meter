# LED-Audio-Meter
Web based peak level (VU) meter.

## Motivation

I need a way to monitor ALSA capture devices input levels, and I wanted it done in a web browser.  After some exaustive searching, I decided to make my own.

Here's what I've got working in `src/`:

![Mockup from flask](assets/LED_meter_flask.png)

## Requirements
Stilll getting requirements.txt in order and getting rid of devel cruft, but basically:
* flask
* flask-socketio
* pyalsalaudio
* audioop - so useful, but [deprecated beginning 3.13](https://docs.python.org/3/library/audioop.html)

## Python version
Development for this was initiated on a box running Linux Mint 19.3 (for which some hardware has specific drivers), and which has Python 3.6.9 installed.  I've also used it on a Python 3.8 system with no problem.
