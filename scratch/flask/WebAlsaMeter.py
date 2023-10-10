#! /bin/env python

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import alsacapture  # Import your custom alsacapture module

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('WebSocket Client Connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('WebSocket Client Disconnected')

def send_peak_amplitudes():
    audio_capture = alsacapture.open_capture()  # Create an instance of your custom AudioCapture class
    nm = 100/(2**15)

    try:
        #for i in range(1000):  # Adjust the number of iterations or add a condition to stop
        while True:
            length, data = audio_capture.read()
            if length:
                maxl, maxr = alsacapture.stereo_max(data)
                print(f'{maxl}      {maxr}')

                socketio.emit('peaks', {
                    'c1': f'{(maxl * nm):.2}',
                    'c2': f'{(maxr * nm):.2}'
                })
            socketio.sleep(0.06)  # Adjust the sleep time as needed
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    socketio.start_background_task(send_peak_amplitudes)
    socketio.run(app, host='0.0.0.0', port=5000)

