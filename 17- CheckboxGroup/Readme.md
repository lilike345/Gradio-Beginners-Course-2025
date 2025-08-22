### **Gradio CheckboxGroup**

#### **Introduction**
The `gradio.CheckboxGroup` component in Gradio allows users to select multiple options from a predefined list of checkboxes. This component can be used both as an **input**, passing selected values into a function, and as an **output**, displaying selected values from a function.

---

## **Functionality & Behavior**
### **As an Input Component**
- When used as an input, `CheckboxGroup` passes the list of selected checkboxes to the function.
- The function receives these selected values either as:
  - A list of strings, integers, or floats (`list[str | int | float]`).
  - A list of indices corresponding to the selected checkboxes (`list[int]`).

#### **Example Function Signature (Input)**
```python
def predict(value: list[str | int | float] | list[int | None]):
    ...
```

---

### **As an Output Component**
- When used as an output, the function should return:
  - A list of values (`list[str | int | float]`) representing the checkboxes to be marked as checked.
  - A single value (`str | int | float`) for marking a single checkbox.
  - `None` if no checkbox should be selected.

#### **Example Function Signature (Output)**
```python
def predict(···) -> list[str | int | float] | str | int | float | None:
    return value
```

---

## **Initialization Parameters**
The `CheckboxGroup` component offers various initialization parameters that control its behavior and appearance.

| Parameter | Type | Description |
|-----------|------|-------------|
| `choices` | `list[str | int | float | tuple[str, str | int | float]] | None` | List of available checkbox options. Each item can be a string, number, or a tuple (label, value). |
| `value` | `list[str | float | int] | str | float | int | Callable | None` | Default selected values when the component is initialized. |
| `type` | `Literal['value', 'index']` | Determines whether the selected values should be passed as values (`value`) or indices (`index`). |
| `label` | `str | None` | Display label for the component. |
| `info` | `str | None` | Additional descriptive text. |
| `every` | `Timer | float | None` | Sets an interval for automatic updates. |
| `inputs` | `Component | list[Component] | set[Component] | None` | Components used as inputs for this component. |
| `show_label` | `bool | None` | Whether to show the label. |
| `container` | `bool` | Whether to display in a container. |
| `scale` | `int | None` | Determines how much space the component occupies relative to others. |
| `min_width` | `int` | Minimum width of the component. |
| `interactive` | `bool | None` | Whether users can interact with the checkboxes. |
| `visible` | `bool` | Whether the component is visible. |
| `elem_id` | `str | None` | Custom HTML ID for CSS styling. |
| `elem_classes` | `list[str] | str | None` | Custom CSS classes. |
| `render` | `bool` | Whether the component should be rendered immediately. |
| `key` | `int | str | None` | Unique key identifier. |

---

## **Shortcuts**
- **Class Name**: `gradio.CheckboxGroup`
- **Interface String Shortcut**: `"checkboxgroup"`

---

## **Demo Example: Sentence Builder**
The following example demonstrates the `CheckboxGroup` component in a Gradio app that constructs sentences based on user selections.

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
        gr.Dropdown(["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity"),
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
Event listeners allow functions to be triggered when a user interacts with the `CheckboxGroup` component.

### **Supported Listeners**
| Listener | Description |
|----------|------------|
| `CheckboxGroup.change(fn, ···)` | Fires when the value of the `CheckboxGroup` changes due to user interaction or programmatic updates. |
| `CheckboxGroup.input(fn, ···)` | Fires when the user directly changes the `CheckboxGroup` selection. |
| `CheckboxGroup.select(fn, ···)` | Fires when a user selects or deselects a checkbox. Uses `gradio.SelectData` to carry event data. |

---

## **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable | None | Literal['decorator']` | The function to execute when the event occurs. |
| `inputs` | `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None` | Input components affected by the event. |
| `outputs` | `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None` | Output components affected by the event. |
| `api_name` | `str | None | Literal[False]` | API name for the function call. |
| `scroll_to_output` | `bool` | Whether the page should scroll to the output component upon execution. |
| `show_progress` | `Literal['full', 'minimal', 'hidden']` | Controls the display of the execution progress bar. |
| `queue` | `bool` | Whether the event should be queued. |
| `batch` | `bool` | Enables batch processing for the event. |
| `max_batch_size` | `int` | Maximum batch size if batch processing is enabled. |
| `preprocess` | `bool` | Whether to apply preprocessing before executing the function. |
| `postprocess` | `bool` | Whether to apply postprocessing after execution. |
| `cancels` | `dict[str, Any] | list[dict[str, Any]] | None` | Specifies event cancellation behavior. |
| `trigger_mode` | `Literal['once', 'multiple', 'always_last'] | None` | Determines when the function should be triggered. |
| `js` | `str | None` | JavaScript function to run when the event is triggered. |
| `concurrency_limit` | `int | None | Literal['default']` | Limits the number of concurrent executions. |
| `concurrency_id` | `str | None` | Unique identifier for concurrency tracking. |
| `show_api` | `bool` | Whether to show API details for the function. |
| `time_limit` | `int | None` | Execution time limit in seconds. |
| `stream_every` | `float` | Time interval for streaming responses. |
| `like_user_message` | `bool` | Whether to treat the response as a user message. |

---

## **Conclusion**
The `CheckboxGroup` component in Gradio is a versatile tool for handling multiple selections. Whether used for user input, displaying selections dynamically, or triggering event-driven functions, it provides a powerful and flexible way to enhance interactive applications.