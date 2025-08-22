
---

### **gradio.Audio(···)**

#### **Description:**
Creates an audio component for uploading, recording, or displaying audio data. This component supports multiple functionalities such as taking audio as input or showing audio as output. 

#### **Behavior:**

- **As an input component:**  
  This component can accept audio in the form of:
  - `str`: A file path to an audio file.
  - `tuple[int, np.ndarray]`: A tuple consisting of the sample rate (in Hz) and the audio data as a 16-bit integer numpy array. The audio data will have values in the range from -32768 to 32767 and will have the shape `(samples,)` for mono audio or `(samples, channels)` for multi-channel audio.

    **Function Signature Example for Input:**
    ```python
    def predict(value: str | tuple[int, np.ndarray] | None):
        ...
    ```

- **As an output component:**  
  Expects audio data to be in one of the following formats:
  - `str`: Filepath or URL to an audio file.
  - `bytes`: Audio data as a byte object (ideal for streaming).
  - `tuple[int, np.ndarray]`: A tuple consisting of sample rate (in Hz) and the audio data as a numpy array.

    If the audio is provided as a numpy array, it will be normalized by its peak value to prevent distortion or clipping.

    **Function Signature Example for Output:**
    ```python
    def predict(···) -> str | Path | bytes | tuple[int, np.ndarray] | None:
        ...
        return value
    ```

#### **Initialization Parameters:**

- `value`: `str | Path | tuple[int, np.ndarray] | Callable | None`
  - Initial audio data (filepath or numpy array), or a callable function for generating audio.
- `sources`: `list[Literal['upload', 'microphone']]`
  - Defines whether the audio input comes from upload or microphone.
- `type`: `Literal['numpy', 'filepath']`
  - Specifies whether the input audio is in `numpy` or `filepath` format.
- `label`: `str | None`
  - Optional label for the component.
- `streaming`: `bool`
  - Enables or disables audio streaming.
- `format`: `Literal['wav', 'mp3'] | None`
  - Format for the audio file (e.g., WAV or MP3).
- `autoplay`: `bool`
  - If `True`, audio will autoplay upon loading.
- `show_download_button`: `bool | None`
  - If `True`, a download button is displayed for the audio.
- `editable`: `bool`
  - Allows users to edit or change the audio (e.g., trimming).
- `recording`: `bool`
  - If `True`, enables recording functionality.
- `waveform_options`: `gradio.WaveformOptions | dict | None`
  - Specifies options for the waveform display of the audio.

#### **Class Shortcuts:**
- `gradio.Audio` → Interface string: `"audio"`
- `gradio.Microphone` → Interface string: `"microphone"` (for microphone input).

#### **Demos:**

1. **Generate Tone:**
   Generates a sine wave for different musical notes.
   ```python
   import numpy as np
   import gradio as gr

   notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

   def generate_tone(note, octave, duration):
       sr = 48000
       a4_freq, tones_from_a4 = 440, 12 * (octave - 4) + (note - 9)
       frequency = a4_freq * 2 ** (tones_from_a4 / 12)
       duration = int(duration)
       audio = np.linspace(0, duration, duration * sr)
       audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
       return sr, audio

   demo = gr.Interface(
       generate_tone,
       [
           gr.Dropdown(notes, type="index"),
           gr.Slider(4, 6, step=1),
           gr.Textbox(value="1", label="Duration in seconds"),
       ],
       "audio",
   )
   if __name__ == "__main__":
       demo.launch()
   ```

#### **Event Listeners:**

Gradio's `Audio` component supports the following event listeners:

1. **Audio.stream(fn, ···)**  
   Triggered when the user streams the audio.

2. **Audio.change(fn, ···)**  
   Triggered when the value of the audio changes, either from user input (e.g., uploading or recording) or from function updates.

3. **Audio.clear(fn, ···)**  
   Triggered when the user clears the audio using the clear button.

4. **Audio.play(fn, ···)**  
   Triggered when the user plays the media in the audio.

5. **Audio.pause(fn, ···)**  
   Triggered when the media in the audio stops (e.g., pause or end of playback).

6. **Audio.stop(fn, ···)**  
   Triggered when the user reaches the end of the media playing.

7. **Audio.start_recording(fn, ···)**  
   Triggered when the user starts recording.

8. **Audio.pause_recording(fn, ···)**  
   Triggered when the user pauses the recording.

9. **Audio.stop_recording(fn, ···)**  
   Triggered when the user stops recording.

10. **Audio.upload(fn, ···)**  
   Triggered when the user uploads a file.

11. **Audio.input(fn, ···)**  
   Triggered when the user modifies the audio input.

#### **Event Parameters:**

- **fn**: The function or callable to be triggered on the event.
- **inputs**: The component(s) from which to collect input.
- **outputs**: The component(s) to display the results.
- **api_name**: Optional name for the API endpoint.
- **scroll_to_output**: Whether to scroll to the output after the event is triggered.
- **show_progress**: Controls how the progress bar is shown (full, minimal, or hidden).
- **queue**: Whether to queue multiple events for processing.
- **batch**: Whether to process events in batches.
- **trigger_mode**: How often the event triggers (`once`, `multiple`, or `always_last`).
- **concurrency_limit**: Limits the concurrency for the event handler.

---

