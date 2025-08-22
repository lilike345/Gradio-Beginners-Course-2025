
---

### **gradio.Chatbot**
```python
gradio.Chatbot(type="messages", ···)
```

#### **Description**
Creates a chatbot component that displays user-submitted messages and responses. It supports:
- A subset of **Markdown** (bold, italics, code, tables).
- **Multimedia files** (audio, video, images) displayed directly.
- **Other file types** displayed as downloadable links.
- Used primarily as an **output component**.

---

### **Behavior**
The chatbot supports **two data formats** controlled by the `type` parameter:
1. **"messages" (Recommended)**  
   - Data is a list of dictionaries with `"role"` and `"content"` keys.
   - Compatible with LLM APIs (e.g., OpenAI, Claude, HuggingChat).
   - Supports displaying **Gradio components** inside the chatbot.
   
   **Example:**
   ```python
   import gradio as gr

   history = [
       {"role": "assistant", "content": "I am happy to provide you that report and plot."},
       {"role": "assistant", "content": gr.Plot(value=make_plot_from_file('quarterly_sales.txt'))}
   ]

   with gr.Blocks() as demo:
       gr.Chatbot(history)

   demo.launch()
   ```

2. **"tuples" (Deprecated)**
   - Uses a **list of (user_message, bot_response) tuples**.
   - Will be removed in future versions.

---

### **Initialization Parameters**
| Parameter         | Type | Description |
|------------------|------|-------------|
| `value` | `list[MessageDict | Message]` \| `TupleFormat` \| `Callable` \| `None` | Initial chatbot history. |
| `type` | `'messages'` \| `'tuples'` | Format of chatbot data (use `'messages'`). |
| `label` | `str` | Label for the component. |
| `inputs` | `Component` \| `list[Component]` | Components that act as chatbot inputs. |
| `visible` | `bool` | Show or hide the chatbot. |
| `autoscroll` | `bool` | Automatically scroll to the latest message. |
| `editable` | `'user'` \| `'all'` \| `None` | Who can edit messages in the chatbot. |
| `layout` | `'panel'` \| `'bubble'` | Display style of chatbot messages. |
| `group_consecutive_messages` | `bool` | Whether to merge messages from the same sender. |
| `show_copy_button` | `bool` | Show a copy button for chatbot messages. |
| `allow_file_downloads` | `bool` | Allow users to download files sent in the chat. |

---

### **Event Listeners**
Gradio's `Chatbot` component supports multiple event listeners:

| Listener | Description |
|----------|------------|
| `Chatbot.change(fn, ···)` | Triggers when the chatbot's value changes (user input or function update). |
| `Chatbot.select(fn, ···)` | Triggers when the chatbot is selected/deselected. |
| `Chatbot.like(fn, ···)` | Triggers when the user likes/dislikes a message. |
| `Chatbot.retry(fn, ···)` | Triggers when the user clicks **Retry** on a chatbot message. |
| `Chatbot.undo(fn, ···)` | Triggers when the user clicks **Undo** on a chatbot message. |
| `Chatbot.example_select(fn, ···)` | Triggers when the user selects an example in the chatbot. |
| `Chatbot.option_select(fn, ···)` | Triggers when the user selects an option in the chatbot. |
| `Chatbot.clear(fn, ···)` | Triggers when the chatbot is cleared. |
| `Chatbot.copy(fn, ···)` | Triggers when the user copies a message. |
| `Chatbot.edit(fn, ···)` | Triggers when a chatbot message is edited. |

**Example Usage:**
```python
chatbot.change(fn=update_chat, inputs=chatbot, outputs=chatbot)
```

---

### **Using Gradio Components Inside Chatbot**
You can embed **Gradio components** (like `gr.Image`, `gr.Plot`, `gr.Audio`) inside the chatbot.

#### **Example: Displaying Audio & Video**
```python
import gradio as gr

def load():
    return [
        ("Here's an audio", gr.Audio("https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav")),
        ("Here's a video", gr.Video("https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4"))
    ]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    button = gr.Button("Load audio and video")
    button.click(load, None, chatbot)

demo.launch()
```

---

### **Example: A Basic Chatbot**
```python
import gradio as gr
import random
import time

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "Today is a great day!", "I'm very hungry."])
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": bot_message})
        time.sleep(2)  # Simulate response delay
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()
```

---

### **Helper Class: `ChatMessage`**
Gradio provides a helper **dataclass** for chatbot messages.
```python
gradio.ChatMessage(role="assistant", content="Hello!")
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `content` | `str` \| `FileData` \| `Component` | The message content (text, image, audio, etc.). |
| `role` | `'user'` \| `'assistant'` \| `'system'` | Role of the message sender. |
| `metadata` | `dict` | Additional metadata (e.g., tool usage info). |

**Example: Displaying AI Tool Metadata**
```python
def generate_response(history):
    history.append(
        gr.ChatMessage(
            role="assistant",
            content="The weather API says it is 20°C in New York.",
            metadata={"title": "🛠️ Used tool: Weather API"}
        )
    )
    return history
```

---

### **Demos**
Gradio provides interactive demos:
- **`chatbot_simple`**
- **`chatbot_streaming`**
- **`chatbot_with_tools`**
- **`chatbot_core_components`**

To explore further, check out the Gradio documentation and examples.

---

