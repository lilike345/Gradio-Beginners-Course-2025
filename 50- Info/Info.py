'''
The gradio.Info component in Gradio allows you to display informational messages to users in a modal dialog. This is 
particularly useful for providing feedback, instructions, or additional context during the interaction with your Gradio 
demo. The modal appears with a gray background and a default title "Info." The message can be customized, and you can 
specify how long the modal should remain visible.
'''

# Example 1. Basic Info Message
import gradio as gr

def show_info():
    gr.Info("This is a basic info message.")
    return "Message Shown"

with gr.Blocks() as demo:
    gr.Markdown("Click the button to show an info message.")
    btn = gr.Button("Show Info")
    btn.click(show_info, None, None)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 2: Info Message with Custom Duration
import gradio as gr

def show_info():
    gr.Info("This message will disappear in 10 seconds.", duration=10)
    return "Check the info modal!"

with gr.Blocks() as demo:
    gr.Markdown("Click the button to see a timed info message.")
    btn = gr.Button("Show Timed Info")
    output = gr.Textbox(label="Output")
    btn.click(fn=show_info, inputs=None, outputs=output)

demo.queue().launch()
# (-----------------------------------------------------------------------------------------)

# Example 3: Info Message with Custom Title
import gradio as gr

def show_info():
    gr.Info("This message has a custom title.", title="Custom Title")
    return "Check the info modal!"

with gr.Blocks() as demo:
    gr.Markdown("Click the button to see an info message with a custom title.")
    btn = gr.Button("Show Custom Title Info")
    output = gr.Textbox(label="Output")
    btn.click(fn=show_info, inputs=None, outputs=output)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 4: Info Message Triggered by Multiple Events
import gradio as gr

def info_fn():
    gr.Info("This is an info message triggered by multiple events.")

with gr.Blocks() as demo:
    gr.Markdown("Click either button to see an info message.")
    btn1 = gr.Button("Button 1")
    btn2 = gr.Button("Button 2")
    btn1.click(info_fn, None, None)
    btn2.click(info_fn, None, None)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 5: Info Message with Dynamic Content
import gradio as gr

def show_info(name):
    gr.Info(f"Hello, {name}! Welcome to the demo.")
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    gr.Markdown("Enter your name and click the button to see a personalized info message.")
    name_input = gr.Textbox(label="Your Name")
    btn = gr.Button("Show Personalized Info")
    output = gr.Textbox(label="Output")
    btn.click(fn=show_info, inputs=name_input, outputs=output)

demo.queue().launch()

# (-----------------------------------------------------------------------------------------)

# Example 6: Chained Events with Info Message
import gradio as gr

def first_event():
    gr.Info("First event triggered.")
    return "First event triggered"

def second_event():
    gr.Info("Second event triggered.")
    return "Second event triggered"

with gr.Blocks() as demo:
    gr.Markdown("Click the button to trigger two events with info messages.")
    btn = gr.Button("Trigger Events")
    output1 = gr.Textbox(label="Output 1")
    output2 = gr.Textbox(label="Output 2")
    btn.click(fn=first_event, inputs=None, outputs=output1).then(fn=second_event, inputs=None, outputs=output2)

demo.queue().launch()

# (-------------------------------------------------------------------------------------------)

# Example 7: Info Message with Conditional Logic
import gradio as gr

def check_number(num):
    if num > 10:
        gr.Info("Number is greater than 10.")
    else:
        gr.Info("Number is less than or equal to 10.")
    return f"You entered: {num}"

with gr.Blocks() as demo:
    gr.Markdown("Enter a number and click the button to see an info message based on the condition.")
    num_input = gr.Number(label="Enter Number")
    btn = gr.Button("Check Number")
    output = gr.Textbox(label="Output")
    btn.click(fn=check_number, inputs=num_input, outputs=output)

demo.queue().launch()

# (---------------------------------------------------------------------------------------------)

# Example 8: Info Message with Multiple Outputs
import gradio as gr

def process_data(data):
    gr.Info("Data processing complete.")
    return data.upper(), data.lower()

with gr.Blocks() as demo:
    gr.Markdown("Enter some text and click the button to see an info message and processed outputs.")
    text_input = gr.Textbox(label="Enter Text")
    btn = gr.Button("Process Data")
    output1 = gr.Textbox(label="Uppercase")
    output2 = gr.Textbox(label="Lowercase")
    btn.click(fn=process_data, inputs=text_input, outputs=[output1, output2])

demo.queue().launch()