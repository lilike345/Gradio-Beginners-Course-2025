## 📌 **`gradio.Textbox`**  

### 🔹 **Description:**  
`gradio.Textbox` provides a simple text input area where users can enter text, which can be passed into a function or displayed as output.

### 🔹 **Behavior:**  
- **As Input Component:** Passes the text entered as a string (`str`) into the function.  
- **As Output Component:** Displays a string returned from the function in the text area.  

---

### 🔹 **Example Usage:**
#### ✅ **Simple Greeting App**
```python
import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(fn=greet, inputs=gr.Textbox(label="Your Name"), outputs="textbox")

if __name__ == "__main__":
    demo.launch()
```
💡 **Explanation:** The `gr.Textbox` component takes a user's name and returns a greeting.

---

### 🔹 **Initialization Parameters:**  
| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `str | Callable | None` | Default text in the textbox |
| `lines` | `int` | Number of lines visible in the textbox |
| `max_lines` | `int` | Maximum allowed lines in the textbox |
| `placeholder` | `str | None` | Placeholder text before user input |
| `label` | `str | None` | Label for the textbox |
| `info` | `str | None` | Additional information below the textbox |
| `interactive` | `bool | None` | If `True`, allows user interaction |
| `visible` | `bool` | If `False`, hides the component |
| `type` | `"text" | "password" | "email"` | Type of input (plain text, password, or email) |
| `text_align` | `"left" | "right" | None` | Text alignment |
| `show_copy_button` | `bool` | If `True`, shows a copy button |
| `max_length` | `int | None` | Maximum number of characters allowed |

💡 **Shortcut for `TextArea`:**  
- `gr.TextArea` is an alias for `gr.Textbox` with `lines=7` by default.

---

### 🔹 **Event Listeners:**  
| Listener | Description |
|----------|-------------|
| `.change(fn, ...)` | Triggered when the value of the textbox changes due to user input or function updates. |
| `.input(fn, ...)` | Triggered when the user types into the textbox. |
| `.select(fn, ...)` | Triggered when the user selects or deselects the textbox. |
| `.submit(fn, ...)` | Triggered when the user presses **Enter** while the textbox is focused. |
| `.focus(fn, ...)` | Triggered when the textbox gains focus. |
| `.blur(fn, ...)` | Triggered when the textbox loses focus. |
| `.stop(fn, ...)` | Triggered when media playback in the textbox stops. |
| `.copy(fn, ...)` | Triggered when the user copies text from the textbox. |

---

### 🔹 **Advanced Usage:**  
#### ✅ **Handling Multiple Inputs with `Textbox`**
```python
import gradio as gr

def summarize(text):
    return f"Word count: {len(text.split())}\nCharacter count: {len(text)}"

with gr.Blocks() as demo:
    txt_input = gr.Textbox(placeholder="Enter your text here...", lines=5)
    btn = gr.Button("Summarize")
    output = gr.Textbox(label="Summary", interactive=False)

    btn.click(fn=summarize, inputs=txt_input, outputs=output)

demo.launch()
```
💡 **Explanation:** The app counts words and characters in the entered text.

---

### 🔹 **When to Use `gradio.Textbox`?**  
✅ When collecting **single-line or multi-line text** input.  
✅ When displaying **string outputs** from a function.  
✅ When needing **different input types** like passwords or emails.  

This should help you efficiently integrate `gradio.Textbox` into your applications! 🚀