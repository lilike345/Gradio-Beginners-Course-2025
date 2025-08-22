
---

# **`gradio.DateTime`**
`gradio.DateTime(...)`

### **Description**  
A component for selecting a **date** and **(optionally) time**.

---

## **Behavior**  
### **As an Input Component**  
- Passes the selected date/time as a **string (`str`)** into the function.  
- Your function should accept one of the following types:

```python
def predict(value: float | datetime | str | None):
    ...
```

### **As an Output Component**  
- Expects a **tuple pair of datetimes**.  
- Your function should return one of these types:

```python
def predict(...) -> float | datetime | str | None:
    ...
    return value
```

---

## **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `float` \| `str` \| `datetime` \| `None` | Initial value of the DateTime component |
| `include_time` | `bool` | Whether to include time selection |
| `type` | `"timestamp"` \| `"datetime"` \| `"string"` | Format of the output value |
| `timezone` | `str` \| `None` | Timezone for display and conversion |
| `label` | `str` \| `None` | Label for the component |
| `show_label` | `bool` \| `None` | Whether to show the label |
| `info` | `str` \| `None` | Additional information displayed below the component |
| `every` | `float` \| `None` | Refresh interval in seconds |
| `scale` | `int` \| `None` | Scaling factor |
| `min_width` | `int` | Minimum width of the component |
| `visible` | `bool` | Whether the component is visible |
| `interactive` | `bool` \| `None` | If `True`, allows user interaction |
| `render` | `bool` | Whether to render the component |
| `key` | `int` \| `str` \| `None` | Unique identifier for the component |

---

## **Shortcuts**
| Class | Interface String Shortcut | Initialization |
|-------|----------------|-----------------|
| `gradio.DateTime` | `"datetime"` | Uses default values |

---

## **Example: Using `DateTime` in a Gradio Interface**
This example demonstrates how to create a **DateTime selector** and display the selected date/time.

```python
import gradio as gr
from datetime import datetime

def show_datetime(value):
    return f"Selected Date & Time: {value}"

with gr.Blocks() as demo:
    datetime_picker = gr.DateTime(include_time=True, type="datetime")
    output_text = gr.Textbox()

    datetime_picker.change(show_datetime, inputs=datetime_picker, outputs=output_text)

demo.launch()
```

---

## **Event Listeners**
| Listener | Description |
|----------|------------|
| `DateTime.change(fn, ···)` | Triggered when the **value of the DateTime changes** (either due to user input or a function update). |
| `DateTime.submit(fn, ···)` | Triggered when the **user presses Enter** while the DateTime field is focused. |

### **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable` \| `None` \| `"decorator"` | Function triggered on event |
| `inputs` | `Component` \| `BlockContext` \| `list[Component | BlockContext]` \| `Set[Component | BlockContext]` \| `None` | Inputs to the function |
| `outputs` | `Component` \| `BlockContext` \| `list[Component | BlockContext]` \| `Set[Component | BlockContext]` \| `None` | Outputs from the function |
| `queue` | `bool` | Whether to queue function execution |
| `batch` | `bool` | Whether to batch inputs |
| `preprocess` | `bool` | Whether to preprocess input before passing to function |
| `postprocess` | `bool` | Whether to postprocess output before displaying |
| `concurrency_limit` | `int` \| `None` \| `"default"` | Maximum concurrent executions |

---

 