'''
Gradio's Error component allows developers to display custom error messages to users in a modal format. This component is 
particularly useful for handling exceptions and providing user-friendly feedback. The Error class can be raised anywhere 
in the code, and it will trigger a modal to appear with the specified message.
'''


# Example 1: Basic Error Message
import gradio as gr

def greet(name):
    if not name:
        raise gr.Error("Name cannot be empty!")
    return f"Hello, {name}!"

demo = gr.Interface(greet, "text", "text")
demo.launch()

# (--------------------------------------------------------------------------------)

# Example 2: Error with Duration
import gradio as gr

def check_age(age):
    if age < 18:
        raise gr.Error("You must be at least 18 years old!", duration=5)
    return "Welcome!"

demo = gr.Interface(check_age, "number", "text")
demo.launch()

# (--------------------------------------------------------------------------------)

# Example 3: Error with Custom Title
import gradio as gr

def validate_email(email):
    if "@" not in email:
        raise gr.Error("Invalid email address!", title="Email Error")
    return "Email validated!"

demo = gr.Interface(validate_email, "text", "text")
demo.launch()

# (--------------------------------------------------------------------------------)

# Example 4: Error in a Calculator
import gradio as gr

def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!", duration=3)
        return num1 / num2

demo = gr.Interface(
    calculator,
    [
        "number",
        gr.Radio(["add", "subtract", "multiply", "divide"]),
        "number"
    ],
    "number",
    examples=[
        [45, "add", 3],
        [3.14, "divide", 2],
        [144, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="Toy Calculator",
    description="Here's a sample toy calculator.",
)

demo.launch()
# (--------------------------------------------------------------------------------)

# Example 5: Error in Image Upload
import gradio as gr

def process_image(image):
    if image.shape[0] > 1000 or image.shape[1] > 1000:
        raise gr.Error("Image too large! Please upload a smaller image.", duration=5)
    return image

demo = gr.Interface(process_image, "image", "image")
demo.launch()

# (---------------------------------------------------------------------------------)

# Example 6: Error in Text Classification
import gradio as gr

def classify_text(text):
    if len(text) < 10:
        raise gr.Error("Text too short! Please enter more content.", duration=3)
    return {"positive": 0.9, "negative": 0.1}

demo = gr.Interface(classify_text, "text", gr.Label(num_top_classes=2))
demo.launch()

# (---------------------------------------------------------------------------------)

# Example 7: Error in File Upload
import gradio as gr

def process_file(file):
    if file.name.split(".")[-1] != "txt":
        raise gr.Error("Only .txt files are allowed!", duration=3)
    return "File processed successfully!"

demo = gr.Interface(process_file, "file", "text")
demo.launch()

# (---------------------------------------------------------------------------------)

# Example 8: Error in Multiple Inputs
import gradio as gr

def validate_inputs(name, age, email):
    if not name:
        raise gr.Error("Name cannot be empty!", duration=3)
    if age < 18:
        raise gr.Error("You must be at least 18 years old!", duration=3)
    if "@" not in email:
        raise gr.Error("Invalid email address!", duration=3)
    return "All inputs are valid!"

demo = gr.Interface(
    validate_inputs,
    [
        "text",
        "number",
        "text"
    ],
    "text",
    title="Input Validation",
    description="Validate your inputs before submission."
)

demo.launch()