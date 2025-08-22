'''
The Gradio Gallery component is a versatile tool for displaying a grid of images or videos with optional captions. 
It can be used both as an input and an output component in a Gradio app. When used as an input, users can upload images 
or videos to the gallery. When used as an output, users can click on individual images or videos to view them at a higher 
resolution. The gallery supports various configurations, including the number of columns and rows, object fit, and preview options.
'''

# Example 1: Display Static Images

import gradio as gr

def display_images():
    images = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
    ]
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Static Images", columns=[3], rows=[1], object_fit="contain")
    btn = gr.Button("Display Images")

    btn.click(display_images, None, gallery)

demo.launch()

# (-------------------------------------------------------------------------------------------------)

# Example 2: Display Images with Captions

import gradio as gr

def display_images():
    images = [
        ("https://example.com/image1.jpg", "Caption 1"),
        ("https://example.com/image2.jpg", "Caption 2"),
        ("https://example.com/image3.jpg", "Caption 3")
    ]
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Images with Captions", columns=[3], rows=[1], object_fit="contain")
    btn = gr.Button("Display Images")

    btn.click(display_images, None, gallery)

demo.launch()

# (--------------------------------------------------------------------------------------------------)

# Example 3: Allow User Uploads

import gradio as gr

def display_images(images):
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Upload Images", columns=[5], object_fit="contain")
    btn = gr.Button("Upload Images")

    btn.click(display_images, gallery, gallery)

demo.launch()

# (----------------------------------------------------------------------------------------------------)

# Example 4: Display Videos

import gradio as gr

def display_videos():
    videos = [
        "https://example.com/video1.mp4",
        "https://example.com/video2.mp4",
        "https://example.com/video3.mp4"
    ]
    return videos

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Videos", columns=[3], rows=[1], object_fit="contain")
    btn = gr.Button("Display Videos")

    btn.click(display_videos, None, gallery)

demo.launch()

# (------------------------------------------------------------------------------------------------------)

# Example 5: Display Images with Preview

import gradio as gr

def display_images():
    images = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
    ]
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Images with Preview", columns=[3], rows=[1], object_fit="contain", allow_preview=True)
    btn = gr.Button("Display Images")

    btn.click(display_images, None, gallery)

demo.launch()

# (------------------------------------------------------------------------------------------------------)

# Example 6: Display Images with Fullscreen Option

import gradio as gr

def display_images():
    images = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
    ]
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Images with Fullscreen", columns=[3], rows=[1], object_fit="contain", show_fullscreen_button=True)
    btn = gr.Button("Display Images")

    btn.click(display_images, None, gallery)

demo.launch()

# (------------------------------------------------------------------------------------------------------)

# Example 7: Display Images with Download Option
import gradio as gr

def display_images():
    images = [
        "https://example.com/image1.jpg",
        "https://example.com/image2.jpg",
        "https://example.com/image3.jpg"
    ]
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(label="Images with Download", columns=[3], rows=[1], object_fit="contain", show_download_button=True)
    btn = gr.Button("Display Images")

    btn.click(display_images, None, gallery)

demo.launch()

# (--------------------------------------------------------------------------------------------------------)