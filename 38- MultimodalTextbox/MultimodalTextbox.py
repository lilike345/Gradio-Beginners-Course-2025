'''
The MultimodalTextbox component in Gradio is a versatile input/output component that allows users to input and display 
text along with uploading multimedia files like images, audio, or videos. This makes it incredibly useful for applications 
that require multimodal interaction, such as chatbots, multimedia annotation tools, and more.
'''

# Example 1: Basic MultimodalTextbox

import gradio as gr

def multimodal_example(value):
    return value

with gr.Blocks() as demo:
    input_textbox = gr.MultimodalTextbox(
        placeholder="Enter text or upload files...",
        file_count="multiple",
        sources=["upload"],
        file_types=["image", "video"],
        label="Upload or type message"
    )
    output_textbox = gr.MultimodalTextbox(label="Output")
    
    input_textbox.change(multimodal_example, inputs=input_textbox, outputs=output_textbox)
    
demo.launch()

# (---------------------------------------------------------------------------------------)

# Example 2: MultimodalTextbox with Microphone Input
import gradio as gr

def process_audio(value):
    text = value.get("text", "")
    files = value.get("files", [])
    return f"Received Text: {text}\nReceived Audio Files: {files}"

with gr.Blocks() as demo:
    input_box = gr.MultimodalTextbox(label="Enter text or record audio", sources=["microphone"], file_count="multiple")
    output_box = gr.Textbox(label="Processed Output")
    input_box.change(fn=process_audio, inputs=input_box, outputs=output_box)

demo.launch()

# (---------------------------------------------------------------------------------------)

# Example 3: Basic Chatbot with Multimodal Input

import gradio as gr
import time

def add_message(history, message):
    for x in message["files"]:
        history.append({"role": "user", "content": {"path": x}})
    if message["text"] is not None:
        history.append({"role": "user", "content": message["text"]})
    return history, gr.MultimodalTextbox(value=None, interactive=False)

def bot(history: list):
    response = "**That's cool!**"
    history.append({"role": "assistant", "content": ""})
    for character in response:
        history[-1]["content"] += character
        time.sleep(0.05)
        yield history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(elem_id="chatbot", bubble_full_width=False, type="messages")
    chat_input = gr.MultimodalTextbox(interactive=True, file_count="multiple", placeholder="Enter message or upload file...", show_label=False, sources=["microphone", "upload"])
    chat_msg = chat_input.submit(add_message, [chatbot, chat_input], [chatbot, chat_input])
    bot_msg = chat_msg.then(bot, chatbot, chatbot, api_name="bot_response")
    bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

if __name__ == "__main__":
    demo.launch()

# (-------------------------------------------------------------------------------------------)

# Example 4: Multimodal Input with Multiple File Types
import gradio as gr

def process_files(value):
    if value["files"]:
        return {"text": f"Files received: {value['files']}"}
    else:
        return {"text": "No files uploaded."}

with gr.Blocks() as demo:
    input_textbox = gr.MultimodalTextbox(
        placeholder="Upload files...",
        file_count="multiple",
        sources=["upload"],
        file_types=["image", "audio", "video"],
        label="Upload files"
    )
    output_textbox = gr.MultimodalTextbox(label="Output")
    
    input_textbox.change(process_files, inputs=input_textbox, outputs=output_textbox)
    
demo.launch()

# (-----------------------------------------------------------------------------------------------)


# Example 5: MultimodalTextbox with File Type Restrictions
import gradio as gr

def process_files(value):
    files = value.get("files", [])
    return f"Received Files: {files}"

with gr.Blocks() as demo:
    input_box = gr.MultimodalTextbox(label="Upload images only", sources=["upload"], file_types=["image/png", "image/jpeg"], file_count="single")
    output_box = gr.Textbox(label="Processed Output")
    input_box.change(fn=process_files, inputs=input_box, outputs=output_box)

demo.launch()


# (-------------------------------------------------------------------------------------------------)

# Example 6: Uploading directory and counting total files based on their type

import os
import gradio as gr
from collections import defaultdict

def process_directory(value):
    files = value.get("files", [])
    
    # Count total files
    total_files = len(files)
    
    # Count files by extension
    file_types = defaultdict(int)
    for file in files:
        ext = os.path.splitext(file)[1].lower()  # Get file extension
        file_types[ext] += 1

    # Format the output
    output = f"Total Files: {total_files}\n\nFile Types:\n"
    output += "\n".join(f"{ext if ext else 'No Extension'}: {count}" for ext, count in file_types.items())

    return output

with gr.Blocks() as demo:
    input_box = gr.MultimodalTextbox(label="Upload a directory", sources=["upload"], file_count="directory")
    output_box = gr.Textbox(label="Processed Output")
    input_box.change(fn=process_directory, inputs=input_box, outputs=output_box)

demo.launch()




