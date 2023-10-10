#! /bin/env python

# Let's see if we can just open an alsa device and print something
# interesting

import alsaaudio, audioop

#ALSA_DEVICE = "plughw:0,7"  # My laptop's built-in mic
ALSA_DEVICE = "hw:1,0"  # My desktop's usb mic

# Probably the only parameters that count
SAMPLE_RATE = 44100
CHANNELS = 2
FORMAT = "PCM_FORMAT_S16_LE"
PERIOD_SIZE = 2048
PERIODS = 8

def open_capture(cap_device=ALSA_DEVICE):
    inp = alsaaudio.PCM( type=alsaaudio.PCM_CAPTURE,
        mode=alsaaudio.PCM_NONBLOCK,
        rate=44100,
        channels=CHANNELS,
        device=cap_device,
        format=alsaaudio.PCM_FORMAT_S16_LE,
        periodsize=PERIOD_SIZE,
        periods=PERIODS)
    return inp

def stereo_max(data):
    return [audioop.max(audioop.tomono(data,2,1,0),2) ,
            audioop.max(audioop.tomono(data,2,0,1),2) ]

def main():
    nm = 100/(2**15)
    print(nm)
    inp = open_capture()
    while True:
        length, data = inp.read()
        if length:
            maxl, maxr = stereo_max(data)
            print(f'{maxl}      {maxr}')
    inp.close()



if __name__ == '__main__' :
    main()

