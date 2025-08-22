
---

## `gradio.Dataframe`
`gradio.Dataframe(...)`

### **Description**
This component displays a table similar to a spreadsheet. It can be used:
- **As an input component:** To collect structured data from the user.
- **As an output component:** To display structured data.

### **Behavior**
#### **As an input component:**
Passes the uploaded spreadsheet data as one of the following formats:
- `pandas.DataFrame`
- `numpy.array`
- `polars.DataFrame`
- Native 2D Python `list[list]`

Example function signature:
```python
def predict(value: pd.DataFrame | np.ndarray | pl.DataFrame | list[list]):
    ...
```

#### **As an output component:**
Expects data in one of the following formats:
- `pandas.DataFrame`
- `pandas.Styler`
- `numpy.array`
- `polars.DataFrame`
- `list[list]`
- `list`
- `dict` (with keys `"data"` and optionally `"headers"`)
- `str` (path to a CSV file)

Example function signature:
```python
def predict(...) -> pd.DataFrame | Styler | np.ndarray | pl.DataFrame | list | list[list] | dict | str | None:
    ...
    return value
```

---

### **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `pd.DataFrame` \| `Styler` \| `np.ndarray` \| `pl.DataFrame` \| `list` \| `list[list]` \| `dict` \| `str` \| `Callable` \| `None` | The initial value of the dataframe |
| `headers` | `list[str]` \| `None` | Column headers |
| `row_count` | `int` \| `tuple[int, str]` | Number of rows (fixed or flexible) |
| `col_count` | `int` \| `tuple[int, str]` \| `None` | Number of columns (fixed or flexible) |
| `datatype` | `str` \| `list[str]` | Type of data in each column |
| `type` | `"pandas"` \| `"numpy"` \| `"array"` \| `"polars"` | Type of data structure |
| `label` | `str` \| `None` | Label for the dataframe |
| `interactive` | `bool` \| `None` | If `True`, allows user editing |
| `visible` | `bool` | Whether the component is visible |
| `render` | `bool` | Whether to render the component |
| `wrap` | `bool` | Whether to wrap text in cells |
| `column_widths` | `list[str | int]` \| `None` | Column widths |

---

### **Shortcuts**
| Class | Interface String Shortcut | Initialization |
|-------|----------------|-----------------|
| `gradio.Dataframe` | `"dataframe"` | Uses default values |
| `gradio.Numpy` | `"numpy"` | Uses `type="numpy"` |
| `gradio.Matrix` | `"matrix"` | Uses `type="array"` |
| `gradio.List` | `"list"` | Uses `type="array", col_count=1` |

---

### **Example**
```python
import gradio as gr
import pandas as pd

def filter_records(records, gender):
    return records[records["gender"] == gender]

demo = gr.Interface(
    fn=filter_records,
    inputs=[
        gr.Dataframe(
            headers=["name", "age", "gender"],
            datatype=["str", "number", "str"],
            row_count=5,
            col_count=(3, "fixed"),
        ),
        gr.Dropdown(["M", "F", "O"]),
    ],
    outputs="dataframe",
    description="Enter gender as 'M', 'F', or 'O' for other.",
)

if __name__ == "__main__":
    demo.launch()
```

---

### **Event Listeners**
| Listener | Description |
|----------|------------|
| `Dataframe.change(fn, ···)` | Triggered when the Dataframe value changes (either via user input or function update) |
| `Dataframe.input(fn, ···)` | Triggered when the user changes the Dataframe value |
| `Dataframe.select(fn, ···)` | Triggered when the user selects or deselects the Dataframe |

#### **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable` \| `None` \| `"decorator"` | Function to trigger on the event |
| `inputs` | `Component` \| `BlockContext` \| `list[Component | BlockContext]` \| `Set[Component | BlockContext]` \| `None` | Inputs to the function |
| `outputs` | `Component` \| `BlockContext` \| `list[Component | BlockContext]` \| `Set[Component | BlockContext]` \| `None` | Outputs from the function |
| `queue` | `bool` | Whether to queue function execution |
| `batch` | `bool` | Whether to batch inputs |

---
 