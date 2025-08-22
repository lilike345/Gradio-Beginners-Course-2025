'''

The `gradio.DownloadButton` component allows users to download a file with a single click. It accepts a file path
 (`str` or `pathlib.Path`) as output and can be dynamically updated based on user interactions. The button supports 
 customization options like labels, icons, and size variations. It also includes event listeners, enabling functions 
 to be triggered when clicked. This component is ideal for applications requiring users to retrieve processed files, 
 reports, or generated content. 🚀

'''

# Example 1: Simple Download Button

import gradio as gr

def download_file():
    return "example.txt"

demo = gr.Interface(
    fn=download_file,
    inputs=[],
    outputs=[gr.DownloadButton("Download File")],
    title="Simple Download Button"
)

if __name__ == "__main__":
    demo.launch()


# (------------------------------------------------------------------------------------------)

# Example 2: Download Button with Custom Label

import gradio as gr

def download_file():
    return "example.txt"

demo = gr.Interface(
    fn=download_file,
    inputs=[],
    outputs=[gr.DownloadButton(label="Download Example File")],
    title="Custom Label Download Button"
)

if __name__ == "__main__":
    demo.launch()



# (--------------------------------------------------------------------------------------------)

# Example 3: Download Button with Icon

import gradio as gr

def download_file():
    return "example.txt"

demo = gr.Interface(
    fn=download_file,
    inputs=[],
    outputs=[gr.DownloadButton("Download File", icon="fa fa-download")],
    title="Download Button with Icon"
)

if __name__ == "__main__":
    demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 4: Download Button with Custom CSS

import gradio as gr

def download_file():
    return "example.txt"

demo = gr.Interface(
    fn=download_file,
    inputs=[],
    outputs=[gr.DownloadButton("Download File", elem_classes=["custom-button"])],
    title="Download Button with Custom CSS",
    css=".custom-button { background-color: #4CAF50; color: #fff; }"
)

if __name__ == "__main__":
    demo.launch()


# (----------------------------------------------------------------------------------------------)