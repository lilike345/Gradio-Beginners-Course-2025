'''
Gradio's JSON component is a versatile tool for displaying JSON data in a user-friendly and visually appealing manner. 
This component is typically used to display the output of a function, such as a dictionary or list that represents JSON 
data. Unlike other input components, JSON is not designed to accept user input directly, making it more suitable for output purposes.
'''

# Example 1: Displaying a Simple Dictionary

import gradio as gr

def display_dict():
    return {"Key 1": "Value 1", "Key 2": "Value 2"}

demo = gr.Interface(display_dict, inputs=None, outputs="json")
demo.launch()

# (----------------------------------------------------------------------)

# Example 2: Displaying a Nested Dictionary

import gradio as gr

def nested_dict():
    return {
        "Key 1": "Value 1",
        "Key 2": {
            "Key 3": "Value 2",
            "Key 4": "Value 3"
        }
    }

demo = gr.Interface(nested_dict, inputs=None, outputs="json")
demo.launch()

# (-----------------------------------------------------------------------)

#Example 3: Displaying a List

import gradio as gr

def list_display():
    return ["Item 1", "Item 2", "Item 3"]

demo = gr.Interface(list_display, inputs=None, outputs="json")
demo.launch()

# (-------------------------------------------------------------------------)

# Example 4: Displaying a List of Dictionaries

import gradio as gr

def list_of_dicts():
    return [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]

demo = gr.Interface(list_of_dicts, inputs=None, outputs="json")
demo.launch()

# (--------------------------------------------------------------------------)


# Example 5: Displaying a Dictionary with Mixed Data Types

import gradio as gr

def mixed_data_types():
    return {
        "string": "Hello",
        "integer": 123,
        "float": 123.456,
        "boolean": True,
        "null": None
    }

demo = gr.Interface(mixed_data_types, inputs=None, outputs="json")
demo.launch()

# (---------------------------------------------------------------------------)

# Example 6: Displaying JSON from a File

import gradio as gr
import json

def json_from_file(file_path):
    with open(file_path.name, 'r') as f:
        return json.load(f)

demo = gr.Interface(json_from_file, inputs="file", outputs="json")
demo.launch()


# (---------------------------------------------------------------------------)

# Example 7: Displaying JSON from a URL

import gradio as gr
import requests

def json_from_url(url):
    response = requests.get(url)
    return response.json()

demo = gr.Interface(json_from_url, inputs="text", outputs="json")
demo.launch()

# Example link: https://jsonplaceholder.typicode.com/posts

# (------------------------------------------------------------------------------)

# Example 8: Displaying JSON with User Input

import gradio as gr

def process_input(user_input):
    return {"user_input": user_input}

demo = gr.Interface(process_input, inputs="text", outputs="json")
demo.launch()

