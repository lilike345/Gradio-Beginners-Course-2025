## 📌 **`gradio.Info`**

### 🔹 **Description:**
The `gradio.Info` class allows you to pass custom informational messages to the user. When this function is called within your code, a modal with the given message will appear to notify the user with helpful information. The modal is typically gray and is labeled with the heading "Info". 

- **Queueing Behavior:**
  - Queue must be enabled for the modal to show up on the interface. If queueing is not enabled, the message will be printed in the console instead.

- **Duration Control:** 
  - You can control how long the message is displayed using the `duration` parameter. 
  - If `None`, the message will stay visible indefinitely until the user closes it.
  - If a duration (in seconds) is specified, the message will automatically disappear after the given time.

- **Visibility:** 
  - You can choose to hide the info message by setting `visible=False`.

---

### 🔹 **Usage Pattern:**

#### **Displaying Information to Users:**

```python
import gradio as gr

def hello_world():
    gr.Info('This is some info.')
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```

- **Explanation:** In this example, when the function `hello_world` is executed, an informational message `"This is some info."` will appear in a modal.

---

### 🔹 **Parameters:**

#### 1️⃣ **`message: str`**
- **Description:** The custom info message that you wish to display in the modal.

#### 2️⃣ **`duration: float | None`**
- **Description:** Controls the duration for which the info message will be displayed.
  - If `None`, the message will remain until the user closes it.
  - If a number is provided, the message will disappear after that many seconds.

#### 3️⃣ **`visible: bool`**
- **Description:** A flag to control the visibility of the info modal. Setting this to `False` prevents the message from being shown in the UI.

#### 4️⃣ **`title: str`**
- **Description:** The title of the info modal (e.g., "Info"). 

---

### 🔹 **Example Usage:**

#### ✅ **Example 1: Basic Info Message**
```python
import gradio as gr

def hello_world():
    gr.Info('This is some info.')
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```
- **Explanation:** When the function `hello_world()` is executed, the info message `"This is some info."` will appear in the modal.

#### ✅ **Example 2: Info Message with Duration**
```python
import gradio as gr

def hello_world():
    gr.Info('This is some info.', duration=5)
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```
- **Explanation:** In this case, the info message will stay visible for 5 seconds before disappearing automatically.

#### ✅ **Example 3: Info Message with Visibility Control**
```python
import gradio as gr

def hello_world():
    gr.Info('This is some info.', visible=False)
    return "hello world"

with gr.Blocks() as demo:
    md = gr.Markdown()
    demo.load(hello_world, inputs=None, outputs=[md])

demo.queue().launch()
```
- **Explanation:** Here, the info message will not appear because the visibility flag is set to `False`.

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
- **Explanation:** This demo tests the behavior of different status modals including the info modal. When the "Trigger Info" button is clicked, the info message `"This is some info"` will be shown.

---

### 🔹 **Summary:**
- The `gr.Info` class enables you to display custom information messages to users.
- It supports parameters for controlling the message's duration, visibility, title, and event triggers.
- Using `gr.Info`, you can guide users with helpful tips, without disrupting their flow like error or warning messages might.