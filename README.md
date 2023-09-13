# LED-Audio-Meter

I need some way to monitor ALSA capture devices and set the capure level (hopefully with amixer, or pyalsaaudio).

This style is what I'm going for:
[Simple LED skin for VU Meter by tedgo on DeviantArt](https://www.deviantart.com/tedgo/art/Simple-LED-skin-for-VU-Meter-556117014)

## Goals/milestones
1. GUI mockup
2. Basic input from ALSA via STDIN
3. Add capture level slider?
4. Port somehow to Web-interface

Currently exploring Python with
1. pySimpleGui (and pySimpleGuiWeb)
2. pyalsaaudio

## Mockup
![Mockup from LED_meter.py](assets/LED_meter-mockup.png)