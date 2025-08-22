'''
The gradio.Sidebar component in Gradio is a collapsible panel that can be placed on the left or right side 
of the screen within a Blocks layout. It is useful for organizing UI elements in a clean and user-friendly 
manner, allowing users to access additional controls or information without cluttering the main interface.
'''

# Example 1: Basic Sidebar with Textbox and Button

import gradio as gr

with gr.Blocks() as demo:
    with gr.Sidebar(label="Settings"):
        gr.Textbox(label="Enter Text")
        gr.Button("Submit")

demo.launch()

# (--------------------------------------------------------------------------------)

# Example 2: Sidebar with Default Open State
import gradio as gr

with gr.Blocks() as demo:
    with gr.Sidebar(label="Settings", open=True):
        gr.Textbox(label="Enter Text")
        gr.Button("Submit")

demo.launch()

# (--------------------------------------------------------------------------------)

# Example 3: Sidebar with Custom Width
import gradio as gr

with gr.Blocks() as demo:
    with gr.Sidebar(label="Settings", width=300):
        gr.Textbox(label="Enter Text")
        gr.Button("Submit")

demo.launch()

# (--------------------------------------------------------------------------------)

# Example 4: Sidebar with Collapsible and Expandable Events
import gradio as gr

def on_expand():
    return "Sidebar Expanded"

def on_collapse():
    return "Sidebar Collapsed"

with gr.Blocks() as demo:
    with gr.Sidebar(label="Settings") as sidebar:
        gr.Textbox(label="Enter Text")
        gr.Button("Submit")
    
    output = gr.Textbox(label="Event Output")
    sidebar.expand(fn=on_expand, outputs=output)
    sidebar.collapse(fn=on_collapse, outputs=output)

demo.launch()

# (---------------------------------------------------------------------------------)

# Example 5: Sidebar with Visibility Control
import gradio as gr

def toggle_visibility(visible):
    return not visible

with gr.Blocks() as demo:
    visible = gr.Checkbox(value=True, label="Toggle Sidebar Visibility")
    with gr.Sidebar(label="Settings", visible=True) as sidebar:
        gr.Textbox(label="Enter Text")
        gr.Button("Submit")
    
    visible.change(fn=toggle_visibility, inputs=visible, outputs=sidebar)

demo.launch()

# (----------------------------------------------------------------------------------)


# Example 6: Sidebar with Visibility Control


import gradio as gr

def toggle_sidebar_visibility(visible):
    if visible:
        return gr.update(visible=True), ""
    else:
        return gr.update(visible=False), ""

with gr.Blocks() as demo:
    visible = gr.Checkbox(value=True, label="Toggle Sidebar Visibility")
    
    css_container = gr.HTML("")   
    
    with gr.Sidebar():
        with gr.Column(visible=True) as sidebar:
            gr.Textbox(label="Enter Text")
            gr.Button("Submit")

    visible.change(fn=toggle_sidebar_visibility, inputs=visible, outputs=[sidebar, css_container])

demo.launch()


# (------------------------------------------------------------------------------------)

# Example 7: Sidebar with Multiple Components
import gradio as gr

with gr.Blocks() as demo:
    with gr.Sidebar(label="Settings"):
        gr.Textbox(label="Name")
        gr.Slider(label="Age", minimum=0, maximum=100)
        gr.Checkbox(label="Subscribe to Newsletter")
        gr.Button("Submit")

demo.launch()

# (------------------------------------------------------------------------------------)

# Example 8: Sidebar with Image Upload and Display
import gradio as gr
from PIL import Image

def process_image(image_path):
    img = Image.open(image_path)
    return img

with gr.Blocks() as demo:
    with gr.Sidebar(label="Image Operations"):
        image_input = gr.File(label="Upload Image", type="filepath")  # Fix here
        image_output = gr.Image(label="Processed Image")
        gr.Button("Process Image").click(fn=process_image, inputs=image_input, outputs=image_output)

demo.launch()


# (------------------------------------------------------------------------------------)













