'''
The gradio.Number component in Gradio is used for creating numeric input and output fields. It allows users to enter numbers 
as input or display numbers as output. This component can accept both integers and floats and provides options to set minimum 
and maximum values, precision, and step increments.
'''

# Example 1: Basic Number Input and Output
import gradio as gr

def double_number(value):
    return value * 2

demo = gr.Interface(
    fn=double_number,
    inputs=gr.Number(label="Enter a number"),
    outputs=gr.Number(label="Doubled number"),
)
demo.launch()

# (-------------------------------------------------------------------------------------------)

# Example 2: Number Input with Multiple Inputs

import gradio as gr

def calculate_total_price(quantity, price_per_unit):
    return quantity * price_per_unit

iface = gr.Interface(
    fn=calculate_total_price,
    inputs=[
        gr.Number(label="Quantity", minimum=0, step=1),
        gr.Number(label="Price per unit", minimum=0, step=0.1)
    ],
    outputs=gr.Number(label="Total price")
)
iface.launch()

# (-------------------------------------------------------------------------------------------)

# Example 3: Number Input with Precision
import gradio as gr

def square_number(value):
    return value

demo = gr.Interface(
    fn=square_number,
    inputs=gr.Number(precision=0, label="Enter a number"),
    outputs=gr.Number(precision=0, label="Squared number"),
)
demo.launch()

# Precision to round input/output to. If set to 0, will round to nearest integer and convert type to int. If None, no rounding happens.

# (----------------------------------------------------------------------------------------------)

# Example 4: Number Input with Minimum and Maximum
import gradio as gr

def validate_age(value):
    if value < 0 or value > 120:
        return "Invalid age"
    return f"Age is {value}"

demo = gr.Interface(
    fn=validate_age,
    inputs=gr.Number(minimum=0, maximum=120, label="Enter your age"),
    outputs=gr.Textbox(label="Validation result"),
)
demo.launch()

# (------------------------------------------------------------------------------------------------)

# Example 5: Number Input with Custom CSS
import gradio as gr

def double_number(value):
    return value * 2

demo = gr.Interface(
    fn=double_number,
    inputs=gr.Number(label="Enter a number", elem_classes=["custom-number"]),
    outputs=gr.Number(label="Doubled number", elem_classes=["custom-number"]),
)

demo.css = """
.custom-number {
    background-color: purple;
    border: 2px solid #ccc;
    padding: 30px;
    border-radius: 20px;
}
"""

demo.launch()













