# **`gradio.FileExplorer`**  
`gradio.FileExplorer(...)`

---

## **Description**  
The `gradio.FileExplorer` component creates a **file explorer** UI that allows users to:  
- Browse directories and files hosted on the machine running the Gradio app.  
- Select one or more files depending on the configuration.  
- Select files as input to a function, or return file paths for output.  

This component enables **local file browsing**, which is only available in local mode and does **not work on Hugging Face Spaces**.

---

## **Behavior**  

### **As an Input Component**  
- Passes the selected file or directory as:  
  - `str` (file path)  
  - `list[str]` (multiple file paths)  
  - `None` (if no file is selected)  

- Your function should accept:

```python
def predict(value: list[str] | str | None):
    ...
```

### **As an Output Component**  
- Expects your function to return:
  - `str` (path to a single file)  
  - `list[str]` (list of paths to multiple files)  
  - `None` (if no output file)

- Your function should return:

```python
def predict(...) -> str | list[str] | None:
    ...
    return value
```

---

## **Initialization Parameters**  
| Parameter          | Type                                   | Default     | Description |
|--------------------|----------------------------------------|-------------|-------------|
| `glob`             | `str`                                  | `None`      | Glob pattern to filter files. |
| `value`            | `str | list[str] | Callable | None`    | `None`      | Default selected file(s). |
| `file_count`       | `'single'` \| `'multiple'`            | `'single'`  | Number of files allowed for selection. |
| `root_dir`         | `str | Path`                           | `None`      | Root directory for file exploration. |
| `ignore_glob`      | `str | None`                           | `None`      | Glob pattern for excluding files. |
| `label`            | `str | None`                           | `None`      | Label for the component. |
| `interactive`      | `bool | None`                          | `True`      | Whether the component is interactive. |
| `visible`          | `bool`                                 | `True`      | Whether the component is visible. |
| `height`           | `int | str | None`                     | `None`      | Height of the component. |
| `max_height`       | `str | None`                           | `None`      | Maximum height of the component. |
| `min_height`       | `str | None`                           | `None`      | Minimum height of the component. |
| `scale`            | `int | None`                           | `None`      | Scale factor for the component. |
| `min_width`        | `int`                                  | `160`       | Minimum width of the component. |
| `container`        | `bool`                                 | `True`      | Whether to wrap the component in a container. |
| `elem_id`          | `str | None`                           | `None`      | Unique ID for styling. |
| `elem_classes`     | `list[str] | str | None`               | `None`      | CSS classes for custom styling. |

---

## **Shortcuts**
| Class             | Interface String Shortcut | Initialization |
|-------------------|---------------------------|----------------|
| `gr.FileExplorer`  | `"fileexplorer"`           | Uses default values |

---

## **Example: File Explorer with Multiple Selections**
This example demonstrates how to allow users to select multiple files from a specific directory.

```python
import gradio as gr
from pathlib import Path

# Set the root directory for file exploration
root_dir = Path("/path/to/directory")

def process_selected_files(files):
    return files  # Return selected files

with gr.Blocks() as demo:
    gr.Markdown('### Select multiple Python files')
    file_explorer = gr.FileExplorer(
        glob="**/*.py",  # Select Python files
        file_count="multiple",  # Allow multiple selections
        root_dir=root_dir
    )
    
    # Process selected files
    gr.Button("Submit").click(process_selected_files, inputs=file_explorer, outputs="text")

demo.launch()
```

---

## **Event Listeners**
Event listeners allow you to respond to user interactions with the `FileExplorer` component. Below are the event listeners you can use:

| Listener                        | Description                                           |
|----------------------------------|-------------------------------------------------------|
| `FileExplorer.change(fn, ···)`   | Triggered when the file selection changes.            |
| `FileExplorer.select(fn, ···)`   | Triggered when a file is selected or deselected.      |
| `FileExplorer.clear(fn, ···)`    | Triggered when the selection is cleared.              |
| `FileExplorer.upload(fn, ···)`   | Triggered when a file is uploaded.                    |
| `FileExplorer.delete(fn, ···)`   | Triggered when a file is deleted.                     |
| `FileExplorer.download(fn, ···)` | Triggered when a file is downloaded.                  |

### **Event Parameters**
| Parameter           | Type                                        | Description                                                                 |
|---------------------|---------------------------------------------|-----------------------------------------------------------------------------|
| `fn`                | `Callable | None | "decorator"`              | Function to execute when the event is triggered.                            |
| `inputs`            | `Component | list[Component] | None`       | Input components involved in the event.                                     |
| `outputs`           | `Component | list[Component] | None`      | Output components triggered by the event.                                   |
| `queue`             | `bool`                                      | Whether to queue the execution of the function.                             |
| `preprocess`        | `bool`                                      | Whether to preprocess input before executing the function.                 |
| `postprocess`       | `bool`                                      | Whether to postprocess output after executing the function.                 |
| `trigger_mode`      | `'once' | 'multiple' | 'always_last'`      | Defines the trigger mode for event execution.                              |
| `js`                | `str | None`                                | Custom JavaScript to be executed when the event is triggered.               |

---

## **Limitations**  
- **Does NOT work on Hugging Face Spaces**.  
- **Local mode only**: This component is only available when running Gradio apps locally.  
- Can **only browse files on the machine** that is running the app.

---

 