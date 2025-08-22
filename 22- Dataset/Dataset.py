'''
The Gradio Dataset component is a versatile tool for displaying and interacting with datasets in a web-based interface. 
It can present data as a gallery or a table, allowing users to select samples and interact with them. This component is 
particularly useful for demonstrating and showcasing machine learning models, as it can display input and output data 
samples alongside each other. Users can select samples from the dataset, and the selected data can be used to trigger 
other components or functions in your Gradio app.
'''

# Example 1: Displaying Text Samples in a Gallery
import gradio as gr

# Define text samples
text_samples = [
    ["The quick brown fox jumps over the lazy dog"],
    ["Build & share delightful machine learning apps"],
    ["She sells seashells by the seashore"],
    ["Supercalifragilisticexpialidocious"],
    ["Lorem ipsum"],
    ["That's all folks!"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with a textbox to display text samples
    dataset = gr.Dataset(components=[gr.Textbox()], samples=text_samples, layout="gallery", headers=["Sample Text"])

# Launch the app
demo.launch()

# (-------------------------------------------------------------------------------------------------------------------------)

# Example 2: Displaying Images in a Gallery

import gradio as gr

# Define image samples
image_samples = [
    ["https://cdn.pixabay.com/photo/2017/03/17/11/50/car-2151324_1280.jpg"],
    ["https://cdn.pixabay.com/photo/2016/05/05/18/01/coupe-1374436_1280.jpg"],
    ["https://cdn.pixabay.com/photo/2016/05/05/18/02/coupe-1374444_1280.jpg"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with an image component to display image samples
    dataset = gr.Dataset(components=[gr.Image()], samples=image_samples, layout="gallery", headers=["Sample Image"])

# Launch the app
demo.launch()

# (--------------------------------------------------------------------------------------------------------------------------)


# Example 3: Displaying Multiple Components per Sample

import gradio as gr

# Define samples with multiple components
samples = [
    ["The quick brown fox jumps over the lazy dog", "images/image1.jpg"],
    ["Build & share delightful machine learning apps", "images/image2.jpg"],
    ["She sells seashells by the seashore", "images/image3.jpg"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with a textbox and image component
    dataset = gr.Dataset(components=[gr.Textbox(), gr.Image()], samples=samples, layout="table", headers=["Text", "Image"])

# Launch the app
demo.launch()

# (--------------------------------------------------------------------------------------------------------------------------)

# Example 4: Displaying Tabular Data

import gradio as gr

# Define tabular data samples
samples = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Charlie", 35, "Manager"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with textboxes to display tabular data
    dataset = gr.Dataset(components=[gr.Textbox(), gr.Number(), gr.Textbox()], samples=samples, layout="table", headers=["Name", "Age", "Job"])

# Launch the app
demo.launch()

# (-----------------------------------------------------------------------------------------------------------------------)

# Example 5: Customizing Layout and Appearance

import gradio as gr

# Define image samples
image_samples = [
    ["images/image1.jpg"],
    ["images/image2.jpg"],
    ["images/image3.jpg"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with an image component
    dataset = gr.Dataset(
        components=[gr.Image()],
        samples=image_samples,
        layout="gallery",
        headers=["Sample Image"],
        samples_per_page=2,
        visible=True,
        elem_id="custom-dataset",
        elem_classes=["custom-class"]
    )

# Launch the app
demo.launch()

# (--------------------------------------------------------------------------------------------------------------------------)


# Example 6: Displaying Audio Samples

import gradio as gr

# Define audio samples
audio_samples = [
    ["audios/audio1.mp3"],
    ["audios/audio2.mp3"],
    ["audios/audio3.mp3"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with an audio component
    dataset = gr.Dataset(components=[gr.Audio()], samples=audio_samples, layout="gallery", headers=["Sample Audio"])

# Launch the app
demo.launch()


# (---------------------------------------------------------------------------------------------------------------------------)

# Example 7: Displaying Video Samples

import gradio as gr

# Define video samples
video_samples = [
    ["videos/video1.mp4"],
    ["videos/video2.mp4"],
    ["videos/video3.mp4"]
]

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    # Create a Dataset component with a video component
    dataset = gr.Dataset(components=[gr.Video()], samples=video_samples, layout="gallery", headers=["Sample Video"])

# Launch the app
demo.launch()