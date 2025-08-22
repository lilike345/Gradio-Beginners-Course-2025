'''
The Dropdown component in Gradio is a versatile input/output component that allows users to select a single or multiple 
items from a predefined list of choices. It can be used to create dropdown menus for user inputs or to display selected 
options as outputs. The Dropdown component supports various parameters to customize its behavior, such as enabling multi-selection, 
allowing custom values, and setting maximum choices.
'''

# Example 1: Basic Dropdown with Single Selection
# This example demonstrates a simple dropdown with a single selection.

import gradio as gr

def greet(name):
    return f"Hello {name}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Dropdown(choices=["Alice", "Bob", "Charlie"], label="Choose a name"),
    outputs="text"
)

demo.launch()


# (-------------------------------------------------------------------------------------)

# Example 2: Dropdown with Multiple Selections
# This example shows a dropdown where users can select multiple names.

import gradio as gr

def greet(names):
    return f"Hello {' and '.join(names)}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Dropdown(choices=["Alice", "Bob", "Charlie"], multiselect=True, label="Choose names"),
    outputs="text"
)

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 3: Dropdown with Custom Value Allowed
# This example allows users to input a custom value if it's not in the list of choices.

import gradio as gr

def greet(name):
    return f"Hello {name}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Dropdown(choices=["Alice", "Bob", "Charlie"], allow_custom_value=True, label="Choose a name"),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------------)

# Example 4: Dropdown with Index Value
# This example returns the index of the selected choice instead of the value.

import gradio as gr

def greet(index):
    choices = ["Alice", "Bob", "Charlie"]
    return f"You selected {choices[index]}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Dropdown(choices=["Alice", "Bob", "Charlie"], type="index", label="Choose a name"),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------------)

# Example 5: Dropdown with Max Choices
# This example limits the number of choices a user can select.

import gradio as gr

def greet(names):
    return f"Hello {' and '.join(names)}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Dropdown(choices=["Alice", "Bob", "Charlie"], multiselect=True, max_choices=2, label="Choose names"),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------------)

# Example 6: Dropdown with Custom Values and Indices
# This example demonstrates how to use tuples for choices, allowing custom labels and values.

import gradio as gr

def greet(value):
    return f"You selected {value}"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Dropdown(choices=[("A", 1), ("B", 2), ("C", 3)], label="Choose a value"),
    outputs="text"
)

demo.launch()

# (---------------------------------------------------------------------------------------)

#Example 7: Dropdown with Conditional Visibility
# This example shows how to conditionally display a dropdown based on another input.

import gradio as gr

def toggle_visibility(show):
    return gr.update(visible=show)

with gr.Blocks() as demo:
    show_dropdown = gr.Checkbox(label="Show Dropdown")
    dropdown = gr.Dropdown(choices=["Option 1", "Option 2", "Option 3"], visible=False, label="Choose an option")
    output = gr.Textbox(label="Output")
    
    show_dropdown.change(toggle_visibility, inputs=show_dropdown, outputs=dropdown)
    
    dropdown.change(lambda x: f"You selected {x}", inputs=dropdown, outputs=output)

demo.launch()

























