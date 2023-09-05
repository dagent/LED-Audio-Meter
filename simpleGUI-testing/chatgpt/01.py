#!/usr/bin/python3

import wave
import numpy as np

def find_peak_amplitudes(audio_file, frame_size, num_frames):
    # Open the audio file
    with wave.open(audio_file, 'rb') as wav_file:
        sample_width = wav_file.getsampwidth()
        num_channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()
        num_samples = wav_file.getnframes()

        # Calculate the number of samples per frame
        samples_per_frame = frame_size * num_channels

        # Read all audio samples
        audio_data = np.frombuffer(wav_file.readframes(num_samples), dtype=np.int16)

        # Reshape the audio data into frames
        audio_frames = audio_data[:num_frames * samples_per_frame].reshape(num_frames, frame_size, num_channels)

        # Calculate peak amplitudes for each frame
        peak_amplitudes = []
        for frame in audio_frames:
            frame_amplitudes = np.abs(frame).max(axis=0)
            peak_amplitudes.append(frame_amplitudes)

    return peak_amplitudes

# Parameters
#audio_file = 'path/to/your/audio/file.wav'
audio_file = '/home/gent/Desktop/20191202-DG+RG.WAV'
frame_size = 1024  # Adjust this according to your needs
num_frames = 100   # Adjust the number of frames you want to analyze

# Find peak amplitudes
peak_amplitudes = find_peak_amplitudes(audio_file, frame_size, num_frames)

# Print or analyze the peak amplitudes as needed
for i, peaks in enumerate(peak_amplitudes):
    print(f"Frame {i + 1}: Channel 1 Peak Amplitude: {peaks[0]}, Channel 2 Peak Amplitude: {peaks[1]}")

