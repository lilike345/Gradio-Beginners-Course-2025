'''
The Slider component in Gradio is used to create a slider that allows users to select a value within a specified range. 
This component is particularly useful for settings that require fine-grained control, such as adjusting parameters for 
a machine learning model, setting thresholds, or selecting numeric values in general.
'''

# Example 1: Basic Slider

import gradio as gr

def display_value(value):
    return f"Selected value: {value}"

demo = gr.Interface(
    fn=display_value,
    inputs=gr.Slider(0, 100, value=50, step=1, label="Select a Value"),
    outputs="text"
)

demo.launch()

# (-----------------------------------------------------------------------------------------------)

# Example 2: Slider with Step Size

import gradio as gr

def display_step(value):
    return f"Selected value with step 5: {value}"

demo = gr.Interface(
    fn=display_step,
    inputs=gr.Slider(0, 100, value=0, step=5, label="Select a Value with Step 5"),
    outputs="text"
)

demo.launch()

# (------------------------------------------------------------------------------------------------)

# Example 3: Interactive Slider

import gradio as gr

def display_value(value):
    return f"Selected value: {value}"

demo = gr.Interface(
    fn=display_value,
    inputs=gr.Slider(0, 100, value=50, step=1, label="Non-Interactive Slider", interactive=False),
    outputs="text"
)

demo.launch()

# (-------------------------------------------------------------------------------------------------)

# Example 4: Slider with Hidden Label

import gradio as gr

def display_value(value):
    return f"Selected value: {value}"

demo = gr.Interface(
    fn=display_value,
    inputs=gr.Slider(0, 100, value=50, step=1, label="Hidden Label Slider", show_label=False),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------------------------)

# Example 5: Slider with Information

import gradio as gr

def display_value(value):
    return f"Selected value: {value}"

demo = gr.Interface(
    fn=display_value,
    inputs=gr.Slider(0, 100, value=50, step=1, label="Slider with Info", info="Choose a value between 0 and 100"),
    outputs="text"
)

demo.launch()

# (---------------------------------------------------------------------------------------------------)

# Example 6: Slider in Blocks with Multiple Inputs

import gradio as gr

def combine_inputs(slider_value, text_input):
    return f"Slider Value: {slider_value}, Text Input: {text_input}"

with gr.Blocks() as demo:
    slider = gr.Slider(0, 100, value=50, step=1, label="Slider")
    text_input = gr.Textbox(label="Text Input")
    output_text = gr.Textbox(label="Output")
    gr.Button("Submit").click(fn=combine_inputs, inputs=[slider, text_input], outputs=output_text)

demo.launch()

# (-----------------------------------------------------------------------------------------------------)

# Example 7: Slider with Randomization

import gradio as gr

def display_value(value):
    return f"Selected value: {value}"

demo = gr.Interface(
    fn=display_value,
    inputs=gr.Slider(0, 100, value=50, step=1, label="Random Slider", randomize=True),
    outputs="text"
)

demo.launch()
