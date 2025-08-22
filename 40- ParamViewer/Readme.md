### ParamViewer Component

#### `gradio.ParamViewer(···)`

##### Description
The `gradio.ParamViewer` component displays an interactive table of parameters, their descriptions, types, and default values, with syntax highlighting. It is primarily used for documentation purposes and does **not** accept user input. 

Internally, this component is used in the [Custom Component Gallery](https://www.gradio.app/custom-components/gallery) to showcase the parameters of various components.

##### Behavior
- **As an Input Component** (Rarely used):  
  - Passes a dictionary `{str: dict}` where:
    - The **keys** are parameter names.
    - The **values** are dictionaries with the keys:
      - `"type"` (type of the parameter, e.g., `str`).
      - `"description"` (human-readable explanation).
      - `"default"` (default value).

  **Example function signature:**
  ```python
  def predict(value: dict[str, dict]) -> None:
      ...
  ```

- **As an Output Component**:  
  - Expects a dictionary `{str: dict}` with the same format as above.

  **Example function signature:**
  ```python
  def predict(···) -> dict[str, dict]:
      ...
      return value
  ```

---

### Initialization Parameters

| Parameter     | Type                                     | Description |
|--------------|------------------------------------------|-------------|
| `value`      | `dict[str, dict] | None`                 | Dictionary defining parameters, their types, descriptions, and default values. |
| `language`   | `Literal['python', 'typescript']`        | Syntax highlighting language for the parameter table. |
| `linkify`    | `list[str] | None`                       | List of keys that should be displayed as hyperlinks. |
| `every`      | `Timer | float | None`                   | Interval between updates. |
| `inputs`     | `Component | list[Component] | set[Component] | None` | Inputs for the component. |
| `render`     | `bool`                                   | Whether the component should be rendered. |
| `key`        | `int | str | None`                       | Unique key for referencing the component. |
| `header`     | `str | None`                             | Header text displayed at the top of the component. |

---

### Shortcuts
- **Class:** `gradio.ParamViewer`
- **Interface String Shortcut:** `"paramviewer"`
- **Initialization:** Uses default values.

---

### Example Usage

```python
import gradio as gr

# Example dictionary containing parameter details
parameters = {
    "learning_rate": {
        "type": "float",
        "description": "The step size used for updating weights in optimization.",
        "default": 0.01
    },
    "batch_size": {
        "type": "int",
        "description": "The number of training samples used in each batch.",
        "default": 32
    },
    "num_epochs": {
        "type": "int",
        "description": "The total number of passes through the dataset.",
        "default": 10
    }
}

# Create a Gradio ParamViewer component
demo = gr.Interface(
    lambda: parameters,  # Function returning the parameter dictionary
    inputs=[],
    outputs=gr.ParamViewer(language="python", header="Model Hyperparameters")
)

demo.launch()
```

---

### Event Listeners

Event listeners allow you to trigger functions based on user interactions with the `ParamViewer` component.

| Listener                  | Description |
|---------------------------|-------------|
| `ParamViewer.change(fn, ···)`  | Triggered when the value of the `ParamViewer` changes (e.g., an update from another function). |
| `ParamViewer.upload(fn, ···)`  | Triggered when the user uploads a file into the `ParamViewer`. |

---

### Event Parameters

| Parameter         | Type  | Description |
|------------------|------------------------------------------------------|-------------|
| `fn`            | `Callable | None | Literal['decorator']`              | The function to be triggered by the event. |
| `inputs`        | `Component | BlockContext | list[Component | BlockContext] | set[Component | BlockContext] | None` | The input components. |
| `outputs`       | `Component | BlockContext | list[Component | BlockContext] | set[Component | BlockContext] | None` | The output components. |
| `api_name`      | `str | None | Literal[False]`                        | Name of the API for the event. |
| `scroll_to_output` | `bool`                                           | Whether to scroll to the output after the event. |
| `show_progress` | `Literal['full', 'minimal', 'hidden']`               | Progress bar display setting. |
| `queue`         | `bool`                                              | Whether to queue the event. |
| `batch`         | `bool`                                              | Whether to batch process the event. |
| `max_batch_size` | `int`                                              | Maximum number of items in a batch. |
| `preprocess`    | `bool`                                              | Whether to preprocess inputs before triggering. |
| `postprocess`   | `bool`                                              | Whether to postprocess outputs after triggering. |

---

### Summary
- `gradio.ParamViewer` is a **read-only** interactive parameter table.
- It is **not commonly used** as an input component.
- Displays **parameter names, types, descriptions, and default values**.
- Supports **syntax highlighting** (Python or TypeScript).
- Has event listeners for **updates and file uploads**.

Would you like an example where `ParamViewer` dynamically updates based on another input component? 🚀