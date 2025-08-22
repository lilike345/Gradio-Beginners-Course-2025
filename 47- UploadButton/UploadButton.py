'''
The gradio.UploadButton component is a powerful tool in Gradio for allowing users to upload files to your application. 
It can be configured to accept specific file types, handle single or multiple file uploads, and even entire directories. 
This component can be used both as an input and an output, making it versatile for various use cases.
'''

# Example 1: Basic Single File Upload and output its type

import gradio as gr
import os

def display_filetype(filepath):
    return f"File Type: {os.path.splitext(filepath)[1]}"

with gr.Blocks() as demo:
    gr.Markdown("Upload a file and see its type.")
    upload_button = gr.UploadButton("Upload a file", file_count="single")
    output = gr.Textbox(label="File Type")
    upload_button.upload(display_filetype, upload_button, output)

demo.launch()


# (-----------------------------------------------------------------------------------)

# Example 2: Multiple File Upload and output their type

import gradio as gr
import os

def display_filetypes(filepaths):
    return "\n".join(os.path.splitext(fp)[1] for fp in filepaths)

with gr.Blocks() as demo:
    gr.Markdown("Upload multiple files and see their types.")
    upload_button = gr.UploadButton("Upload files", file_count="multiple")
    output = gr.Textbox(label="File Types")
    upload_button.upload(display_filetypes, upload_button, output)

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 3: Directory Upload

import gradio as gr
import os

def display_filetypes(filepaths):
    return "\n".join(os.path.splitext(fp)[1] for fp in filepaths)

with gr.Blocks() as demo:
    gr.Markdown("Upload a directory and see file types of its contents.")
    upload_button = gr.UploadButton("Upload directory", file_count="directory")
    output = gr.Textbox(label="File Types in Directory")
    upload_button.upload(display_filetypes, upload_button, output)

demo.launch()

# (---------------------------------------------------------------------------------------)

# Example 4: Download Button Integration
#After uploading a file, a download button appears to allow the user to download the same file.

from pathlib import Path
import gradio as gr

def upload_file(filepath):
    name = Path(filepath).name
    return [gr.UploadButton(visible=False), gr.DownloadButton(label=f"Download {name}", value=filepath, visible=True)]

def download_file():
    return [gr.UploadButton(visible=True), gr.DownloadButton(visible=False)]

with gr.Blocks() as demo:
    gr.Markdown("Upload a file and download it.")
    with gr.Row():
        u = gr.UploadButton("Upload a file", file_count="single")
        d = gr.DownloadButton("Download the file", visible=False)

    u.upload(upload_file, u, [u, d])
    d.click(download_file, None, [u, d])

demo.launch()

# (----------------------------------------------------------------------------------------)

# Example 5: File Size Display

import os
import gradio as gr

def display_filesize(filepath):
    size = os.path.getsize(filepath)
    return f"File size: {size} bytes"

with gr.Blocks() as demo:
    gr.Markdown("Upload a file and see its size.")
    upload_button = gr.UploadButton("Upload a file", file_count="single")
    output = gr.Textbox(label="File Size")
    upload_button.upload(display_filesize, upload_button, output)

demo.launch()


# (-----------------------------------------------------------------------------------------)

# Example 6: File Content Display

import gradio as gr

def display_file_content(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    return content

with gr.Blocks() as demo:
    gr.Markdown("Upload a text file and see its content.")
    upload_button = gr.UploadButton("Upload text file", file_types=[".txt"])
    output = gr.Textbox(label="File Content")
    upload_button.upload(display_file_content, upload_button, output)

demo.launch()


# (------------------------------------------------------------------------------------------)
