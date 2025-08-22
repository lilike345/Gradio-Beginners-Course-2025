'''

The gradio.Code component in Gradio provides a versatile code editor for both input and output purposes within a Gradio interface. 
It supports various programming languages, allowing users to input or view code in a syntax-highlighted environment. This component 
is particularly useful for applications involving code manipulation, visualization, or sharing.

'''

# Example 1: Basic Code Input

import gradio as gr

def process_code(code):
    return f"Received code:\n{code}"

iface = gr.Interface(
    fn=process_code,
    inputs=gr.Code(language="python"),
    outputs="text"
)
iface.launch()

# (-----------------------------------------------------------------------------------------------------------------------)

# Example 2: Code Output with Syntax Highlighting

import gradio as gr

def generate_code():
    return "def hello_world():\n    print('Hello, world!')"

iface = gr.Interface(
    fn=generate_code,
    inputs=None,
    outputs=gr.Code(language="python")
)
iface.launch()

# (------------------------------------------------------------------------------------------------------------------------)

# Example 3: Interactive Code Editor

import gradio as gr

def update_code(code):
    return code.upper()

iface = gr.Interface(
    fn=update_code,
    inputs=gr.Code(language="python", interactive=True),
    outputs=gr.Code(language="python")
)
iface.launch()

# (-------------------------------------------------------------------------------------------------------------------------)

# Example 4: Code Execution

# An interface that takes a Python code snippet, executes it, and returns the output. Note that this example is for educational purposes and should be used with caution due to security risks.

import gradio as gr

def execute_code(code):
    try:
        # This is a simple way to execute code, but it's not safe for production
        # Consider using a safer method such as a sandboxed environment
        exec(code, globals())
        return "Code executed successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

iface = gr.Interface(
    fn=execute_code,
    inputs=gr.Code(label="Enter Python Code", language="python"),
    outputs=gr.Textbox(label="Output"),
    title="Code Executor",
    description="Enter a Python code snippet, and it will be executed."
)
iface.launch()


# (-------------------------------------------------------------------------------------------------------------)

# Example 5: Code Comparison
#An interface that allows the user to input two code snippets and compares them side by side.

import gradio as gr

def compare_codes(code1, code2):
    return code1, code2

iface = gr.Interface(
    fn=compare_codes,
    inputs=[
        gr.Code(label="Code 1", language="python"),
        gr.Code(label="Code 2", language="python")
    ],
    outputs=[
        gr.Code(label="Code 1", language="python"),
        gr.Code(label="Code 2", language="python")
    ],
    title="Code Comparator",
    description="Enter two Python code snippets to compare them side by side."
)
iface.launch()

# (-------------------------------------------------------------------------------------------------------------)

# Example 6: Code Snippet Generator
# An interface that generates a code snippet based on user input (e.g., a function name and parameters).

import gradio as gr

def generate_code(function_name, parameters):
    params = ", ".join(parameters.split(","))
    code = f"def {function_name}({params}):\n    pass"
    return code

iface = gr.Interface(
    fn=generate_code,
    inputs=[
        gr.Textbox(label="Function Name"),
        gr.Textbox(label="Parameters (comma-separated)")
    ],
    outputs=gr.Code(label="Generated Code", language="python"),
    title="Code Snippet Generator",
    description="Enter a function name and parameters to generate a Python function."
)
iface.launch()

# (------------------------------------------------------------------------------------------------------------)

# Example 7: Code Snippet Library
# An interface that allows the user to select a code snippet from a library and displays it with syntax highlighting.

import gradio as gr

code_library = {
    "Hello World": 'print("Hello, World!")',
    "Sum Function": 'def sum(a, b):\n    return a + b',
    "Factorial Function": 'def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)'
}

def display_code(snippet_name):
    return code_library[snippet_name]

iface = gr.Interface(
    fn=display_code,
    inputs=gr.Dropdown(list(code_library.keys()), label="Select Code Snippet"),
    outputs=gr.Code(label="Code Snippet", language="python"),
    title="Code Snippet Library",
    description="Select a code snippet from the library to display it."
)
iface.launch()