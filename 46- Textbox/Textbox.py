'''
The Textbox component in Gradio is a versatile element used for both input and output purposes. It allows users to 
enter text into a textarea or display text output. This component can be configured in numerous ways to suit different 
use cases, from simple text entry to more complex text manipulation and analysis tasks. The Textbox component supports 
various event listeners that enable you to respond to user interactions
'''

# Example 1: Basic Input and Output

import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(
    fn=greet, 
    inputs=gr.Textbox(label="Enter your name"), 
    outputs=gr.Textbox(label="Greeting")
)
demo.launch()

# (----------------------------------------------------------------------------------------)

# Example 2: Password Input

import gradio as gr

def check_password(password):
    if password == "secret123":
        return "Access granted!"
    else:
        return "Access denied!"

demo = gr.Interface(
    fn=check_password,
    inputs=gr.Textbox(label="Enter password", type="password"),
    outputs=gr.Textbox(label="Result")
)
demo.launch()

# (------------------------------------------------------------------------------------------)

# Example 3: Multiline Text Input

import gradio as gr

def echo_text(text):
    return text

demo = gr.Interface(
    fn=echo_text,
    inputs=gr.Textbox(label="Enter your text", lines=5),
    outputs=gr.Textbox(label="Echoed Text")
)
demo.launch()

# (-------------------------------------------------------------------------------------------)

# Example 4: Placeholder Text

import gradio as gr

def summarize_text(text):
    return f"Summary: {text[:50]}..."

demo = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(label="Enter text to summarize", placeholder="Type your text here..."),
    outputs=gr.Textbox(label="Summary")
)
demo.launch()


# (-------------------------------------------------------------------------------------------)


# Example 5: Event Listener - Change

import gradio as gr

def process_text(text):
    return f"Processed: {text.upper()}"

def on_change(text):
    return f"Text changed to: {text}"

with gr.Blocks() as demo:
    input_textbox = gr.Textbox(label="Enter text")
    processed_textbox = gr.Textbox(label="Processed Text")
    
    input_textbox.change(fn=on_change, inputs=input_textbox, outputs=processed_textbox)
    input_textbox.submit(fn=process_text, inputs=input_textbox, outputs=processed_textbox)

demo.launch()

# (---------------------------------------------------------------------------------------------)


# Example 6: Textbox with Max Length and Autofocus

import gradio as gr

def process_text(text):
    return f"Processed: {text.upper()}"

demo = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="Enter text", max_length=50, autofocus=True),
    outputs=gr.Textbox(label="Processed Text")
)
demo.launch()


# (----------------------------------------------------------------------------------------------)


# Example 7: Textbox with Show Copy Button

import gradio as gr

def process_text(text):
    return f"Processed: {text.upper()}"

demo = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="Enter text", show_copy_button=True),
    outputs=gr.Textbox(label="Processed Text", show_copy_button=True)
)
demo.launch()


# (-----------------------------------------------------------------------------------------------)

# Example 8: Textbox with RTL (Right-to-Left) Text

import gradio as gr

def echo_text(text):
    return text

demo = gr.Interface(
    fn=echo_text,
    inputs=gr.Textbox(label="Enter text", rtl=True),
    outputs=gr.Textbox(label="Echoed Text", rtl=True)
)
demo.launch()

# (------------------------------------------------------------------------------------------------)

# Example 9: Textbox with Text Alignment

import gradio as gr

def echo_text(text):
    return text

demo = gr.Interface(
    fn=echo_text,
    inputs=gr.Textbox(label="Left Aligned Text", text_align="left"),
    outputs=gr.Textbox(label="Right Aligned Text", text_align="right")
)
demo.launch()

# (------------------------------------------------------------------------------------------------)










