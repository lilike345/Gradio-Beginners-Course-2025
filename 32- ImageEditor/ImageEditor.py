'''
Gradio's ImageEditor component is a powerful tool that allows users to upload, edit, and manipulate images directly within 
a Gradio interface. It supports various editing tools such as brushes, strokes, cropping, and layers. The component can be 
used both as an input and output, making it versatile for different applications.
'''

# Example 1: Basic Image Editor


import gradio as gr

def predict(im):
    return im["composite"]

with gr.Blocks() as demo:
    im_editor = gr.ImageEditor(type="pil")
    im_preview = gr.Image(type="pil")
    im_editor.change(predict, outputs=im_preview, inputs=im_editor)

demo.launch()

# (---------------------------------------------------------------------------------------)

# Example 2: Image Editor with Multiple Layers

import gradio as gr

def predict(im):
    return im["composite"]

with gr.Blocks() as demo:
    im_editor = gr.ImageEditor(type="pil", layers=True)
    im_preview = gr.Image(type="pil")
    im_editor.change(predict, outputs=im_preview, inputs=im_editor)

demo.launch()

# (---------------------------------------------------------------------------------------)

# Example 3: Image Editor with Fixed Canvas

import gradio as gr

def predict(im):
    return im["composite"]

with gr.Blocks() as demo:
    im_editor = gr.ImageEditor(type="pil", canvas_size=(512, 512), fixed_canvas=True)
    im_preview = gr.Image(type="pil")
    im_editor.change(predict, outputs=im_preview, inputs=im_editor)

demo.launch()

# (----------------------------------------------------------------------------------------)

# Example 4: Multiple Image Editors with Individual Previews

import gradio as gr

def predict(im):
    return im["composite"]

with gr.Blocks() as demo:
    im_editor1 = gr.ImageEditor(type="pil", label="Image Editor 1")
    im_editor2 = gr.ImageEditor(type="pil", label="Image Editor 2")
    im_editor3 = gr.ImageEditor(type="pil", label="Image Editor 3")
    
    im_preview1 = gr.Image(type="pil", label="Preview 1")
    im_preview2 = gr.Image(type="pil", label="Preview 2")
    im_preview3 = gr.Image(type="pil", label="Preview 3")
    
    im_editor1.change(predict, outputs=im_preview1, inputs=im_editor1)
    im_editor2.change(predict, outputs=im_preview2, inputs=im_editor2)
    im_editor3.change(predict, outputs=im_preview3, inputs=im_editor3)

demo.launch()

# (----------------------------------------------------------------------------------------)

