'''
The gradio.Warning component in Gradio allows you to display custom warning messages to users in a modal format. This is useful 
for informing users about potential issues or errors in their interactions with the application. The modal is yellow by default 
and has a heading "Warning." To use the gradio.Warning component, you need to ensure that the queue is enabled in your Gradio application.
'''

# Example 1: Basic Warning
import gradio as gr

def show_warning():
    gr.Warning("This is a basic warning ⛔️!", duration=5)
    return "Warning shown!"

with gr.Blocks() as demo:
    btn = gr.Button("Show Warning")
    output = gr.Textbox()
    btn.click(show_warning, inputs=None, outputs=output)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 2: Warning with Custom Title
import gradio as gr

def custom_title_warning():
    gr.Warning("This is a warning with a custom title ⛔️!", title="Attention!", duration=5)
    return "Custom title warning shown!"

with gr.Blocks() as demo:
    btn = gr.Button("Show Custom Title Warning")
    output = gr.Textbox()
    btn.click(custom_title_warning, inputs=None, outputs=output)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 3: Warning with Long Duration
import gradio as gr

def long_duration_warning():
    gr.Warning("This warning will stay for 10 seconds ⛔️!", duration=10)
    return "Long duration warning shown!"

with gr.Blocks() as demo:
    btn = gr.Button("Show Long Duration Warning")
    output = gr.Textbox()
    btn.click(long_duration_warning, inputs=None, outputs=output)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 4: Warning with Permanent Display
import gradio as gr

def permanent_warning():
    gr.Warning("This warning will stay until dismissed ⛔️!", duration=None)
    return "Permanent warning shown!"

with gr.Blocks() as demo:
    btn = gr.Button("Show Permanent Warning")
    output = gr.Textbox()
    btn.click(permanent_warning, inputs=None, outputs=output)

demo.queue().launch()

# (------------------------------------------------------------------------------------------)

# Example 5: Warning Triggered by Input Validation
import gradio as gr

def validate_input(text):
    if len(text) < 5:
        gr.Warning("Input must be at least 5 characters long ⛔️!", duration=5)
        return "Invalid input"
    return "Valid input"

with gr.Blocks() as demo:
    input_text = gr.Textbox(label="Enter text")
    btn = gr.Button("Validate Input")
    output = gr.Textbox()
    btn.click(validate_input, inputs=input_text, outputs=output)

demo.queue().launch()

# (------------------------------------------------------------------------------------------)

# Example 6: Warning Triggered by Button Click
import gradio as gr

def show_warning_on_click():
    gr.Warning("Button was clicked ⛔️!", duration=5)
    return "Button clicked!"

with gr.Blocks() as demo:
    btn = gr.Button("Click Me")
    output = gr.Textbox()
    btn.click(show_warning_on_click, inputs=None, outputs=output)

demo.queue().launch()

# (------------------------------------------------------------------------------------------)

# Example 7: Warning with Conditional Display
import gradio as gr

def conditional_warning(condition):
    if condition:
        gr.Warning("Condition met ⛔️!", duration=5)
        return "Condition met"
    return "Condition not met"

with gr.Blocks() as demo:
    checkbox = gr.Checkbox(label="Check to trigger warning")
    btn = gr.Button("Check Condition")
    output = gr.Textbox()
    btn.click(conditional_warning, inputs=checkbox, outputs=output)

demo.queue().launch()