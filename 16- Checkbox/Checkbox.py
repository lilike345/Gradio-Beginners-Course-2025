'''
The Checkbox component in Gradio is a simple yet powerful UI element used to capture a boolean input from users. 
It allows users to toggle between two states: checked (True) and unchecked (False). This component can be used as 
both an input to pass a boolean value to a function and as an output to display a boolean state. It integrates 
seamlessly with other Gradio components to build interactive web interfaces for various applications, such as 
configuration settings, feature toggles, or conditional logic in machine learning models.

'''

# Example 1: Basic Checkbox Usage
# This example demonstrates a simple checkbox that toggles between "On" and "Off" states.

import gradio as gr

def toggle_state(value):
    return f"Checkbox is {'checked' if value else 'unchecked'}"

demo = gr.Interface(
    toggle_state,
    gr.Checkbox(label="Toggle Me"),
    "text"
)

demo.launch()

# (-----------------------------------------------------------------------------------------)

# Example 2: Checkbox with Default Value
# This example initializes the checkbox with a default value of True.

import gradio as gr

def toggle_state(value):
    return f"Checkbox is {'checked' if value else 'unchecked'}"

demo = gr.Interface(
    toggle_state,
    gr.Checkbox(value=True, label="Toggle Me"),
    "text"
)

demo.launch()

# (-------------------------------------------------------------------------------------------)

# Example 3: Checkbox with Label and Info
# This example includes a label and additional information about the checkbox.

import gradio as gr

def toggle_state(value):
    return f"Checkbox is {'checked' if value else 'unchecked'}"

demo = gr.Interface(
    toggle_state,
    gr.Checkbox(label="Toggle Me", info="Click to toggle the checkbox state."),
    "text"
)

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 4: Checkbox with Conditional Logic
# This example applies conditional logic based on the checkbox state.


import gradio as gr

def conditional_response(value, text):
    if value:
        return f"You entered: {text}"
    else:
        return "Checkbox is unchecked. Please check it to see your input."

demo = gr.Interface(
    conditional_response,
    [gr.Checkbox(label="Enable Input"), gr.Textbox(label="Enter Text")],
    "text"
)

demo.launch()

# (----------------------------------------------------------------------------------------------)

# Example 5: Checkbox with Multiple Inputs
# This example combines a checkbox with other input components.

import gradio as gr

def process_data(name, age, subscribe):
    if subscribe:
        return f"Hello {name}, you are {age} years old and have subscribed to our newsletter."
    else:
        return f"Hello {name}, you are {age} years old but have not subscribed to our newsletter."

demo = gr.Interface(
    process_data,
    [gr.Textbox(label="Name"), gr.Slider(0, 100, label="Age"), gr.Checkbox(label="Subscribe to Newsletter")],
    "text"
)

demo.launch()

# (----------------------------------------------------------------------------------------------)

# Example 6: Checkbox with Multiple Outputs
# This example demonstrates using a checkbox to control multiple output components.

import gradio as gr

def toggle_output(value):
    if value:
        return "Checkbox is checked", "Output 2: Enabled"
    else:
        return "Checkbox is unchecked", "Output 2: Disabled"

demo = gr.Interface(
    toggle_output,
    gr.Checkbox(label="Toggle Me"),
    ["text", "text"]
)

demo.launch()

# (-----------------------------------------------------------------------------------------------)

# Example 7: Conditional Form Submission

import gradio as gr

def submit_form(name, age, terms_accepted):
    if not terms_accepted:
        return "Please accept the terms and conditions."
    return f"Hello, {name}! You are {age} years old and have accepted the terms."

with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Name")
    age_input = gr.Number(label="Age", minimum=0, maximum=120, value=18)
    terms_checkbox = gr.Checkbox(label="Accept Terms and Conditions", value=False)
    submit_button = gr.Button("Submit")
    output_text = gr.Textbox()

    submit_button.click(fn=submit_form, inputs=[name_input, age_input, terms_checkbox], outputs=output_text)

demo.launch()












































