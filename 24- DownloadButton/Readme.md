
---

# **`gradio.DownloadButton`**
`gradio.DownloadButton(...)`

### **Description**  
A button that allows users to **download a single file** of any type when clicked.

---

## **Behavior**  
### **As an Input Component**  
- **(Rarely used)**  
- Passes the file **as a string (`str`)** into the function.  
- Your function should accept:

```python
def predict(value: str | None):
    ...
```

### **As an Output Component**  
- Expects a **string (`str`) or `Path`** file path.  
- Your function should return one of the following:

```python
def predict(...) -> str | Path | None:
    ...
    return value
```

---

## **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `str` | Label for the button |
| `value` | `str` \| `Path` \| `Callable` \| `None` | The file to be downloaded |
| `every` | `Timer` \| `float` \| `None` | Refresh interval for updates |
| `inputs` | `Component` \| `list[Component]` \| `set[Component]` \| `None` | Components used as input |
| `variant` | `"primary"` \| `"secondary"` \| `"stop"` | Button style variant |
| `visible` | `bool` | Whether the button is visible |
| `size` | `"sm"` \| `"md"` \| `"lg"` | Size of the button |
| `icon` | `str` \| `None` | Icon for the button |
| `scale` | `int` \| `None` | Scaling factor |
| `min_width` | `int` \| `None` | Minimum width of the button |
| `interactive` | `bool` | If `True`, enables interaction |
| `render` | `bool` | Whether to render the button |
| `key` | `int` \| `str` \| `None` | Unique identifier for the component |

---

## **Shortcuts**
| Class | Interface String Shortcut | Initialization |
|-------|----------------|-----------------|
| `gradio.DownloadButton` | `"downloadbutton"` | Uses default values |

---

## **Example: Upload and Download a File**
This example demonstrates how to **upload a file** and then **download it** after processing.

```python
from pathlib import Path
import gradio as gr

def upload_file(filepath):
    name = Path(filepath).name
    return [gr.UploadButton(visible=False), gr.DownloadButton(label=f"Download {name}", value=filepath, visible=True)]

def download_file():
    return [gr.UploadButton(visible=True), gr.DownloadButton(visible=False)]

with gr.Blocks() as demo:
    gr.Markdown("First upload a file, then download it (only once!)")

    with gr.Row():
        upload_btn = gr.UploadButton("Upload a file", file_count="single")
        download_btn = gr.DownloadButton("Download the file", visible=False)

    upload_btn.upload(upload_file, upload_btn, [upload_btn, download_btn])
    download_btn.click(download_file, None, [upload_btn, download_btn])

if __name__ == "__main__":
    demo.launch()
```

---

## **Event Listeners**
| Listener | Description |
|----------|------------|
| `DownloadButton.click(fn, ···)` | Triggered when the **DownloadButton is clicked**. |

### **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable` \| `None` \| `"decorator"` | Function triggered on click |
| `inputs` | `Component` \| `BlockContext` \| `list[Component | BlockContext]` \| `Set[Component | BlockContext]` \| `None` | Inputs to the function |
| `outputs` | `Component` \| `BlockContext` \| `list[Component | BlockContext]` \| `Set[Component | BlockContext]` \| `None` | Outputs from the function |
| `queue` | `bool` | Whether to queue function execution |
| `batch` | `bool` | Whether to batch inputs |
| `preprocess` | `bool` | Whether to preprocess input before passing to function |
| `postprocess` | `bool` | Whether to postprocess output before displaying |
| `concurrency_limit` | `int` \| `None` \| `"default"` | Maximum concurrent executions |

---

 