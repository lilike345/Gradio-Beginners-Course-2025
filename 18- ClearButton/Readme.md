
---

# **Gradio `ClearButton`**  

## **Overview**  
`gr.ClearButton` is a Gradio UI component that **clears the value of one or more components** when clicked. It is useful in applications where users need a **reset** button to clear input fields, selections, or other UI components.  

## **Behavior**  

### **As an Input Component**  
- The button **sends its label (`str`)** when clicked, but this is **rarely used** as an input in function calls.  
- Function signature when used as input:  
  ```python
  def predict(value: str | None):
      ...
  ```

### **As an Output Component**  
- The function should return a string that represents the **button label**.  
- Function signature when used as output:  
  ```python
  def predict(...) -> str | None:
      return value
  ```

---

## **Initialization Parameters**  

| **Parameter**  | **Type**  | **Description**  |
|---------------|-----------|------------------|
| `components`  | `None | list[Component] | Component` | Specifies the list of components that will be cleared when the button is clicked. |
| `value`  | `str`  | The **label text** displayed on the button. |
| `every`  | `Timer | float | None` | Defines whether the component updates automatically at a given time interval. |
| `inputs`  | `Component | list[Component] | set[Component] | None` | Defines which components affect this button. |
| `variant`  | `"primary" | "secondary" | "stop"` | Defines the button's style variant. |
| `size`  | `"sm" | "md" | "lg"` | Specifies the button size (`small`, `medium`, `large`). |
| `icon`  | `str | Path | None` | Adds an **icon** to the button (e.g., a reset icon). |
| `link`  | `str | None` | Turns the button into a clickable **link** instead of a functional button. |
| `visible`  | `bool`  | **Determines visibility** (default: `True`). |
| `interactive`  | `bool`  | Specifies whether the button is **clickable**. |
| `elem_id`  | `str | None`  | Assigns a **unique HTML ID** for CSS customization. |
| `elem_classes`  | `list[str] | str | None`  | Assigns **CSS classes** for custom styling. |
| `render`  | `bool`  | Determines whether the button should **render** in the UI. |
| `key`  | `int | str | None`  | Assigns a unique identifier for **session state** persistence. |
| `scale`  | `int | None`  | Defines the button **size ratio** in a row layout. |
| `min_width`  | `int | None`  | Specifies the **minimum width** of the button. |
| `api_name`  | `str | None | "False"`  | Assigns an **API name** for external access. |
| `show_api`  | `bool`  | Determines whether the API call is **displayed in the UI**. |

---

## **Shortcuts**  
| **Class** | **Interface String Shortcut** | **Initialization** |
|-----------|---------------------------|----------------|
| `gradio.ClearButton` | `"clearbutton"` | Uses default values |

---

## **Event Listeners**  

### **Overview**  
Event listeners allow you to **respond to user interactions** with UI components. In this case, the **ClearButton** supports the following event listeners.

| **Listener**  | **Description**  |
|--------------|-----------------|
| `ClearButton.add(fn, ···)`  | Adds a component or list of components that will be **cleared** when the button is clicked. |
| `ClearButton.click(fn, ···)`  | **Triggered when the button is clicked.** Can be used to perform additional actions. |

---

## **Event Parameters**  

| **Parameter** | **Type** |
|--------------|----------|
| `components` | `None | Component | list[Component]` |

---

## **Example Usage**  

### **Basic Example: Clearing a Textbox**  
```python
import gradio as gr

with gr.Blocks() as demo:
    textbox = gr.Textbox(label="Enter some text")
    clear_button = gr.ClearButton(components=[textbox])

demo.launch()
```
📌 **Explanation:**  
- A `Textbox` is created where users can enter text.  
- The `ClearButton` is linked to the `Textbox`, so clicking the button will clear the input field.

---

### **Advanced Example: Clearing Multiple Components**  
```python
import gradio as gr

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    email = gr.Textbox(label="Email")
    message = gr.Textbox(label="Message", lines=3)

    clear_all = gr.ClearButton(components=[name, email, message], value="Reset Form")

demo.launch()
```
📌 **Explanation:**  
- This form contains **three textboxes** (Name, Email, and Message).  
- The **"Reset Form"** button clears all three fields when clicked.

---

### **Example: Using `ClearButton.click()` for Additional Actions**  
```python
import gradio as gr

def on_clear():
    return "Cleared!"

with gr.Blocks() as demo:
    textbox = gr.Textbox(label="Type something")
    message = gr.Textbox(label="Status", interactive=False)
    
    clear_button = gr.ClearButton(components=[textbox], value="Clear Text")
    clear_button.click(fn=on_clear, outputs=message)

demo.launch()
```
📌 **Explanation:**  
- The **ClearButton** clears the `textbox` when clicked.  
- Additionally, it **updates** the `message` textbox to display `"Cleared!"`.

---

## **Final Thoughts**  
- `gr.ClearButton` is a **simple but powerful** component for clearing inputs in Gradio apps.  
- It can **reset multiple fields**, work with **event listeners**, and even trigger **custom functions** on click.  
- Its flexible parameters allow customization of **size, visibility, icons, and interactivity**.

Let me know if you need further refinements! 🚀