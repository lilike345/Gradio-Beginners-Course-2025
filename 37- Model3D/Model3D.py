'''
The Model3D component in Gradio allows users to upload and view 3D model files in various formats such as 
.obj, .glb, .stl, .gltf, .splat, and .ply. This component can be used both as an input and an output component 
 in Gradio interfaces.
'''

# Example 1: Basic Input and Output

import gradio as gr

def display_model(model_path):
    return model_path

iface = gr.Interface(
    fn=display_model,
    inputs=gr.Model3D(label="Upload a 3D Model"),
    outputs=gr.Model3D(label="Uploaded Model"),
    title="3D Model Viewer",
    description="Upload a 3D model file (.obj, .glb, .stl, .gltf, .splat, .ply) and view it here."
)
iface.launch()

# (------------------------------------------------------------------------------------------------------)

# Example 2. Model3D with Custom Camera Position

import gradio as gr

def display_model(model_path):
    return model_path

iface = gr.Interface(
    fn=display_model,
    inputs=gr.Model3D(label="Upload 3D Model"),
    outputs=gr.Model3D(camera_position=(0, 0, 5), label="Uploaded Model"),
    title="3D Model Viewer",
    description="Upload a 3D model and view it with a custom camera position."
)

iface.launch()

# (-------------------------------------------------------------------------------------------------------)

# Example 3: Playing with clear_color

import gradio as gr

def predict(value):
    return value

iface = gr.Interface(
    fn=predict,
    inputs=gr.Model3D(label="Upload a 3D Model", clear_color=(0.1, 0.1, 0.1, 1.0)),
    outputs=gr.Model3D(label="Uploaded 3D Model", clear_color=(0.9, 0.9, 0.9, 1.0))
)

iface.launch()

# (--------------------------------------------------------------------------------------------------------)

# Example 4: Zoom and Pan Speed

import gradio as gr

def predict(value):
    return value

iface = gr.Interface(
    fn=predict,
    inputs=gr.Model3D(label="Upload a 3D Model", zoom_speed=0.5, pan_speed=0.5),
    outputs=gr.Model3D(label="Uploaded 3D Model", zoom_speed=1.0, pan_speed=1.0)
)

iface.launch()

