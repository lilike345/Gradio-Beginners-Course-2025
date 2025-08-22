## 📌 **`gradio.Slider`**  

### 🔹 **Description:**  
Creates a slider component that allows users to select a value within a specified range.  

### 🔹 **Behavior:**  
- **As Input Component:** Passes slider value as a `float` into the function.  
- **As Output Component:** Accepts an `int` or `float` and updates the slider value, provided it is within range.  

---

### 🔹 **Example Usage:**
#### ✅ **Basic Slider for Numeric Input**
```python
import gradio as gr

def square(num):
    return num ** 2  # Return square of the input number

gr.Interface(
    fn=square,
    inputs=gr.Slider(minimum=1, maximum=100, value=10, step=1, label="Choose a number"),
    outputs=gr.Textbox(label="Squared Value")
).launch()
```

#### ✅ **Controlling Text Size with a Slider**
```python
def change_text_size(size):
    return f"<p style='font-size:{size}px;'>This text is {size}px large!</p>"

gr.Interface(
    fn=change_text_size,
    inputs=gr.Slider(minimum=10, maximum=100, value=20, step=5, label="Font Size"),
    outputs=gr.HTML()
).launch()
```

---

### 🔹 **Initialization Parameters:**  
| Parameter | Type | Description |
|-----------|------|-------------|
| `minimum` | `float` | Minimum slider value |
| `maximum` | `float` | Maximum slider value |
| `value` | `float | Callable | None` | Default slider value |
| `step` | `float | None` | Step size for increments |
| `label` | `str | None` | Label for the slider |
| `info` | `str | None` | Additional information about the slider |
| `every` | `Timer | float | None` | Auto-refresh interval |
| `inputs` | `Component | list[Component] | set[Component] | None` | Input dependencies |
| `show_label` | `bool | None` | Display label or not |
| `container` | `bool` | Wrap in a container |
| `scale` | `int | None` | Relative size compared to other components |
| `min_width` | `int` | Minimum width of the slider |
| `interactive` | `bool | None` | Allows user interaction if `True` |
| `visible` | `bool` | Whether the slider is visible |
| `elem_id` | `str | None` | Custom HTML element ID |
| `elem_classes` | `list[str] | str | None` | Custom CSS classes |
| `render` | `bool` | Whether the component is rendered |
| `key` | `int | str | None` | Unique identifier |
| `randomize` | `bool` | Randomize default value on each run |

---

### 🔹 **Event Listeners:**  
| Listener | Description |
|----------|-------------|
| `.change(fn, ...)` | Triggered when the slider value changes due to user input or function updates. |
| `.input(fn, ...)` | Triggered only when the user interacts with the slider. |
| `.release(fn, ...)` | Triggered when the user releases the mouse after changing the slider. |

---
