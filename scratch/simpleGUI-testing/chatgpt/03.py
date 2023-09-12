#!/usr/bin/python3

import sys
import wave
import numpy as np

def find_peak_amplitude(frame, as_percentage=False):
    frame_amplitudes = np.abs(frame).max(axis=0)
    if as_percentage:
        frame_amplitudes = (frame_amplitudes / 32767) * 100  # Convert to percentage
    return frame_amplitudes

def read_audio_frames_from_stdin(frame_size, as_percentage=False):
    # Read audio data from stdin as a binary stream
    while True:
        try:
            audio_data = sys.stdin.buffer.read(frame_size * 4)  # Read a frame (assuming 16-bit stereo samples)
            if len(audio_data) == 0:
                break  # Break when the input stream is closed
            audio_samples = np.frombuffer(audio_data, dtype=np.int16)
            audio_samples = audio_samples.reshape(-1, 2)  # Assuming stereo (2 channels)

            peak_amplitudes = find_peak_amplitude(audio_samples, as_percentage)
            yield peak_amplitudes

        except KeyboardInterrupt:
            break

# Parameters
frame_size = 16000  # Adjust this according to your needs
as_percentage = True  # Set this to True if you want peak amplitudes as percentages

# Read and process live audio frames from stdin
for i, peak_amplitudes in enumerate(read_audio_frames_from_stdin(frame_size, as_percentage)):
    print(f"Frame {i + 1}: Channel 1 Peak Amplitude: {peak_amplitudes[0]:.2f}{'%' if as_percentage else ''}, Channel 2 Peak Amplitude: {peak_amplitudes[1]:.2f}{'%' if as_percentage else ''}")

