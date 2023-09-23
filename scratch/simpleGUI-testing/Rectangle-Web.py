#!/bin/env python
'''
Just trying to see if I can make some rectangles...
https://www.pysimplegui.org/en/latest/#graph-element
https://www.pysimplegui.org/en/latest/call%20reference/#graph-element
https://www.pysimplegui.org/en/latest/cookbook/#graph-element-drawing-circle-rectangle-etc-objects

Coordinate systems are whack.  Canvas declared with WxH, then bottom-left and top-right.  Rectangles 
declared as top-left and bottom-right.
'''

#import PySimpleGUIWeb as sg
import PySimpleGUI as sg

last_val = 0  # running value to display
rec_height=24
rec_width=96

def mkRectangle(h=rec_height,w=rec_width,color="grey",key=None):
    return [ sg.Graph( canvas_size=(w,h), graph_bottom_left=(0,0), graph_top_right=(w,h) ,key=key, background_color=color) ]

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
    print(f'val={val}, last_val={last_val}')
    if val == last_val:
        print('return')
        return
    if val > last_val:
        changes = [ i for i in rect_ind if last_val < i <= val ]
        print(changes)
        for i in changes:
            print(f'redraw {i}')
            #rect[('BB', i)].erase()
            rect[('BB', i)].draw_rectangle((0, rec_height), (rec_width,0), fill_color='yellow')
    if val < last_val:
        changes = [ i for i in rect_ind if last_val >= i > val ]
        print(changes)
        for i in changes:
            print(f'erase {i}')
            rect[('BB', i)].erase()
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
