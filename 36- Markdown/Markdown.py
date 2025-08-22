'''
The Markdown component in Gradio is used to render Markdown-formatted text, including LaTeX equations enclosed in dollar signs. 
This component is primarily an output component, meaning it is used to display information to the user rather than accept input. 
However, it can also be used as an input component, though this is less common.
'''

# Example 1: Basic Markdown Display

import gradio as gr

def main():
    return """
    # Welcome to Gradio!
    This is a simple Markdown example.
    """

with gr.Blocks() as demo:
    gr.Markdown("""
    # Gradio Markdown Component
    This component is used to render Markdown text.
    """)
    output = gr.Markdown()
    gr.Button("Show Message").click(main, None, output)

demo.launch()

# (-----------------------------------------------------------------------------------------------------------)

# Example 2: Dynamic Markdown Content

import gradio as gr

def update_markdown(name):
    if not name.strip():
        return "### Please enter your name to see a personalized message."
    return f"## 👋 Hello, **{name}**!\nWelcome to this interactive Markdown demo."

# Creating the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 📝 Dynamic Markdown Example\nEnter your name below to see the magic! 🎩✨")

    # Input textbox with a default placeholder
    inp = gr.Textbox(label="Enter your name", placeholder="Type your name here...")

    # Markdown output area
    output = gr.Markdown("### Your greeting will appear here...")

    # Add an event listener to update the Markdown dynamically
    inp.change(fn=update_markdown, inputs=inp, outputs=output)

    # A button to clear the input and reset the output
    def clear():
        return "", "### Your greeting will appear here..."
    
    clear_btn = gr.Button("Clear Input")
    clear_btn.click(fn=clear, inputs=[], outputs=[inp, output])

# Launch the application
demo.launch()

# (------------------------------------------------------------------------------------------------------------)

# Example 3: Rendering LaTeX Equations

import gradio as gr

def get_equation():
    return """
    ## Einstein's Mass-Energy Equivalence Formula
    $E = mc^2$
    """

with gr.Blocks() as demo:
    output = gr.Markdown()
    gr.Button("Show Equation").click(get_equation, None, output)

demo.launch()

# (-------------------------------------------------------------------------------------------------------------)

# Example 4: Markdown with Images

import gradio as gr

def get_image_markdown():
    return """
    ## Image Example
    ![Gradio Logo](https://cdn.pixabay.com/photo/2023/11/17/01/50/pine-8393456_1280.jpg)
    """

with gr.Blocks() as demo:
    output = gr.Markdown()
    gr.Button("Show Image").click(get_image_markdown, None, output)

demo.launch()

# (-------------------------------------------------------------------------------------------------------------)

# Example 5: Markdown with Links

import gradio as gr

def get_links():
    return """
    ## Useful Links
    - [Gradio Documentation](https://gradio.app/docs/)
    - [Gradio GitHub](https://github.com/gradio-app/gradio)
    """

with gr.Blocks() as demo:
    output = gr.Markdown()
    gr.Button("Show Links").click(get_links, None, output)

demo.launch()

# (---------------------------------------------------------------------------------------------------------------)

# Example 6: Markdown with Code Blocks

import gradio as gr

def get_code():
    return """
    ## Python Code Example
    ```python
    def hello_world():
        print("Hello, World!")
    ```
    """

with gr.Blocks() as demo:
    output = gr.Markdown()
    gr.Button("Show Code").click(get_code, None, output)

demo.launch()

# (---------------------------------------------------------------------------------------------------------------)

# Example 7: Markdown with Lists

import gradio as gr

def get_list():
    return """
    ## Shopping List
    - Apples
    - Bananas
    - Carrots
    """

with gr.Blocks() as demo:
    output = gr.Markdown()
    gr.Button("Show List").click(get_list, None, output)

demo.launch()


# (----------------------------------------------------------------------------------------------------------------)

# Example 8: Markdown with Tables 

import gradio as gr

def get_table():
    return """
    ## Student Grades
    | Name    | Grade |
    |---------|-------|
    | Alice   | A     |
    | Bob     | B+    |
    | Charlie | A-    |
    """

with gr.Blocks() as demo:
    output = gr.Markdown()
    gr.Button("Show Table").click(get_table, None, output)

demo.launch()

# (----------------------------------------------------------------------------------------------------------------)

# Example 9: Markdown with Custom CSS

import gradio as gr

def get_custom_markdown():
    return """
    ## Styled Text
    <style>
    .styled-text { color: blue; font-size: 20px; }
    </style>
    <p class="styled-text">This text has custom styling!</p>
    """

with gr.Blocks() as demo:
    output = gr.Markdown(sanitize_html=False)
    gr.Button("Show Styled Text").click(get_custom_markdown, None, output)

demo.launch()
