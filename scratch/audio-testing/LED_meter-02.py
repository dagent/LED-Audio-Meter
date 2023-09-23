#! /usr/bin/env python

import audiocapture as ac

web_port=10422  # Default webserver port if running pysimpleguiweb

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--web", help="run in a web browser", action="store_true")
parser.add_argument("-p", "--port", help="Web server port", default=web_port)
args = parser.parse_args()

if args.web:
    import PySimpleGUIWeb as sg
    if args.port:
        web_port = int(args.port)
else:
    import PySimpleGUI as sg

update_period = 300 # Essentially window timeout (ms)
maxed_meter_time = 2000 # How long the "red" meter stays lit (ms)
maxed_counter_init = maxed_meter_time // update_period

led_height = 24
led_width = 48

def LEDIndicator(key=None, channel="", height=led_height, width=led_width):
    return sg.Graph(canvas_size=(width, height),
        graph_bottom_left=(0, 0),
        graph_top_right=(width, height),
        pad=(0, 0), key=key+channel)

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_rectangle((0, led_height), (led_width, 0), fill_color=color, line_color="black")

def LED_bank(channel="" ):
    return [
    [ LEDIndicator('_max_', channel)],
    [ LEDIndicator('_80_', channel)],
    [ LEDIndicator('_40_', channel)],
    [ LEDIndicator('_20_', channel)],
    [ LEDIndicator('_10_', channel)],
    [ LEDIndicator('_5_', channel)],
    [ LEDIndicator('_0_', channel)],
    ]

LED_banks = { "left": LED_bank("left") ,  "right": LED_bank("right") }

def LED_update(channel, value):  
    if value > 90:
        maxed_counter[channel] = maxed_counter_init 
        SetLED(window, '_max_'+channel, 'red')
    elif maxed_counter[channel] > 0:
        maxed_counter[channel] -= 1
    else:
        SetLED(window, '_max_'+channel, 'grey')

    SetLED(window, '_80_'+channel, 'yellow' if value > 80 else 'grey')
    SetLED(window, '_40_'+channel, 'yellow' if value > 40 else 'grey')
    SetLED(window, '_20_'+channel, 'yellow' if value > 20 else 'grey')
    SetLED(window, '_10_'+channel, 'yellow' if value > 10 else 'grey')
    SetLED(window, '_5_'+channel, 'yellow' if value > 5 else 'grey')
    SetLED(window, '_0_'+channel, 'yellow' if value > 0 else 'grey')


layout = [
    [ sg.Text('LED Meter'), sg.Text("2")           ],
    [ sg.Column( LED_banks["left"]) ,  sg.Column( LED_banks["right"] )    ],
    [ sg.Button('Exit')                          ]
]

if args.web:
    window = sg.Window('Randomized LED meter', layout, web_port=10422, default_element_size=(12, 1), auto_size_text=False) #, finalize=True)
else:
    window = sg.Window('Randomized LED meter', layout, default_element_size=(12, 1), auto_size_text=False, finalize=True)

maxed_counter = {"left": 0, "right": 0 }

inp = ac.open_capture()

full_scale_multiplier = 100/32767

while True:  # Event Loop

    event, value = window.read(timeout=update_period)
    if event in ['Exit', sg.WIN_CLOSED, None]:
        break
    if value is None:
        break

    ldata, data = inp.read()
    maxl, maxr = ac.stereo_max(data)
    LED_update("left", maxl * full_scale_multiplier )
    LED_update("right", maxl * full_scale_multiplier )

window.close()

'''
if __name__ == '__main__':
    main()
'''

