## 📌 **`gradio.Error`**

### 🔹 **Description:**
The `gradio.Error` class allows you to pass custom error messages to the user. This is particularly useful for situations where an operation cannot be completed, and you want to notify the user with a descriptive error message.

You can raise an error by using `raise gr.Error("custom message")` at any point in the code. When this error is raised, the custom message will appear in a modal within the Gradio app. 

- **Duration Control:** 
  - The error message can be shown for a specified duration using the `duration` parameter. 
  - If `duration` is `None`, the error message will remain visible until the user closes it manually.
  - If `duration` is a number, the message will automatically disappear after that many seconds.

- **Visibility:** 
  - You can control whether the error modal is shown by setting the `visible` parameter to `False`.

---

### 🔹 **Usage Pattern:**

#### **Raising an Error when a Condition is Met:**

```python
import gradio as gr

def divide(numerator, denominator):
    if denominator == 0:
        raise gr.Error("Cannot divide by zero!")

gr.Interface(divide, ["number", "number"], "number").launch()
```

- **Explanation:** In this example, when the user tries to divide by zero, the `gr.Error` class is used to raise an error with a custom message `"Cannot divide by zero!"`. This message will appear in a modal on the Gradio interface.

---

### 🔹 **Parameters:**

#### 1️⃣ **`message: str`**
- **Description:** The error message to be displayed in the modal.

#### 2️⃣ **`duration: float | None`**
- **Description:** The duration for which the error message will be displayed. 
  - If `None`, the message will be shown indefinitely until the user closes it.
  - If a float value is provided, the error will be shown for that many seconds.

#### 3️⃣ **`visible: bool`**
- **Description:** Whether the error modal should be visible. If set to `False`, the error modal will not appear.

#### 4️⃣ **`title: str`**
- **Description:** The title of the error modal.

#### 5️⃣ **`print_exception: bool`**
- **Description:** Whether to print the exception stack trace in the console. If `True`, the exception will be logged.

---

### 🔹 **Example Usage:**

#### ✅ **Example 1: Basic Error Message**
```python
import gradio as gr

def divide(numerator, denominator):
    if denominator == 0:
        raise gr.Error("Cannot divide by zero!")

gr.Interface(divide, ["number", "number"], "number").launch()
```
- **Explanation:** When the denominator is zero, the error message `"Cannot divide by zero!"` will be raised and displayed in a modal to the user.

#### ✅ **Example 2: Error Message with Duration**
```python
import gradio as gr

def divide(numerator, denominator):
    if denominator == 0:
        raise gr.Error("Cannot divide by zero!", duration=5)

gr.Interface(divide, ["number", "number"], "number").launch()
```
- **Explanation:** This example shows how the error message will appear for 5 seconds before disappearing automatically.

#### ✅ **Example 3: Error Message with Title and Visibility**
```python
import gradio as gr

def divide(numerator, denominator):
    if denominator == 0:
        raise gr.Error("Cannot divide by zero!", title="Error!", visible=True)

gr.Interface(divide, ["number", "number"], "number").launch()
```
- **Explanation:** Here, the error message `"Cannot divide by zero!"` will be displayed with the title `"Error!"` in the modal and will be visible to the user.

---

### 🔹 **Summary:**
- The `gr.Error` class enables you to display custom error messages to users.
- It supports parameters for controlling the message's duration, visibility, title, and exception logging.
- Raising `gr.Error` can help provide clear, immediate feedback to the user in cases of invalid input or failed operations.