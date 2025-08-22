'''
The FileExplorer component in Gradio is a versatile tool that allows users to browse files and directories on the server 
where the Gradio app is hosted. This component can be used as both an input and an output, making it highly useful for 
applications that require file manipulation or selection.
'''

# 1. Basic File Selection
# A simple example where users can select a single file.

import gradio as gr

def predict(value):
    return f"You selected: {value}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.FileExplorer(root_dir=".", file_count="single"),
    outputs="text"
)
iface.launch()

# (---------------------------------------------------------------------------------)

# 2. Multiple File Selection
# Allow users to select multiple files.

import gradio as gr

def predict(values):
    return f"You selected: {values}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.FileExplorer(root_dir=".", file_count="multiple"),
    outputs="text"
)
iface.launch()

# (----------------------------------------------------------------------------------)

# 3. Filtering Files with glob
# Only show .txt files in the explorer.

import gradio as gr

def predict(value):
    return f"You selected: {value}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.FileExplorer(root_dir=".", glob="*.txt", file_count="single"),
    outputs="text"
)
iface.launch()


# (-----------------------------------------------------------------------------------)

# 4. Ignoring Certain Files or Directories
# Exclude certain files or directories from the explorer using ignore_glob.

import gradio as gr

def predict(value):
    return f"You selected: {value}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.FileExplorer(root_dir=".", ignore_glob="*.txt", file_count="multiple"),
    outputs="text"
)
iface.launch()

# (------------------------------------------------------------------------------------)


# 5. Customizing Appearance
# Change the label and visibility of the FileExplorer.

import gradio as gr

def predict(value):
    return f"You selected: {value}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.FileExplorer(root_dir=".", file_count="single", label="Choose a File", visible=True),
    outputs="text"
)
iface.launch()


# (------------------------------------------------------------------------------------)


# 6. Using a Callback for Initial Value
# Set an initial value using a callable.

import gradio as gr

def initial_value():
    return "data/sample.txt"

def predict(value):
    return f"You selected: {value}"

iface = gr.Interface(
    fn=predict,
    inputs=gr.FileExplorer(root_dir=".", file_count="single", value=initial_value),
    outputs="text"
)
iface.launch()

# (-------------------------------------------------------------------------------------)

 




















































