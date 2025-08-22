'''
The File component in Gradio allows users to upload one or more files and can also be used to display files or URLs for download. 
This component is versatile and can handle different file types and counts (single, multiple, or directory).
'''

# Example 1: Single File Upload (Text File)

# Upload a single text file and display its content.

import gradio as gr

def show_file_content(file):
    with open(file.name, 'r') as f:
        return f.read()

iface = gr.Interface(
    fn=show_file_content,
    inputs=gr.File(label="Upload Text File"),
    outputs="text",
    title="Text File Viewer"
)

iface.launch()

# (-------------------------------------------------------------------------------------------)

# Example 2: Multiple File Upload (Images)
# Upload multiple images and display them.

import gradio as gr
from PIL import Image

def display_images(files):
    images = [Image.open(file.name) for file in files]
    return images

iface = gr.Interface(
    fn=display_images,
    inputs=gr.File(label="Upload Images", file_count="multiple", file_types=["image"]),
    outputs="gallery",
    title="Image Viewer"
)

iface.launch()

# (--------------------------------------------------------------------------------------------)

# Example 3: File Download
# Upload a file and provide a download link for the same file.

import gradio as gr

def download_file(file):
    return file.name

iface = gr.Interface(
    fn=download_file,
    inputs=gr.File(label="Upload File"),
    outputs=gr.File(label="Download File"),
    title="File Uploader and Downloader"
)

iface.launch()

# (---------------------------------------------------------------------------------------------)

# Example 4: File Upload with Custom File Types
# Upload only specific types of files (e.g., .csv).

import gradio as gr

def process_csv(file):
    with open(file.name, 'r') as f:
        return f.read()

iface = gr.Interface(
    fn=process_csv,
    inputs=gr.File(label="Upload CSV File", file_types=[".csv"]),
    outputs="text",
    title="CSV File Processor"
)

iface.launch()


# (---------------------------------------------------------------------------------------------)

# Example 5: File Upload and Process with Progress Bar
#Upload a large file and process it with a progress bar to keep the user informed.

import gradio as gr
import time

def process_large_file(file):
    with open(file.name, 'r') as f:
        content = f.read()
    total_length = len(content)
    chunk_size = total_length // 10  # Divide into 10 chunks
    for i in range(10):
        time.sleep(1)  # Simulate processing time
        yield f"Processed {i*chunk_size} / {total_length} characters"
    return content

iface = gr.Interface(
    fn=process_large_file,
    inputs=gr.File(label="Upload Large Text File"),
    outputs="text",
    title="Large File Processor with Progress",
    show_progress="full"
)

iface.launch()

# (----------------------------------------------------------------------------------------------)

# Example 6: File Upload and Convert to Different Format
# Upload a file and convert it to a different format (e.g., converting a CSV to JSON).

import gradio as gr
import pandas as pd
import json

def convert_csv_to_json(file):
    df = pd.read_csv(file.name)
    json_data = df.to_json(orient='records')
    return json_data

iface = gr.Interface(
    fn=convert_csv_to_json,
    inputs=gr.File(label="Upload CSV File", file_types=[".csv"]),
    outputs="json",
    title="CSV to JSON Converter"
)

iface.launch()


# (-----------------------------------------------------------------------------------------------)

# Example 7: File Upload and Generate Summary
# Upload a text file and generate a summary using a simple text processing function.

import gradio as gr
from transformers import pipeline

def summarize_text(file):
    summarizer = pipeline("summarization")
    with open(file.name, 'r') as f:
        text = f.read()
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.File(label="Upload Text File"),
    outputs="text",
    title="Text Summarizer"
)

iface.launch()





