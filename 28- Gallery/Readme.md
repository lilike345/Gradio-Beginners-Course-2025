# **`gradio.Gallery`**  
`gradio.Gallery(...)`

---

## **Description**  
The `gradio.Gallery` component creates a **gallery-style grid** to display images or videos. It can also show captions, making it ideal for presenting multiple media items in a visually appealing format. The component can also function as an **input** for users to upload images or videos and as an **output** for displaying selected images/videos at a higher resolution when clicked.

---

## **Behavior**

### **As an Input Component**  
- Passes the list of images or videos as:
  - `List[tuple[str, str | None]]` (image or video file path with or without caption).  
  - `List[tuple[PIL.Image.Image, str | None]]` (images with captions).  
  - `List[tuple[np.ndarray, str | None]]` (images as numpy arrays with captions).
  
- Each item is a tuple of (media, caption), where:
  - `media`: str (file path), PIL.Image, or np.ndarray.
  - `caption`: Optional string for captioning.

Your function should accept:

```python
def predict(value: List[tuple[str, str | None]] | List[tuple[PIL.Image.Image, str | None]] | List[tuple[np.ndarray, str | None]] | None):
    ...
```

### **As an Output Component**  
- Expects the function to return a list of images or videos (with or without captions).
  - `List[GalleryImageType | CaptionedGalleryImageType]` (media with optional captions).
  - `None` if no output is available.

Your function should return:

```python
def predict(...) -> list[GalleryImageType | CaptionedGalleryImageType] | None:
    ...
    return value
```

---

## **Initialization Parameters**

| Parameter          | Type                                   | Default      | Description |
|--------------------|----------------------------------------|--------------|-------------|
| `value`            | `list[np.ndarray | PIL.Image.Image | str | Path | tuple]` | `None`     | Initial images/videos with or without captions. |
| `format`           | `str`                                  | `None`       | Format type (either `'numpy'`, `'pil'`, or `'filepath'`). |
| `file_types`       | `list[str]`                            | `None`       | File types to allow (e.g., `['.jpg', '.png']`). |
| `label`            | `str | None`                           | `None`       | Label to display above the gallery. |
| `show_label`       | `bool`                                 | `True`       | Whether to show the label. |
| `container`        | `bool`                                 | `True`       | Whether the gallery is wrapped in a container. |
| `columns`          | `int | list[int] | tuple[int, ...]`     | `3`          | Number of columns for the gallery grid. |
| `rows`             | `int | list[int] | None`              | `None`       | Number of rows for the gallery grid. |
| `height`           | `int | float | str | None`              | `None`       | Height of the gallery component. |
| `allow_preview`    | `bool`                                 | `True`       | Whether to allow media preview. |
| `preview`          | `bool | None`                          | `True`       | Whether the media preview is enabled by default. |
| `selected_index`   | `int | None`                           | `None`       | The index of the initially selected image/video. |
| `object_fit`       | `'contain' | 'cover' | 'fill' | 'none' | 'scale-down'` | `None`  | Specifies how the object fits within the gallery (CSS object-fit). |
| `show_share_button`| `bool`                                 | `True`       | Whether to show a share button for media. |
| `show_download_button`| `bool`                              | `True`       | Whether to show a download button for media. |
| `interactive`      | `bool`                                 | `True`       | Whether the gallery is interactive (e.g., clickable items). |
| `show_fullscreen_button`| `bool`                             | `True`       | Whether to show a fullscreen button. |
| `elem_id`          | `str | None`                           | `None`       | Unique ID for styling. |
| `elem_classes`     | `list[str] | str | None`               | `None`       | CSS classes for custom styling. |

---

## **Shortcuts**

| Class             | Interface String Shortcut | Initialization |
|-------------------|---------------------------|----------------|
| `gr.Gallery`      | `"gallery"`               | Uses default values |

---

## **Example: Dynamic Gallery with Generated Images**
In this example, we generate a random set of images and display them in a gallery format.

```python
import random
import gradio as gr

def fake_gan():
    images = [
        (random.choice([
            "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1151ce9f4b2043de0d2e3b7826127998.jpg",
            "http://www.marketingtool.online/en/face-generator/img/faces/avatar-116b5e92936b766b7fdfc242649337f7.jpg",
            "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1163530ca19b5cebe1b002b8ec67b6fc.jpg",
            "http://www.marketingtool.online/en/face-generator/img/faces/avatar-1116395d6e6a6581eef8b8038f4c8e55.jpg",
            "http://www.marketingtool.online/en/face-generator/img/faces/avatar-11319be65db395d0e8e6855d18ddcef0.jpg"
        ]), f"label {i}") for i in range(3)
    ]
    return images

with gr.Blocks() as demo:
    gallery = gr.Gallery(
        label="Generated images", show_label=False, elem_id="gallery",
        columns=3, rows=1, object_fit="contain", height="auto"
    )
    btn = gr.Button("Generate images")

    btn.click(fake_gan, None, gallery)

demo.launch()
```

---

## **Event Listeners**
Event listeners enable responding to user interactions with the gallery, such as selecting, uploading, or previewing media.

| Listener                        | Description                                           |
|----------------------------------|-------------------------------------------------------|
| `Gallery.select(fn, ···)`        | Triggered when the user selects or deselects an image or video. |
| `Gallery.upload(fn, ···)`        | Triggered when the user uploads a file into the gallery. |
| `Gallery.change(fn, ···)`        | Triggered when the gallery's content changes (e.g., via user interaction or function updates). |
| `Gallery.preview_close(fn, ···)` | Triggered when the gallery's preview is closed. |
| `Gallery.preview_open(fn, ···)`  | Triggered when the gallery's preview is opened. |

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
- The **preview feature** may not work as expected with large videos or images due to browser limitations.
- Media files must be **available locally** or hosted on a publicly accessible URL to display properly in the gallery.

---

 