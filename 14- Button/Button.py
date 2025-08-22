'''
The Gradio Button component is a versatile UI element used to trigger events in Gradio applications. It can be configured to perform actions such as 
executing functions, updating other components, or navigating to new URLs. The Button component can be used both as an input and an output, although 
its primary use is to trigger .click() events. When used as an input, the button's label (a string) can be passed to a function, and when used as an 
output, the function can set the button's label.
'''

# Example 1: Basic Button Click Event
# This example shows a basic button that triggers a function when clicked, displaying a message.

import gradio as gr

def greet():
    return "Hello, Gradio!"

with gr.Blocks() as demo:
    btn = gr.Button("Greet")
    output = gr.Textbox()
    btn.click(fn=greet, inputs=None, outputs=output)

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 2: Button with Input and Output


import gradio as gr

def echo(text):
    return f"You entered: {text}"

with gr.Blocks() as demo:
    input_text = gr.Textbox(label="Enter Text")
    btn = gr.Button("Button")
    output_text = gr.Textbox(label="Output Text")
    btn.click(fn=echo, inputs=input_text, outputs=output_text)

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 3: Button with Multiple Inputs and Outputs

import gradio as gr

def calculate(a, b):
    return a + b, a - b, a * b, a / b

with gr.Blocks() as demo:
    num1 = gr.Number(label="Number 1")
    num2 = gr.Number(label="Number 2")
    calculate_button = gr.Button("Calculate")
    sum_output = gr.Number(label="Sum")
    diff_output = gr.Number(label="Difference")
    prod_output = gr.Number(label="Product")
    div_output = gr.Number(label="Quotient")
    calculate_button.click(fn=calculate, inputs=[num1, num2], outputs=[sum_output, diff_output, prod_output, div_output])

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 4: Button with Timer
# This example creates a button that triggers a function at regular intervals.

import gradio as gr

def update_counter(counter):
    return counter + 1

with gr.Blocks() as demo:
    counter = gr.Number(value=0)
    btn = gr.Button("Start Counter", every=1)
    btn.click(fn=update_counter, inputs=counter, outputs=counter)

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 5: Button with Timer

import gradio as gr
import time

def update_time():
    return time.strftime("%H:%M:%S", time.localtime())

with gr.Blocks() as demo:
    btn = gr.Button("Refresh Time", every=1.0)
    output = gr.Textbox()
    btn.click(fn=update_time, inputs=[], outputs=output)

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 6: Button with Link
# This example demonstrates a button that navigates to a URL when clicked.

import gradio as gr

def greet():
    return "Hello, World!"

with gr.Blocks() as demo:
    greet_button = gr.Button("Visit Gradio", link="https://gradio.app")
    greet_button.click()

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 7: Button with Variant and Size
# This example shows a button with different variants and sizes.

import gradio as gr

def greet():
    return "Hello, World!"

with gr.Blocks() as demo:
    primary_button = gr.Button("Primary", variant="primary", size="lg")
    secondary_button = gr.Button("Secondary", variant="secondary", size="md")
    stop_button = gr.Button("Stop", variant="stop", size="sm")
    huggingface_button = gr.Button("HuggingFace", variant="huggingface", size="lg")
    primary_button.click()
    secondary_button.click()
    stop_button.click()
    huggingface_button.click()

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Question # 8: Button with Custom CSS

import gradio as gr

def on_button_click():
    return "Button styled with custom CSS clicked!"

with gr.Blocks() as demo:
    button = gr.Button("Click Me", elem_classes=["custom-button"])
    output = gr.Textbox(label="Output")
    button.click(fn=on_button_click, outputs=output)
    demo.css = """
    .custom-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    """

demo.launch()