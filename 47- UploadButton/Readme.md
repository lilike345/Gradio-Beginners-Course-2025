## 📌 **`gradio.UploadButton`**  

### 🔹 **Description:**  
`gradio.UploadButton` allows users to upload files by clicking a button. It can accept **single or multiple** files, and **specific file types** (e.g., images, videos, text files).

---

### 🔹 **Behavior:**  
- **As Input Component:**  
  - Passes the uploaded file as a **string filepath** or **binary bytes object**.  
  - If multiple files are allowed, it passes a **list of filepaths/bytes**.  

- **As Output Component:**  
  - Expects a **filepath (`str`) or list of filepaths (`list[str]`)**.  

---

### 🔹 **Example Usage:**  
#### ✅ **Uploading & Displaying an Image**
```python
import gradio as gr
from PIL import Image

def process_image(file):
    image = Image.open(file)  # Open the uploaded image
    return image  # Return the image for display

demo = gr.Interface(
    fn=process_image,
    inputs=gr.UploadButton("Upload an Image", file_types=[".png", ".jpg", ".jpeg"]),
    outputs=gr.Image()
)

demo.launch()
```
💡 **Explanation:** The user uploads an image, and it is displayed using `gr.Image()`.

---

### 🔹 **Initialization Parameters:**  
| Parameter | Type | Description |
|-----------|------|-------------|
| `label` | `str` | The button's label. |
| `value` | `str \| list[str] \| Callable \| None` | Default file(s) to load. |
| `every` | `Timer \| float \| None` | How often to trigger the upload function. |
| `inputs` | `Component \| list[Component] \| None` | Input components. |
| `variant` | `'primary' \| 'secondary' \| 'stop'` | Button style. |
| `visible` | `bool` | Whether the button is visible. |
| `size` | `'sm' \| 'md' \| 'lg'` | Button size. |
| `icon` | `str \| None` | Optional icon. |
| `interactive` | `bool` | Whether the button is interactive. |
| `file_count` | `'single' \| 'multiple' \| 'directory'` | Number of files allowed. |
| `file_types` | `list[str] \| None` | Allowed file extensions (e.g., `[".png", ".jpg"]`). |

💡 **Shortcut:**  
- `"uploadbutton"` is the alias for `gr.UploadButton` with default settings.

---

### 🔹 **Event Listeners:**  
| Listener | Description |
|----------|-------------|
| `.click(fn, ...)` | Triggered when the UploadButton is clicked. |
| `.upload(fn, ...)` | Triggered when the user uploads a file. |

---

### 🔹 **Advanced Usage:**  
#### ✅ **Upload & Download a File**
```python
from pathlib import Path
import gradio as gr

def upload_file(filepath):
    name = Path(filepath).name
    return [
        gr.UploadButton(visible=False),
        gr.DownloadButton(label=f"Download {name}", value=filepath, visible=True)
    ]

def download_file():
    return [gr.UploadButton(visible=True), gr.DownloadButton(visible=False)]

with gr.Blocks() as demo:
    gr.Markdown("Upload a file, then download it (only once!).")
    
    with gr.Row():
        u = gr.UploadButton("Upload a file", file_count="single")
        d = gr.DownloadButton("Download the file", visible=False)

    u.upload(upload_file, u, [u, d])
    d.click(download_file, None, [u, d])

demo.launch()
```
💡 **Explanation:**  
- The user uploads a file, making the **download button appear**.  
- The file can be downloaded **only once**, then the upload button **reappears**.

---

### 🔹 **When to Use `gradio.UploadButton`?**  
✅ When users need to upload **images, videos, text, or any file**.  
✅ When handling **single or multiple** file uploads.  
✅ When restricting file types for **better validation**.  

This should help you integrate `gradio.UploadButton` efficiently into your projects! 🚀