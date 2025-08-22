### `gradio.Checkbox`  

#### **Description**  
The `gradio.Checkbox` component creates a checkbox that can be toggled between `True` and `False`. It can be used as an **input** to pass a boolean value to a function or as an **output** to display a boolean value.

---

### **Behavior**
- **As an input component:** Passes the status of the checkbox as a `bool`.  
  ✅ Example function signature:  
  ```python
  def predict(value: bool | None):
      ...
  ```
- **As an output component:** Expects a `bool` value to set the checkbox status.  
  ✅ Example function return type:  
  ```python
  def predict(...) -> bool | None:
      ...
      return value
  ```

---

### **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `bool | Callable` | Default value of the checkbox (`True` or `False`). |
| `label` | `str | None` | Label displayed next to the checkbox. |
| `info` | `str | None` | Tooltip text displayed when hovering over the component. |
| `every` | `Timer | float | None` | Runs the function at a set interval. |
| `inputs` | `Component | list[Component] | set[Component] | None` | Input components linked to the checkbox. |
| `show_label` | `bool | None` | Whether to show the label. |
| `container` | `bool` | Whether to wrap the component in a container. |
| `scale` | `int | None` | Defines relative width of the component. |
| `min_width` | `int` | Minimum width of the component in pixels. |
| `interactive` | `bool | None` | Enables user interaction. |
| `visible` | `bool` | Whether to show the checkbox. |
| `elem_id` | `str | None` | Custom HTML element ID. |
| `elem_classes` | `list[str] | str | None` | Custom CSS classes. |
| `render` | `bool` | If `False`, prevents rendering of the component. |
| `key` | `int | str | None` | Unique identifier for state management. |

---

### **Shortcuts**
| **Class** | **Shortcut** | **Description** |
|-----------|--------------|---------------|
| `gradio.Checkbox` | `"checkbox"` | Uses default values. |

---

### **Example Usage**
```python
import gradio as gr

def sentence_builder(quantity, animal, countries, place, activity_list, morning):
    return f"The {quantity} {animal}s from {', '.join(countries)} went to the {place} where they {' and '.join(activity_list)} until the {'morning' if morning else 'night'}."

demo = gr.Interface(
    sentence_builder,
    [
        gr.Slider(2, 20, value=4, label="Count"),
        gr.Dropdown(["cat", "dog", "bird"], label="Animal"),
        gr.CheckboxGroup(["USA", "Japan", "Pakistan"], label="Countries"),
        gr.Radio(["park", "zoo", "road"], label="Location"),
        gr.Dropdown(["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity"),
        gr.Checkbox(label="Morning", info="Did they do it in the morning?"),
    ],
    "text",
    examples=[
        [2, "cat", ["Japan", "Pakistan"], "park", ["ate", "swam"], True],
        [4, "dog", ["Japan"], "zoo", ["ate", "swam"], False],
    ]
)

if __name__ == "__main__":
    demo.launch()
```

---

### **Event Listeners**
Event listeners allow the `gradio.Checkbox` to trigger actions when its value changes.

| **Listener** | **Description** |
|-------------|----------------|
| `Checkbox.change(fn, ···)` | Triggers when the checkbox state changes (either by user input or programmatically). |
| `Checkbox.input(fn, ···)` | Triggers only when the user manually changes the checkbox. |
| `Checkbox.select(fn, ···)` | Triggers when the checkbox is selected or deselected. Uses `gradio.SelectData`. |

#### **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable | None | 'decorator'` | Function to execute when the event is triggered. |
| `inputs` | `Component | list[Component] | None` | Input components linked to the event. |
| `outputs` | `Component | list[Component] | None` | Output components affected by the event. |
| `queue` | `bool` | Whether to queue the event execution. |
| `batch` | `bool` | Enables batch processing. |
| `scroll_to_output` | `bool` | Automatically scrolls to output when triggered. |

---

 