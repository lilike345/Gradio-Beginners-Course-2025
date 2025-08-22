# Gradio ChatInterface 

## Overview

The `gr.ChatInterface` class in Gradio is a high-level abstraction specifically designed for creating chatbot UIs. This class allows you to create a web-based demo around a chatbot model in just a few lines of code. The main parameter required is the function (`fn`), which governs how the chatbot responds to user input and chat history. You can customize the chatbot’s behavior, appearance, and interactivity using additional parameters.

## Example Usage

### Basic Example: Echo Chatbot

In this simple example, the chatbot echoes back whatever message the user sends.

```python
import gradio as gr

def echo(message, history):
    return message

demo = gr.ChatInterface(fn=echo, type="messages", examples=["hello", "hola", "merhaba"], title="Echo Bot")
demo.launch()
```

This demonstrates a straightforward chatbot where the function `echo` takes the user’s input and history, and simply returns the input message. The `gr.ChatInterface` is launched with a few examples and a title.

### Custom Chatbot with Like/Dislike Feature

Here is an example of a more advanced chatbot with a custom `gr.Chatbot` that includes a placeholder and upvote/downvote buttons. The voting behavior is added via a `.like()` event.

```python
import gradio as gr

def yes(message, history):
    return "yes"

def vote(data: gr.LikeData):
    if data.liked:
        print("You upvoted this response: " + data.value["value"])
    else:
        print("You downvoted this response: " + data.value["value"])

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(placeholder="<strong>Your Personal Yes-Man</strong><br>Ask Me Anything")
    chatbot.like(vote, None, None)
    gr.ChatInterface(fn=yes, type="messages", chatbot=chatbot)
    
demo.launch()
```

In this example:
- The chatbot is set with a placeholder and the upvote/downvote functionality is integrated using a `gr.LikeData` callback.
- The `gr.ChatInterface` is wrapped inside a `gr.Blocks()` to ensure the interaction between the chatbot and the voting system.

## Parameters

### Main Parameters

- **fn**: `Callable`  
  A Python function that defines how the chatbot should respond based on the input message and the conversation history. The function must accept two parameters: the user's message and the chat history, and return the chatbot's response.

- **type**: `'messages' | 'tuples' | None`  
  Specifies the format of the conversation. Use `messages` for the typical message-response format, or `tuples` for a tuple format where each conversation entry is a pair of (input, output).

- **chatbot**: `Chatbot | None`  
  A custom `gr.Chatbot` component used to define the appearance and behavior of the chatbot. If not provided, a default chatbot is used.

- **textbox**: `Textbox | MultimodalTextbox | None`  
  The input textbox where users type their messages. This can be customized to use a `MultimodalTextbox` for more complex inputs.

- **additional_inputs**: `str | Component | list[str | Component] | None`  
  Optional additional inputs (other than the user message) that can be included in the chatbot interface.

- **editable**: `bool`  
  Determines whether the user can edit the messages in the chat history.

- **examples**: `list[str] | list[MultimodalValue] | list[list] | None`  
  A list of example messages that users can click on to try out the chatbot with predefined inputs.

- **example_labels**: `list[str] | None`  
  Optional labels for the example inputs.

- **title**: `str | None`  
  The title of the chatbot interface.

- **description**: `str | None`  
  A description that can be shown alongside the interface.

- **theme**: `Theme | str | None`  
  The theme of the chatbot interface (e.g., "dark", "light").

- **flagging_mode**: `'never' | 'manual' | None`  
  Defines the flagging behavior. If set to `manual`, users can flag responses for review.

- **flagging_options**: `list[str] | tuple[str, ...] | None`  
  Options for flagging responses, such as "Spam", "Offensive", or custom options.

- **analytics_enabled**: `bool | None`  
  Whether to enable or disable the collection of analytics for the chatbot interaction.

- **autofocus**: `bool`  
  If set to `True`, the input box will automatically gain focus when the page loads.

- **autoscroll**: `bool`  
  If set to `True`, the chat interface will automatically scroll to the bottom as new messages are sent.

- **submit_btn**: `str | bool | None`  
  Customize the submit button text or hide it if `False`.

- **stop_btn**: `str | bool | None`  
  Customize the stop button text or hide it if `False`.

- **show_progress**: `'full' | 'minimal' | 'hidden'`  
  Defines the level of progress display while the chatbot is processing a response.

- **fill_height**: `bool`  
  If `True`, the chatbot interface will fill the available height of the browser window.

- **fill_width**: `bool`  
  If `True`, the chatbot interface will fill the available width of the browser window.

- **save_history**: `bool`  
  If `True`, the chatbot will save the conversation history, allowing users to scroll through previous messages.

### Additional Features

- **css**: `str | None`  
  Custom CSS to style the chatbot interface.

- **css_paths**: `str | Path | list[str | Path] | None`  
  Path to external CSS files to be applied to the interface.

- **js**: `str | None`  
  Custom JavaScript for advanced behavior or interaction handling.

- **head**: `str | None`  
  Custom HTML or metadata to be included in the header of the page.

- **head_paths**: `str | Path | list[str | Path] | None`  
  Paths to external files to be included in the header.

### Advanced Interaction

- **concurrency_limit**: `int | None | 'default'`  
  Limits the number of concurrent interactions with the chatbot.

- **delete_cache**: `tuple[int, int] | None`  
  Controls cache management for the interface.

## Demos

- **chatinterface_random_response**: A chatbot that provides random responses like "Yes" or "No".
- **chatinterface_streaming_echo**: A streaming echo chatbot where each message is echoed back progressively.
- **chatinterface_artifacts**: A chatbot that handles multimodal inputs (e.g., text + images).

## Example: Random Response Chatbot

```python
import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

demo = gr.ChatInterface(random_response, type="messages", autofocus=False)

if __name__ == "__main__":
    demo.launch()
```

This example demonstrates a chatbot that responds randomly with either "Yes" or "No" when the user sends a message.

## Conclusion

The `gr.ChatInterface` class in Gradio provides an easy-to-use framework for building sophisticated chatbots with minimal code. With its rich set of parameters and methods, you can customize the chatbot's behavior, appearance, and user experience, making it ideal for deploying machine learning models or interactive chat-based applications in a web interface.