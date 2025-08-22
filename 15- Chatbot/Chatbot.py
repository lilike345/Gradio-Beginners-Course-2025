'''
Gradio's Chatbot component is a powerful tool for building interactive chat interfaces in your web applications. 
It supports rich text formatting, image, video, and audio content, and can be integrated seamlessly with other Gradio components. 
The Chatbot component is typically used for creating conversational interfaces, displaying thoughts or tool usage, and integrating 
with large language models (LLMs).
'''

# Example 1: Basic Chatbot with Static Responses

import gradio as gr

def respond(message, chat_history):
    bot_message = "Hello! How can I help you today?"
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

#(-----------------------------------------------------------------------------)

# Example 2: Chatbot with Random Responses

import gradio as gr
import random

def respond(message, chat_history):
    bot_message = random.choice(["How are you?", "Today is a great day", "I'm very hungry"])
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

#(-----------------------------------------------------------------------------)

# Example 3: Chatbot with Metadata

import gradio as gr

def respond(message, chat_history):
    bot_message = "The weather API says it is 20 degrees Celsius in New York."
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message, "metadata": {"title": "🛠️ Used tool Weather API"}})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

#(------------------------------------------------------------------------------)

# Example 4: Chatbot with Image and Video

import gradio as gr

def load():
    return [
        {"role": "assistant", "content": "Here's an audio", "metadata": {"title": "Audio Sample"}},
        {"role": "assistant", "content": gr.Audio("https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav")},
        {"role": "assistant", "content": "Here's a video", "metadata": {"title": "Video Sample"}},
        {"role": "assistant", "content": gr.Video("https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4")}
    ]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    button = gr.Button("Load audio and video")
    button.click(load, None, chatbot)

demo.launch()


#(-----------------------------------------------------------------------------)

# Example 5: Chatbot with Custom Avatar Images

import gradio as gr

def respond(message, chat_history):
    bot_message = "Hello! How can I help you today?"
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages", avatar_images=("https://cdn.pixabay.com/photo/2022/10/10/18/39/flower-7512435_1280.jpg", 
    	"https://cdn.pixabay.com/photo/2024/02/27/00/15/chrysanthemum-8599121_1280.jpg"))
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

# (------------------------------------------------------------------------------)

# Example 6: Chatbot with Clear Button

import gradio as gr

def respond(message, chat_history):
    bot_message = f"Echo: {message}"
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()


# (--------------------------------------------------------------------------------)

# Example 7: Chatbot with Copy Button

import gradio as gr

def respond(message, chat_history):
    bot_message = f"Echo: {message}"
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages", show_copy_button=True)
    msg = gr.Textbox()
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

































