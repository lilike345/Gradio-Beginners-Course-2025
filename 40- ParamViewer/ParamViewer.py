'''
The ParamViewer component in Gradio is designed to display an interactive table of parameters and their descriptions, 
along with default values. It supports syntax highlighting and is particularly useful for documenting and displaying 
the parameters of other components, especially in the context of custom components in the Gradio Custom Component Gallery.
'''

# Example 1. Documenting a Custom Function's Parameters
import gradio as gr

def my_custom_function(param1, param2):
    return param1 + param2

param_info = {
    "param1": {"type": "int", "description": "First number", "default": 0},
    "param2": {"type": "int", "description": "Second number", "default": 0}
}

with gr.Blocks() as demo:
    gr.Markdown("## My Custom Function")
    gr.ParamViewer(param_info)

demo.launch()

# (-------------------------------------------------------------------------------------)

#Example 2: Parameters for a Complex Function
import gradio as gr

def complex_function(param1: list, param2: dict, param3: tuple, param4: set):
    return f"Param1: {param1}, Param2: {param2}, Param3: {param3}, Param4: {param4}"

with gr.Blocks() as demo:
    gr.Markdown("### Parameters for `complex_function`")
    gr.ParamViewer({
        "param1": {"type": "list", "description": "A list parameter", "default": "[]"},
        "param2": {"type": "dict", "description": "A dictionary parameter", "default": "{}"},
        "param3": {"type": "tuple", "description": "A tuple parameter", "default": "()"},
        "param4": {"type": "set", "description": "A set parameter", "default": "set()"},
    })

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 3. Documenting API Parameters
import gradio as gr

api_params = {
    "user_id": {"type": "str", "description": "User ID", "default": "user123"},
    "token": {"type": "str", "description": "API token", "default": "abc123"},
    "query": {"type": "str", "description": "Search query", "default": ""}
}

with gr.Blocks() as demo:
    gr.Markdown("## API Parameters")
    gr.ParamViewer(api_params)

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 4: Basic Usage with Python Parameters
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("### Parameters for the `round()` function in Python")
    gr.ParamViewer({
        "number": {"type": "int | float", "description": "The number to round", "default": "None"},
        "ndigits": {"type": "int", "description": "The number of digits to round to", "default": "0"}
    })

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 5: Using TypeScript Parameters
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("### Parameters for a TypeScript Function")
    gr.ParamViewer({
        "param1": {"type": "number", "description": "A number parameter", "default": "0"},
        "param2": {"type": "string", "description": "A string parameter", "default": "''"},
        "param3": {"type": "boolean", "description": "A boolean parameter", "default": "false"}
    }, language='typescript')

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 6: Adding a Header
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("### Parameters with Custom Header")
    gr.ParamViewer({
        "param1": {"type": "int", "description": "An integer parameter", "default": "None"},
        "param2": {"type": "str", "description": "A string parameter", "default": "None"},
    }, header="Custom Header")

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 7: Using Event Listeners to Update Parameters
import gradio as gr

def update_params(param_name, param_type, param_desc, param_default):
    return {
        param_name: {"type": param_type, "description": param_desc, "default": param_default}
    }

with gr.Blocks() as demo:
    gr.Markdown("### Dynamic Parameters with Event Listeners")
    param_viewer = gr.ParamViewer({
        "param1": {"type": "int", "description": "An integer parameter", "default": "None"},
    })

    param_name = gr.Textbox(label="Parameter Name")
    param_type = gr.Textbox(label="Parameter Type")
    param_desc = gr.Textbox(label="Parameter Description")
    param_default = gr.Textbox(label="Parameter Default")

    update_button = gr.Button("Update Parameters")
    update_button.click(
        fn=update_params,
        inputs=[param_name, param_type, param_desc, param_default],
        outputs=param_viewer
    )

demo.launch()

# (-------------------------------------------------------------------------------------)

