'''
Gradio's Video component is a versatile tool for handling video data in Gradio interfaces. Whether you need to upload, 
record, or display videos, this component supports a variety of formats and codecs. The component ensures that the video 
is playable in the browser by converting it if necessary to one of the supported formats: .mp4 with h264, .ogg with 
theora, and .webm with vp9.
'''

# Example 1: Basic Video Upload and Display

import gradio as gr

def display_video(video):
    return video

demo = gr.Interface(
    display_video,
    gr.Video(label="Upload Video"),
    gr.Video(label="Uploaded Video"),
    title="Video Upload and Display",
    description="Upload a video and see it displayed."
)

demo.launch()

# (---------------------------------------------------------------------------------------)

# Example 2: Video Autoplay and Loop

import gradio as gr

def video_identity(video):
    return video

demo = gr.Interface(
    fn=video_identity,
    inputs=gr.Video(label="Upload Video"),
    outputs=gr.Video(autoplay=True, loop=True, label="Autoplay and Loop Video"),
    title="Autoplay and Loop Video",
    description="Upload a video, and it will autoplay and loop."
)

demo.launch()

# (-----------------------------------------------------------------------------------------)

# Example 3: Video with Download Button

import gradio as gr

def video_identity(video):
    return video

demo = gr.Interface(
    fn=video_identity,
    inputs=gr.Video(label="Upload Video"),
    outputs=gr.Video(show_download_button=True, label="Downloadable Video"),
    title="Video with Download Button",
    description="Upload a video, and it will be displayed with a download button."
)

demo.launch()

# (-------------------------------------------------------------------------------------------)

# Example 4: Video with Specific Dimensions

import gradio as gr

def video_identity(video):
    return video

demo = gr.Interface(
    fn=video_identity,
    inputs=gr.Video(label="Upload Video"),
    outputs=gr.Video(height=200, width=200, label="Resized Video"),
    title="Video with Specific Dimensions",
    description="Upload a video, and it will be displayed with specific dimensions."
)

demo.launch()


# (---------------------------------------------------------------------------------------------)








