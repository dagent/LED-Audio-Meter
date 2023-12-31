#!/bin/env python

import sys
import PySimpleGUI as sg
import numpy as np

def find_peak_amplitude(frame):
    frame_amplitudes = np.abs(frame).max(axis=0)
    return frame_amplitudes

def read_audio_frames_from_stdin(frame_size, max_amplitude):
    while True:
        try:
            audio_data = sys.stdin.buffer.read(frame_size * 4)  # Read a frame (assuming 16-bit stereo samples)
            if len(audio_data) == 0:
                break
            audio_samples = np.frombuffer(audio_data, dtype=np.int16)
            audio_samples = audio_samples.reshape(-1, 2)

            peak_amplitudes = find_peak_amplitude(audio_samples)
            normalized_amplitudes = (peak_amplitudes / max_amplitude) * 100  # Normalize to 100 for the progress bar
            yield normalized_amplitudes

        except KeyboardInterrupt:
            break

# Get frame size and max amplitude from command line arguments
frame_size = 1024  # Default frame size
max_amplitude = 32767  # Default max amplitude for 16-bit PCM

if len(sys.argv) > 1 and sys.argv[1] == "-f" and len(sys.argv) > 2:
    frame_size = int(sys.argv[2])

# Create a PySimpleGUI window
layout = [
    [sg.Text('Peak Amplitude Meter', font=('Helvetica', 12))],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressL')],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progressR')],
    [sg.Button('Exit')]
]

window = sg.Window('Audio Peak Amplitude Meter', layout, finalize=True)
progress_barL = window['progressL']
progress_barR = window['progressR']

# Read and process live audio frames from stdin
for i, normalized_amplitudes in enumerate(read_audio_frames_from_stdin(frame_size, max_amplitude)):
    # Update the progress bar based on the normalized amplitudes
    progress_barL.update_bar(int(normalized_amplitudes[0]))
    progress_barR.update_bar(int(normalized_amplitudes[1]))

    # Print the peak amplitudes to stdout
    print(f"Frame {i + 1}: Channel 1 Peak Amplitude: {normalized_amplitudes[0]:.2f}%, Channel 2 Peak Amplitude: {normalized_amplitudes[1]:.2f}%")

    # Check for events and close the window when the "Exit" button is clicked
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
