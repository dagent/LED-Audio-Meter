#!/bin/env python
'''
Just trying to see if I can make some empty textboxes and change the background color such that it looks like a meter.
'''

import PySimpleGUIWeb as sg
#import PySimpleGUI as sg

last_val = 0  # running value to display
rec_height=1
rec_width=8

def mkRectangle(h=rec_height,w=rec_width,color="grey",key=None):
    return [ sg.Text( size=(w,h), key=key, background_color=color) ]

rect_ind = [5,10,50,100]

rect_elem = [  mkRectangle(key=('BB', i)) for i in rect_ind ] 
rect_elem.reverse()
buttons = [ sg.Button('0', key=('button',0 ) ) ] + [ sg.Button(f'{i}', key=('button', i)) for i in rect_ind ] 

#print(rect_elem)
layout = [
    [ sg.Column(rect_elem) ],
     buttons 
]

def update_rect(rect , val=0):
    global last_val
    global rect_ind
    print(f'val={val}, last_val={last_val}')
    if val == last_val:
        print('return')
        return
    if val > last_val:
        changes = [ i for i in rect_ind if last_val < i <= val ]
        print(changes)
        for i in changes:
            print(f'redraw {i}')
            rect[('BB', i)].update(background_color='yellow')
    if val < last_val:
        changes = [ i for i in rect_ind if last_val >= i > val ]
        changes.reverse();
        print(changes)
        for i in changes:
            print(f'erase {i}')
            rect[('BB', i)].update(background_color='grey')
    last_val = val


    
    
window = sg.Window("Rectangle Test", layout, finalize=True)

while True:
    event, values = window.read()
    #print(f'{event} : {values}')
    if event in [sg.WIN_CLOSED, None]:
        break
    if 'button' in event:
        #print(event[1])
        update_rect(window, event[1])
window.close()
