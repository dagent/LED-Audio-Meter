# LED-Audio-Meter

I need some way to monitor ALSA capture devices and set the capure level (hopefully with amixer, or pyalsaaudio).

This style is what I'm going for:
[Simple LED skin for VU Meter by tedgo on DeviantArt](https://www.deviantart.com/tedgo/art/Simple-LED-skin-for-VU-Meter-556117014)

## Goals/milestones
1. GUI mockup
    * Done-ish.  Both in pySimpleGui, and as a web page
2. Basic input from ALSA via STDIN
    * Exceeded -- audiocapture.py uses alsaaudio
3. Add capture level slider?
4. Port somehow to Web-interface
    * Proof-of-concept now with flask and flask-socketio

Have explored Python with
1. pySimpleGui (~~pySimpleGuiWeb~~ - Web version pretty bad.)  tK version OK
2. pyalsaaudio -- This was sorta great, along with built-in audiooop, and will be used.
3. flask -- have a semiworking version using flask-socketio

## Mockup
![Mockup from LED_meter.py](assets/LED_meter-mockup.png)