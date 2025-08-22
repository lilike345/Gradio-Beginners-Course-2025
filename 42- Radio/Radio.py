'''
The Gradio Radio component is a user interface element that presents a set of options (radio buttons) from which 
the user can select only one. This component is commonly used in scenarios where a single choice is required from 
a predefined set of options. For example, selecting a language preference, choosing a category, or picking a setting.
'''

# Example 1: Basic Radio Button Group
import gradio as gr

def greet(name):
    return f"Hello {name}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Radio(["Alice", "Bob", "Charlie"], label="Choose a name"),
    outputs="text"
)

demo.launch()

# (-------------------------------------------------------------------------------------------------)

# Example 2: Radio Button Group with Default Value

import gradio as gr

def greet(name):
    return f"Hello {name}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Radio(["Alice", "Bob", "Charlie"], value="Bob", label="Choose a name"),
    outputs="text"
)

demo.launch()

# (--------------------------------------------------------------------------------------------------)


# Example 3: Radio Button Group with Numeric Choices
import gradio as gr

def describe_age(age):
    if age == 18:
        return "You are an adult!"
    elif age == 17:
        return "You are almost an adult!"
    else:
        return "You are a minor."

demo = gr.Interface(
    fn=describe_age,
    inputs=gr.Radio([16, 17, 18], label="Select your age"),
    outputs="text"
)

demo.launch()

# (---------------------------------------------------------------------------------------------------)

# Example 4: Radio Button Group with Type Index
import gradio as gr

def describe_choice(index):
    options = ["Red", "Green", "Blue"]
    return f"You selected: {options[index]}"

demo = gr.Interface(
    fn=describe_choice,
    inputs=gr.Radio(["Red", "Green", "Blue"], type="index", label="Choose a color"),
    outputs="text"
)

demo.launch()

# (----------------------------------------------------------------------------------------------------)

# Example 5: Radio Button Group with Info Text
import gradio as gr

def describe_role(role):
    if role == "Admin":
        return "You have full access."
    elif role == "User":
        return "You have limited access."
    else:
        return "You have no access."

demo = gr.Interface(
    fn=describe_role,
    inputs=gr.Radio(["Admin", "User", "Guest"], info="Select your role", label="Choose your role"),
    outputs="text"
)

demo.launch()

# (-------------------------------------------------------------------------------------------------------)

# Example 6: Radio Button Group with Event Listener on Change
import gradio as gr

def on_change(value):
    return f"Value changed to: {value}"

demo = gr.Interface(
    fn=on_change,
    inputs=gr.Radio(["Option 1", "Option 2", "Option 3"], label="Choose an option"),
    outputs="text"
)

demo.launch()

# (---------------------------------------------------------------------------------------------------------)

# Example 7: Radio Button Group with Multiple Components
import gradio as gr

def describe_pet(pet, activity):
    return f"The {pet} {activity}."

demo = gr.Interface(
    fn=describe_pet,
    inputs=[
        gr.Radio(["Dog", "Cat", "Bird"], label="Choose a pet"),
        gr.Radio(["runs", "flies", "barks"], label="Choose an activity")
    ],
    outputs="text"
)

demo.launch()
