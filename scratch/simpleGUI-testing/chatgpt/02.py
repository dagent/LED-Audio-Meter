#!/usr/bin/python3

import sys
import wave
import numpy as np

def find_peak_amplitudes(audio_data, frame_size, num_frames, as_percentage=False):
    num_samples = len(audio_data)

    # Reshape the audio data into frames
    audio_frames = audio_data[:num_frames * frame_size].reshape(num_frames, frame_size)

    # Calculate peak amplitudes for each frame
    peak_amplitudes = []
    for frame in audio_frames:
        frame_amplitude = np.abs(frame).max()
        peak_amplitudes.append(frame_amplitude)

    if as_percentage:
        peak_amplitudes = (np.array(peak_amplitudes) / 32767) * 100  # Convert to percentage

    return peak_amplitudes

def read_audio_from_stdin():
    # Read audio data from stdin as a binary stream
    audio_data = sys.stdin.buffer.read()

    # Convert binary data to numerical samples
    audio_samples = np.frombuffer(audio_data, dtype=np.int16)

    return audio_samples

# Parameters
frame_size = 1024  # Adjust this according to your needs
num_frames = 100   # Adjust the number of frames you want to analyze
as_percentage = True  # Set this to True if you want peak amplitudes as percentages

# Read audio data from stdin
audio_samples = read_audio_from_stdin()

# Find peak amplitudes
peak_amplitudes = find_peak_amplitudes(audio_samples, frame_size, num_frames, as_percentage)

# Print or analyze the peak amplitudes as needed
for i, peak in enumerate(peak_amplitudes):
    print(f"Frame {i + 1}: Peak Amplitude: {peak:.2f}{'%' if as_percentage else ''}")

