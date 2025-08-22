# **`gradio.File`**
`gradio.File(...)`

---

## **Description**  
Creates a **file upload/download** component that allows:  
- **Uploading** one or more files (as input).  
- **Displaying/download** of file(s) or URLs (as output).  

### **Demo Examples**  
- [zip_files](https://huggingface.co/spaces/gradio/zip_files)  
- [zip_to_json](https://huggingface.co/spaces/gradio/zip_to_json)  

---

## **Behavior**  

### **As an Input Component**  
- Passes the file(s) as either:  
  - `str` (file path)  
  - `bytes` (file content)  
  - `list[str]` (multiple file paths)  
  - `list[bytes]` (multiple file contents)  
  - `None` (if no file uploaded)  

- Your function should accept:

```python
def predict(value: bytes | str | list[bytes] | list[str] | None):
    ...
```

### **As an Output Component**  
- Expects either:  
  - `str` (single file path or URL)  
  - `list[str]` (multiple file paths or URLs)  
  - `None` (if no file to display)  

- Your function should return:

```python
def predict(...) -> str | list[str] | None:
    ...
    return value
```

---

## **Initialization Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `value` | `str | list[str] | Callable | None` | Default file(s) for display/download |
| `file_count` | `'single'` \| `'multiple'` \| `'directory'` | Number of files allowed |
| `file_types` | `list[str] | None` | Allowed file extensions (e.g., `["png", "jpg"]`) |
| `type` | `'filepath'` \| `'binary'` | Whether to return file path or binary content |
| `label` | `str | None` | Label for the component |
| `every` | `Timer | float | None` | Interval for automatic updates |
| `inputs` | `Component | list[Component] | set[Component] | None` | Components to take as input |
| `show_label` | `bool | None` | Whether to show label |
| `container` | `bool` | Whether to wrap component in a container |
| `scale` | `int | None` | Scaling factor |
| `min_width` | `int` | Minimum width of the component |
| `height` | `int | str | float | None` | Height of the component |
| `interactive` | `bool | None` | Whether the user can upload files |
| `visible` | `bool` | Whether the component is visible |
| `elem_id` | `str | None` | Unique ID for the element |
| `elem_classes` | `list[str] | str | None` | CSS classes for styling |
| `render` | `bool` | Whether to render the component |
| `key` | `int | str | None` | Unique identifier for the component |
| `allow_reordering` | `bool` | Whether users can reorder uploaded files |

---

## **Shortcuts**
| Class | Interface String Shortcut | Initialization |
|-------|----------------|-----------------|
| `gradio.File` | `"file"` | Uses default values |
| `gradio.Files` | `"files"` | Uses `file_count="multiple"` |

---

## **Example: Upload and Display File**
This example demonstrates uploading a file and returning its content.

```python
import gradio as gr

def read_file(file):
    with open(file.name, "r") as f:
        return f.read()

demo = gr.Interface(
    fn=read_file,
    inputs=gr.File(type="filepath", label="Upload a text file"),
    outputs="text"
)

if __name__ == "__main__":
    demo.launch()
```

---

## **Event Listeners**
Event listeners allow the UI to respond to user interactions.

| Listener | Description |
|----------|------------|
| `File.change(fn, ···)` | Triggered when file is uploaded or changed. |
| `File.select(fn, ···)` | Triggered when file is selected/deselected. Uses `gradio.SelectData`. |
| `File.clear(fn, ···)` | Triggered when file is cleared. |
| `File.upload(fn, ···)` | Triggered when file is uploaded. |
| `File.delete(fn, ···)` | Triggered when file is deleted. Uses `gradio.DeletedFileData`. |
| `File.download(fn, ···)` | Triggered when file is downloaded. Uses `gradio.DownloadData`. |

### **Event Parameters**
| Parameter | Type | Description |
|-----------|------|-------------|
| `fn` | `Callable | None | "decorator"` | Function to execute |
| `inputs` | `Component | list[Component] | None` | Input components |
| `outputs` | `Component | list[Component] | None` | Output components |
| `queue` | `bool` | Whether to queue execution |
| `batch` | `bool` | Whether to batch inputs |
| `preprocess` | `bool` | Whether to preprocess input |
| `postprocess` | `bool` | Whether to postprocess output |
| `concurrency_limit` | `int | None | "default"` | Maximum concurrent executions |

---

 