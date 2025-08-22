'''

The ClearButton component in Gradio is a button that, when clicked, clears the value of a specified component or a list of components. 
This component is particularly useful for resetting user inputs or outputs in a Gradio interface, making it easier for users to start 
fresh without reloading the entire application.

'''

# Example 1: Clearing a Single TextInput

import gradio as gr

def greet(name):
    return f"Hello {name}!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Enter your name")
    output = gr.Textbox(label="Output")
    clear_button = gr.ClearButton(components=[name, output], value="Clear")

    name.submit(greet, inputs=name, outputs=output)
    clear_button.click(greet, inputs=name, outputs=output)

demo.launch()

# (---------------------------------------------------------------------------------------------------)

# Example 2: Clearing Image Input and Output

import gradio as gr

def process_image(img):
    return img

with gr.Blocks() as demo:
    img_input = gr.Image(label="Upload an image")
    img_output = gr.Image(label="Processed image")
    clear_button = gr.ClearButton(components=[img_input, img_output], value="Clear")

    img_input.upload(process_image, inputs=img_input, outputs=img_output)
    clear_button.click(process_image, inputs=img_input, outputs=img_output)

demo.launch()

# (----------------------------------------------------------------------------------------------------)

# Example 3: Clearing Dropdown and Textbox

import gradio as gr

def get_description(animal):
    descriptions = {
        "Dog": "A domesticated carnivorous mammal.",
        "Cat": "A small, typically furry carnivorous mammal.",
        "Bird": "A warm-blooded vertebrate with feathers, beak, and laying hard-shelled eggs."
    }
    return descriptions.get(animal, "Unknown animal")

with gr.Blocks() as demo:
    animal_dropdown = gr.Dropdown(["Dog", "Cat", "Bird"], label="Select an animal")
    description_textbox = gr.Textbox(label="Description")
    clear_button = gr.ClearButton(components=[animal_dropdown, description_textbox], value="Clear")

    animal_dropdown.change(get_description, inputs=animal_dropdown, outputs=description_textbox)
    clear_button.click(get_description, inputs=animal_dropdown, outputs=description_textbox)

demo.launch() 

# (----------------------------------------------------------------------------------------------------------------)

# Example 4: Clearing Radio and Textbox

import gradio as gr

def get_response(question):
    responses = {
        "What is the capital of France?": "The capital of France is Paris.",
        "What is the largest planet?": "The largest planet is Jupiter."
    }
    return responses.get(question, "Unknown question")

with gr.Blocks() as demo:
    question_radio = gr.Radio(["What is the capital of France?", "What is the largest planet?"], label="Select a question")
    response_textbox = gr.Textbox(label="Response")
    clear_button = gr.ClearButton(components=[question_radio, response_textbox], value="Clear")

    question_radio.change(get_response, inputs=question_radio, outputs=response_textbox)
    clear_button.click(get_response, inputs=question_radio, outputs=response_textbox)

demo.launch()

# (-------------------------------------------------------------------------------------------------------------------)


# Example 5: Clearing Checkbox and Textbox

import gradio as gr

def summarize_features(features):
    return "Selected features: " + ", ".join(features)

with gr.Blocks() as demo:
    features_checkbox = gr.CheckboxGroup(["Fast", "Efficient", "Reliable"], label="Select features")
    summary_textbox = gr.Textbox(label="Summary")
    clear_button = gr.ClearButton(components=[features_checkbox, summary_textbox], value="Clear")

    features_checkbox.change(summarize_features, inputs=features_checkbox, outputs=summary_textbox)
    clear_button.click(summarize_features, inputs=features_checkbox, outputs=summary_textbox)

demo.launch()


# (---------------------------------------------------------------------------------------------------------------)


# Example 6: Clearing Slider and Textbox

import gradio as gr

def describe_age(age):
    return f"You are {age} years old."

with gr.Blocks() as demo:
    age_slider = gr.Slider(0, 100, step=1, label="Age")
    description_textbox = gr.Textbox(label="Description")
    clear_button = gr.ClearButton(components=[age_slider, description_textbox], value="Clear")

    age_slider.change(describe_age, inputs=age_slider, outputs=description_textbox)
    clear_button.click(describe_age, inputs=age_slider, outputs=description_textbox)

demo.launch()


# (----------------------------------------------------------------------------------------------------------------)


# Example 7: Clearing RadioGroup and Textbox

import gradio as gr

def get_answer(question):
    answers = {
        "What is 2 + 2?": "2 + 2 = 4",
        "What is 5 * 5?": "5 * 5 = 25"
    }
    return answers.get(question, "Unknown question")

with gr.Blocks() as demo:
    question_radiogroup = gr.Radio(["What is 2 + 2?", "What is 5 * 5?"], label="Select a question")
    answer_textbox = gr.Textbox(label="Answer")
    clear_button = gr.ClearButton(components=[question_radiogroup, answer_textbox], value="Clear")

    question_radiogroup.change(get_answer, inputs=question_radiogroup, outputs=answer_textbox)
    clear_button.click(get_answer, inputs=question_radiogroup, outputs=answer_textbox)

demo.launch()




