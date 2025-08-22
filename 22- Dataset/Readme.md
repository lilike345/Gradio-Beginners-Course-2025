
---

# `gradio.Dataset`
`gradio.Dataset(...)`

### **Description**  
Creates a **gallery** or **table** to display data samples. Primarily designed for **internal use** to showcase examples, but it can also be used to display datasets and let users **select examples**.

---

## **Behavior**  
### **As an Input Component**  
- Passes the selected sample in one of the following formats:
  - **`"value"`** → Returns a list of data corresponding to each input component.  
  - **`"index"`** → Returns an `int` index of the selected sample.  
  - **`"tuple"`** → Returns a tuple `(index, data)`.  

Your function should accept one of these types:
```python
def predict(value: int | list | None):
    ...
```

### **As an Output Component**  
- Expects an `int` index or a `list` of sample data.  
- Returns the **index of the sample** in the dataset or `None` if the sample is not found.

Your function should return:
```python
def predict(...) -> list[list]:
    ...
    return value
```

---

## **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `str` \| `None` | Label of the dataset |
| `show_label` | `bool` | Whether to display the label |
| `components` | `list[Component]` \| `list[str]` \| `None` | Components for displaying dataset items |
| `component_props` | `list[dict[str, Any]]` \| `None` | Additional properties for each component |
| `samples` | `list[list[Any]]` \| `None` | The dataset samples to display |
| `headers` | `list[str]` \| `None` | Column headers (if displaying as a table) |
| `type` | `"values"` \| `"index"` \| `"tuple"` | Determines the format in which the dataset passes data |
| `layout` | `"gallery"` \| `"table"` \| `None` | Determines if data is displayed in a **gallery** or a **table** |
| `samples_per_page` | `int` | Number of samples displayed per page |
| `visible` | `bool` | Whether the component is visible |
| `render` | `bool` | Whether to render the component |
| `key` | `int` \| `str` \| `None` | Unique identifier for component |
| `container` | `bool` | Whether to wrap dataset in a container |
| `scale` | `int` \| `None` | Scale factor for the component |
| `proxy_url` | `str` \| `None` | Optional proxy URL for dataset items |
| `sample_labels` | `list[str]` \| `None` | Labels for each sample in the dataset |

---

## **Shortcuts**
| Class | Interface String Shortcut | Initialization |
|-------|----------------|-----------------|
| `gradio.Dataset` | `"dataset"` | Uses default values |

---

## **Example: Updating a Dataset**
This example **displays a text dataset** using `gr.Dataset` and updates it when a user clicks a button.

```python
import gradio as gr

philosophy_quotes = [
    ["I think, therefore I am."],
    ["The unexamined life is not worth living."]
]

startup_quotes = [
    ["Ideas are easy. Implementation is hard."],
    ["Make mistakes faster."]
]

def show_startup_quotes():
    return gr.Dataset(samples=startup_quotes)

with gr.Blocks() as demo:
    textbox = gr.Textbox()
    dataset = gr.Dataset(components=[textbox], samples=philosophy_quotes)
    button = gr.Button()

    button.click(show_startup_quotes, None, dataset)

demo.launch()
```

---

## **Event Listeners**
| Listener | Description |
|----------|------------|
| `Dataset.click(fn, ···)` | Triggered when the **Dataset is clicked**. |
| `Dataset.select(fn, ···)` | Triggered when the **user selects or deselects** the Dataset. Uses `gradio.SelectData` to store the event data. |

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

 