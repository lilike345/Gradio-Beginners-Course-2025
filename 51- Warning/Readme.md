## 📌 **`gradio.Warning`**

### 🔹 **Description:**
The `gradio.Warning` class allows you to display custom warning messages to the user. When this function is called, a modal with the specified message will appear on the demo interface. The modal is yellow by default and is labeled with the heading "Warning". 

- **Queueing Behavior:**
  - The modal will only be shown if the queue is enabled. If queueing is not enabled, the warning message will be printed to the console using Python’s `warnings` library instead.

- **Duration Control:** 
  - You can control how long the warning message is displayed using the `duration` parameter.
  - If `None`, the message will remain visible indefinitely until the user closes it.
  - If a number is provided (in seconds), the message will automatically disappear after the specified time.

- **Visibility:** 
  - You can hide the warning modal by setting `visible=False`.

---

### 🔹 **Usage Pattern:**

#### **Displaying Warning Messages to Users:**

```python
import gradio as gr

def hello_world():
    gr.Warning('This is a warning message.')
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```

- **Explanation:** In this example, when the `hello_world` function is executed, the warning message `"This is a warning message."` will appear in a yellow modal.

---

### 🔹 **Parameters:**

#### 1️⃣ **`message: str`**
- **Description:** The custom warning message that you wish to display in the modal.

#### 2️⃣ **`duration: float | None`**
- **Description:** Controls the duration for which the warning message will be displayed.
  - If `None`, the message will stay visible until the user closes it.
  - If a number is provided (in seconds), the message will disappear automatically after that time.

#### 3️⃣ **`visible: bool`**
- **Description:** A flag to control the visibility of the warning modal. Setting this to `False` prevents the message from being shown in the UI.

#### 4️⃣ **`title: str`**
- **Description:** The title of the warning modal (e.g., "Warning"). 

---

### 🔹 **Example Usage:**

#### ✅ **Example 1: Basic Warning Message**
```python
import gradio as gr

def hello_world():
    gr.Warning('This is a warning message.')
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```
- **Explanation:** This example displays the warning message `"This is a warning message."` when the function `hello_world()` is executed.

#### ✅ **Example 2: Warning Message with Duration**
```python
import gradio as gr

def hello_world():
    gr.Warning('This is a warning message.', duration=5)
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```
- **Explanation:** The warning message will remain visible for 5 seconds before disappearing automatically.

#### ✅ **Example 3: Warning Message with Visibility Control**
```python
import gradio as gr

def hello_world():
    gr.Warning('This is a warning message.', visible=False)
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```
- **Explanation:** In this case, the warning message will not be displayed because the visibility flag is set to `False`.

---

### 🔹 **Demos:**

#### ✅ **Demo 1: Success, Warning, Info, and Error Handling**

```python
import gradio as gr

def failure():
    raise gr.Error("This should fail!")

def exception():
    raise ValueError("Something went wrong")

def success():
    return True

def warning_fn():
    gr.Warning("This is a warning!")

def info_fn():
    gr.Info("This is some info")

with gr.Blocks() as demo:
    gr.Markdown("Used in E2E tests of success event trigger. The then event covered in chatbot E2E tests. Also testing that the status modals show up.")
    with gr.Row():
        result = gr.Textbox(label="Result")
        result_2 = gr.Textbox(label="Consecutive Event")
    with gr.Row():
        success_btn = gr.Button(value="Trigger Success")
        success_btn_2 = gr.Button(value="Trigger Consecutive Success")
        failure_btn = gr.Button(value="Trigger Failure")
        failure_exception = gr.Button(value="Trigger Failure With ValueError")
    with gr.Row():
        trigger_warning = gr.Button(value="Trigger Warning")
        trigger_info = gr.Button(value="Trigger Info")

        success_btn_2.click(success, None, None).success(lambda: "First Event Trigered", None, result).success(lambda: "Consecutive Event Triggered", None, result_2)
        success_btn.click(success, None, None).success(lambda: "Success event triggered", inputs=None, outputs=result)
        failure_btn.click(failure, None, None).success(lambda: "Should not be triggered", inputs=None, outputs=result)
        failure_exception.click(exception, None, None)
        trigger_warning.click(warning_fn, None, None)
        trigger_info.click(info_fn, None, None)

if __name__ == "__main__":
    demo.launch(show_error=True)
```
- **Explanation:** This demo tests various status modals, including the warning modal. When the `"Trigger Warning"` button is clicked, the warning message `"This is a warning!"` will be shown in a yellow modal.

---

### 🔹 **Summary:**
- The `gr.Warning` class helps you display custom warning messages to users in your Gradio interface.
- It supports parameters for controlling the message’s visibility, duration, and title.
- Using `gr.Warning`, you can alert users to potential issues without disrupting their flow, unlike error messages which might require corrective action.