'''

Gradio's ColorPicker component provides a user-friendly interface for selecting colors. It allows users to pick a color 
and returns the selected color as a hexadecimal string (#RRGGBB). This component can be used both as an input and an 
output in Gradio interfaces.


'''

# Example 1: Basic Color Picker
import gradio as gr

def show_color(color):
    return color

demo = gr.Interface(
    fn=show_color,
    inputs=gr.ColorPicker(label="Pick a color"),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------)

# Example 2: Color Picker with Default Value
import gradio as gr

def show_color(color):
    return color

demo = gr.Interface(
    fn=show_color,
    inputs=gr.ColorPicker(value="#FF5733", label="Pick a color"),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------)

# Example 3: Color Picker with Dynamic Update
import gradio as gr

def update_color(color):
    return color

with gr.Blocks() as demo:
    color_picker = gr.ColorPicker(label="Pick a color")
    output = gr.ColorPicker(label="Selected Color")

    color_picker.change(fn=update_color, inputs=color_picker, outputs=output)

demo.launch()


# (--------------------------------------------------------------------------------)

# Example 4: Dynamic Text Color Customization
import gradio as gr

def change_text_color(text, color):
    return f"<p style='color: {color};'>{text}</p>"

inputs = [
    gr.Textbox(label="Enter Text"),
    gr.ColorPicker(label="Pick a text color")
]
outputs = gr.HTML(label="Customized Text")

demo = gr.Interface(
    fn=change_text_color,
    inputs=inputs,
    outputs=outputs
)

demo.launch()

# (--------------------------------------------------------------------------------)


# Example 5: Color Picker with Multiple Inputs
# Change the background color of a text box based on the selected color and font size.

import gradio as gr

def change_bg_color(color, font_size):
    return gr.Markdown(f"<div style='background-color: {color}; font-size: {font_size}px;'>This is a colored box</div>")

color_picker = gr.ColorPicker(label="Choose a background color")
font_size_slider = gr.Slider(10, 50, step=1, label="Font Size")
outputs = gr.HTML()

demo = gr.Interface(
    fn=change_bg_color,
    inputs=[color_picker, font_size_slider],
    outputs=outputs
)

demo.launch()

# (--------------------------------------------------------------------------------)

# Example 6: Color Picker with Animated Gradient Background
# Create an animated gradient background using the selected color.

import gradio as gr

def create_gradient(color1, color2):
    gradient_html = f"""
    <div style="
        width: 100%;
        height: 300px;
        background: linear-gradient(45deg, {color1}, {color2});
        animation: gradient 10s ease infinite;
    "></div>
    <style>
    @keyframes gradient {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    </style>
    """
    return gr.HTML(gradient_html)

color_picker1 = gr.ColorPicker(label="Color 1", value="#FF0000")
color_picker2 = gr.ColorPicker(label="Color 2", value="#0000FF")
output = gr.HTML()

demo = gr.Interface(
    fn=create_gradient,
    inputs=[color_picker1, color_picker2],
    outputs=output
)

demo.launch()

# (-----------------------------------------------------------------------------------)


# Example 7: Color Picker with Interactive Text Animation
# Create an animated text effect with the selected color.

import gradio as gr

def create_text_animation(color, text):
    animation_html = f"""
    <div style="
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        animation: text-animation 5s infinite;
    ">{text}</div>
    <style>
    @keyframes text-animation {{
        0% {{ color: {color}; }}
        25% {{ color: white; }}
        50% {{ color: {color}; }}
        75% {{ color: white; }}
        100% {{ color: {color}; }}
    }}
    </style>
    """
    return gr.HTML(animation_html)

color_picker = gr.ColorPicker(label="Text Color", value="#FF0000")
text_input = gr.Textbox(label="Enter Text", value="Hello, Gradio!")
output = gr.HTML()

demo = gr.Interface(
    fn=create_text_animation,
    inputs=[color_picker, text_input],
    outputs=output
)

demo.launch()














