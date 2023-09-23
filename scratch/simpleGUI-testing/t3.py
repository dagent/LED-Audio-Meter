#! /bin/env python

'''
Let's test out some argument parsing, and some sg layouts, and some pysimpleguiweb functionality.

All of this seems to work for the moment
'''

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

# Make 2 columns of (x1,x2) and a button
columnA = [[sg.Text(f"a{str(i)}", key=("a", i), enable_events=True)] for i in range(0,9)]
columnA.append( [ sg.Button("Press me", key=('a','-BUTTON-'))] )
columnB = [ [ sg.Text(f"b{str(i)}", key=("b", i)) ] for i in range(0,9) ]
columnB.append( [sg.Button("Press me", key=('-BUTTON-', 'b'))] )

# Hopefully this makes sense: The columns seems to have to call the Column method.
layout =  [ [sg.Column( columnA )  ,  sg.Column( columnB  ) ],
           [ sg.Text('placeholder', key='-TXTUPDATE-', justification='center') ],
           [ sg.Exit()]
           ]

if args.web:
    window = sg.Window("Column Tests", layout=layout, web_port=web_port)
else:
    window = sg.Window("Column Tests", layout=layout, finalize=True)

while True:
    event, values = window.read()
    print(event, values)

    window['-TXTUPDATE-'].update(f'{event} , {values}')
    if event == sg.WIN_CLOSED or event == 'Exit' :
        break

window.close()
del window