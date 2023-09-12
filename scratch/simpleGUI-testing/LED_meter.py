#! /usr/bin/env python


#import PySimpleGUIWeb as sg
import PySimpleGUI as sg
import time
import random

update_period = 100 # Essentially window timeout (ms)
maxed_meter_time = 3000 # How long the "red" meter stays lit (ms)
maxed_counter_init = int( maxed_meter_time / update_period )

led_height = 24
led_width = 48

"""
Inspired by 
https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_LED_Indicators.py
"""

def LEDIndicator(key=None, channel="", height=led_height, width=led_width):
    return sg.Graph(canvas_size=(width, height),
             graph_bottom_left=(0, 0),
             graph_top_right=(width, height),
             pad=(0, 0), key=key+channel)

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    #graph.draw_circle((0, 0), 12, fill_color=color, line_color="black")
    graph.draw_rectangle((0, 0), (led_width, led_height), fill_color=color, line_color="black")

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
    [ sg.Column(LED_banks["left"]) ,  sg.Column(LED_banks["right"])    ],
    [ sg.Button('Exit')                          ]
]

window = sg.Window('Randomized LED meter', layout,
       default_element_size=(12, 1), auto_size_text=False, finalize=True)

#i = 0
maxed_counter = {"left": 0, "right": 0 }
while True:  # Event Loop

    event, value = window.read(timeout=update_period)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if value is None:
        break
    #i += 1

    LED_update("left", random.randint(0, 100))
    LED_update("right", random.randint(0, 100))


window.close()


'''
if __name__ == '__main__':
    main()
'''
