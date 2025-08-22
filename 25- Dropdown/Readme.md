
---

# **`gradio.Dropdown`**
`gradio.Dropdown(...)`

### **Description**  
Creates a **dropdown menu** that allows users to **select one or multiple options** as input or display a selected value as output.

---

## **Behavior**  
### **As an Input Component**  
- Passes the selected value as **`str` | `int` | `float`**, or its index as **`int`**.  
- If `multiselect=True`, it passes a **list** of selected values or indices.  
- Your function should accept:

```python
def predict(value: str | int | float | list[str | int | float] | list[int | None] | None):
    ...
```

### **As an Output Component**  
- Expects a **single value** (`str` | `int` | `float`) corresponding to the dropdown selection.  
- If `multiselect=True`, expects a **list** of selected values.  
- Your function should return:

```python
def predict(...) -> str | int | float | list[str | int | float] | None:
    ...
    return value
```

---

## **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `choices` | `list[str | int | float | tuple[str, str | int | float]] | None` | List of choices to display |
| `value` | `str | int | float | list[str | int | float] | Callable | DefaultValue | None` | Default selected value |
| `type` | `"value"` \| `"index"` | Whether to return selected value or index |
| `multiselect` | `bool | None` | Allows selecting multiple values |
| `allow_custom_value` | `bool` | Allows users to enter custom values |
| `max_choices` | `int | None` | Max number of choices selectable when `multiselect=True` |
| `filterable` | `bool` | Enables search/filter functionality |
| `label` | `str | None` | Label for the dropdown |
| `info` | `str | None` | Additional info or tooltip text |
| `every` | `Timer | float | None` | Refresh interval for updates |
| `show_label` | `bool | None` | Whether to display the label |
| `container` | `bool` | Whether to wrap the component in a container |
| `scale` | `int | None` | Scaling factor |
| `min_width` | `int` | Minimum width of the dropdown |
| `interactive` | `bool | None` | Enables user interaction |
| `visible` | `bool` | Whether the dropdown is visible |
| `render` | `bool` | Whether to render the dropdown |
| `key` | `int | str | None` | Unique identifier for the component |

---

## **Shortcuts**
| Class | Interface String Shortcut | Initialization |
|-------|----------------|-----------------|
| `gradio.Dropdown` | `"dropdown"` | Uses default values |

---

## **Example: Dynamic Sentence Builder**
This example demonstrates **multiple dropdown selections** used to build a sentence dynamically.

```python
import gradio as gr

def sentence_builder(quantity, animal, countries, place, activity_list, morning):
    return f"""The {quantity} {animal}s from {" and ".join(countries)} went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""

demo = gr.Interface(
    sentence_builder,
    [
        gr.Slider(2, 20, value=4, label="Count", info="Choose between 2 and 20"),
        gr.Dropdown(["cat", "dog", "bird"], label="Animal", info="Will add more animals later!"),
        gr.CheckboxGroup(["USA", "Japan", "Pakistan"], label="Countries", info="Where are they from?"),
        gr.Radio(["park", "zoo", "road"], label="Location", info="Where did they go?"),
        gr.Dropdown(
            ["ran", "swam", "ate", "slept"], 
            value=["swam", "slept"], 
            multiselect=True, 
            label="Activity", 
            info="Choose multiple activities."
        ),
        gr.Checkbox(label="Morning", info="Did they do it in the morning?"),
    ],
    "text",
    examples=[
        [2, "cat", ["Japan", "Pakistan"], "park", ["ate", "swam"], True],
        [4, "dog", ["Japan"], "zoo", ["ate", "swam"], False],
        [10, "bird", ["USA", "Pakistan"], "road", ["ran"], False],
        [8, "cat", ["Pakistan"], "zoo", ["ate"], True],
    ]
)

if __name__ == "__main__":
    demo.launch()
```

---

## **Event Listeners**
| Listener | Description |
|----------|------------|
| `Dropdown.change(fn, ···)` | Triggered when the dropdown value changes (either from user input or function update). |
| `Dropdown.input(fn, ···)` | Triggered **only** when the user changes the value manually. |
| `Dropdown.select(fn, ···)` | Triggered when the user **selects or deselects** an option. |
| `Dropdown.focus(fn, ···)` | Triggered when the dropdown **gains focus**. |
| `Dropdown.blur(fn, ···)` | Triggered when the dropdown **loses focus**. |
| `Dropdown.key_up(fn, ···)` | Triggered when the user **presses a key** while the dropdown is focused. |

### **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable | None | "decorator"` | Function triggered on event |
| `inputs` | `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None` | Inputs to the function |
| `outputs` | `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None` | Outputs from the function |
| `queue` | `bool` | Whether to queue function execution |
| `batch` | `bool` | Whether to batch inputs |
| `preprocess` | `bool` | Whether to preprocess input before passing to function |
| `postprocess` | `bool` | Whether to postprocess output before displaying |
| `concurrency_limit` | `int | None | "default"` | Maximum concurrent executions |

---

 