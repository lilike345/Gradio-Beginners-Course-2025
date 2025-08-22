

---

# 📌 **Gradio `Radio` Component**

### 📝 **Description**
The `gr.Radio` component creates a set of radio buttons from which the user can select **only one** option. The options can be **strings, integers, or floats**.

### 🔄 **Behavior**
#### ✅ **As an Input Component**
- **Passes:** The selected value (`str | int | float`) or the **index** of the selected option (`int`) into the function.
- **Function signature:**
  ```python
  def predict(value: str | int | float | None):
      ...
  ```
#### 📤 **As an Output Component**
- **Receives:** A `str`, `int`, or `float`, corresponding to the selected radio button.
- **Function signature:**
  ```python
  def predict(...) -> str | int | float | None:
      ...
      return value
  ```

---

## ⚙️ **Initialization Parameters**
| Parameter        | Type | Description |
|-----------------|------|-------------|
| `choices` | `list[str | int | float | tuple[str, str | int | float]]` | Options for the radio buttons. Each option can be a string, integer, float, or a tuple where the first item is the label. |
| `value` | `str | int | float | Callable | None` | Default selected value. |
| `type` | `"value"` or `"index"` | If `"value"`, the selected value is passed; if `"index"`, the index of the selection is passed. |
| `label` | `str | None` | Label for the radio group. |
| `info` | `str | None` | Additional description for the radio group. |
| `interactive` | `bool | None` | If `True`, allows user input. |
| `visible` | `bool` | If `False`, hides the component. |
| `key` | `int | str | None` | Unique key for component state. |

📌 **Shortcut for Initialization**  
- Class: `gradio.Radio`
- Interface String: `"radio"`
- Example:
  ```python
  radio = gr.Radio(["Option 1", "Option 2", "Option 3"], label="Select an option")
  ```

---

## 🎛 **Event Listeners**
| Listener | Description |
|----------|-------------|
| **`Radio.select(fn, ...)`** | Triggered when the user selects or deselects a radio button. Returns event data (`gr.SelectData`). |
| **`Radio.change(fn, ...)`** | Triggered when the selected value changes, either by user input or function update. |
| **`Radio.input(fn, ...)`** | Triggered **only** when the user **manually** changes the value. |

### 🎯 **Event Data Structure (`gr.SelectData`)**
```python
{
    "value": "<selected_label>",  # The selected label
    "selected": True              # Whether the radio button is selected
}
```

---

## 🔧 **Example: Radio Button in Action**
```python
import gradio as gr

def sentence_builder(quantity, animal, countries, place, activity_list, morning):
    return f"""The {quantity} {animal}s from {" and ".join(countries)} went to the {place} 
    where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}."""

# Define UI components
demo = gr.Interface(
    sentence_builder,
    [
        gr.Slider(2, 20, value=4, label="Count"),
        gr.Dropdown(["cat", "dog", "bird"], label="Animal"),
        gr.CheckboxGroup(["USA", "Japan", "Pakistan"], label="Countries"),
        gr.Radio(["park", "zoo", "road"], label="Location"),  # Radio Component
        gr.Dropdown(["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity"),
        gr.Checkbox(label="Morning"),
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

## 🚀 **Key Takeaways**
- `gr.Radio` allows only **one selection** at a time.
- Can accept **strings, integers, or floats** as choices.
- Supports event listeners like **select, change, and input**.
- Use the `type` parameter to return **either the value or index** of the selected choice.

Would you like me to integrate this into a larger **Gradio-based UI**? 🚀