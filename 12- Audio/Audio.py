
'''
The `gradio.Audio` component in Gradio allows users to upload, record, or play audio, functioning as both an input and output component. As input, it supports file paths or tuples containing sample rate and NumPy arrays of 16-bit audio data. As output, it can handle file paths, URLs, byte streams, or NumPy arrays (which are normalized to prevent clipping). It supports sources like uploads and microphones, offers configurable parameters like format (`wav`, `mp3`), autoplay, looping, and download buttons, and includes event listeners for actions like play, pause, record, and upload. This component is ideal for applications in speech recognition, music generation, and real-time audio processing. 🚀
'''

# Example 1: Basic Audio Input and Output
This example allows users to upload an audio file and play it back.

import gradio as gr

def play_audio(audio):
    return audio

demo = gr.Interface(
    fn=play_audio,
    inputs=gr.Audio(type="filepath"),
    outputs=gr.Audio(type="filepath")
)

demo.launch()


# Example 2: Audio Input with Microphone Source
This example allows users to record audio using their microphone and then play it back.

import gradio as gr

def play_audio(audio):
    return audio

demo = gr.Interface(
    play_audio,
    gr.Audio(sources=["microphone"], label="Record Audio"),
    "audio",
    title="Microphone Audio Playback Example",
    description="Record audio using your microphone and hear it back."
)

demo.launch()


# Example 3: Audio Input and Output with a Tone Generator
This example demonstrates generating a tone based on user input and playing it back.

import numpy as np
import gradio as gr

def generate_tone(note, octave, duration):
    sr = 48000
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note) + 12 * (octave - 4)
    frequency = 440 * 2 ** (note_index / 12)
    duration = int(duration)
    audio = np.linspace(0, duration, duration * sr)
    audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
    return sr, audio

demo = gr.Interface(
    generate_tone,
    [
        gr.Dropdown(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], label="Note"),
        gr.Slider(4, 6, step=1, label="Octave"),
        gr.Slider(1, 10, step=1, label="Duration (seconds)"),
    ],
    gr.Audio(type="numpy"),
    live=True
)

demo.launch()



# Example 4: Audio Input and Custom Waveform Options
This example demonstrates customizing the waveform display using WaveformOptions.

import numpy as np
import gradio as gr

def generate_tone(note, octave, duration):
    sr = 48000
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_index = notes.index(note) + 12 * (octave - 4)
    frequency = 440 * 2 ** (note_index / 12)
    duration = int(duration)
    audio = np.linspace(0, duration, duration * sr)
    audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
    return sr, audio

waveform_options = gr.WaveformOptions(waveform_color="#ff0000", waveform_progress_color="#00ff00", show_recording_waveform=True, show_controls=True, skip_length=0.5, sample_rate=48000)

demo = gr.Interface(
    generate_tone,
    [
        gr.Dropdown(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], label="Note"),
        gr.Slider(4, 6, step=1, label="Octave"),
        gr.Slider(1, 10, step=1, label="Duration (seconds)"),
    ],
    gr.Audio(type="numpy", waveform_options=waveform_options),
    live=True
)

demo.launch()



