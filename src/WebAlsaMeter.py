#! /bin/env python

#from flask import Flask, render_template
from flask import Flask, Response
from flask_socketio import SocketIO, emit
import argparse
import alsacapture

app = Flask(__name__, static_folder='htdocs', static_url_path='')
socketio = SocketIO(app)

@app.route('/')
def index():
    """Sends HTML file (GET /)"""
    return app.send_static_file('index.html')

@socketio.on('connect')
def handle_connect():
    print('WebSocket Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('WebSocket Client Disconnected')

def send_peak_amplitudes():
    audio_capture = alsacapture.open_capture()
    nm = 100/(2**15)

    try:
        while True:
            length, data = audio_capture.read()
            if length:
                maxl, maxr = alsacapture.stereo_max(data)
                #print(f'{maxl}      {maxr}')
                #print(f'{(maxl * nm):.1f}    {(maxr * nm):.1f}')

                socketio.emit('peaks', {
                    'c1': f'{(maxl * nm):.1f}',
                    'c2': f'{(maxr * nm):.1f}'
                })
            socketio.sleep(0.06)  # Adjust the sleep time as needed
    except Exception as e:
        print(f"Error: {e}")

def main():
    socketio.start_background_task(send_peak_amplitudes)
    socketio.run(app, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
