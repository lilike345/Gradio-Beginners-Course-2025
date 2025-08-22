
### **Description**
The `gr.Image` component allows you to upload images as input or display images as output. It supports various image formats and can handle images from different sources like file upload, webcam, or clipboard.

### **Behavior**
- **As an input component**: The uploaded image is passed as one of the following types:
  - `np.ndarray`: A NumPy array representing the image.
  - `PIL.Image.Image`: A PIL image object.
  - `str`: A file path pointing to the image.

  Example of input:
  ```python
  def predict(value: np.ndarray | PIL.Image.Image | str | None):
      ...
  ```

- **As an output component**: The function should return one of the following types:
  - `np.ndarray`: The output image as a NumPy array.
  - `PIL.Image.Image`: The output image as a PIL image object.
  - `str`: The file path to the image.
  - `Path`: A Path object pointing to the image file.

  Example of output:
  ```python
  def predict(...) -> np.ndarray | PIL.Image.Image | str | Path | None:
      ...
      return value
  ```

### **Initialization Parameters**
- **value**: Image source (either a file path, `PIL.Image.Image`, `np.ndarray`, or a callable).
- **format**: Desired image format (optional).
- **height**: Height of the displayed image (optional).
- **width**: Width of the displayed image (optional).
- **image_mode**: Image color mode (e.g., 'RGB', 'RGBA', etc.).
- **sources**: List of sources from where the image can be obtained. Options include:
  - `'upload'`: Upload an image from the file system.
  - `'webcam'`: Capture an image using the webcam.
  - `'clipboard'`: Paste an image from the clipboard.
- **type**: Specifies the expected type for the input. Options are:
  - `'numpy'`: Expects a NumPy array.
  - `'pil'`: Expects a PIL Image.
  - `'filepath'`: Expects a file path string.
- **label**: Label to display with the component (optional).
- **show_label**: Whether to display the label for the component.
- **show_download_button**: Whether to display a button for downloading the image.
- **interactive**: Whether the component should be interactive.
- **visible**: Whether the component should be visible.
- **streaming**: Whether to stream images as they are processed.
- **elem_id**: Unique ID for custom styling.
- **elem_classes**: CSS classes for styling.
- **render**: Whether to render the component.
- **key**: Unique key for the component.
- **mirror_webcam**: Whether to mirror the webcam feed.
- **show_share_button**: Whether to display a share button.
- **webcam_constraints**: Constraints for the webcam feed.

### **GIF and SVG Image Formats**
- **GIF**: Animated GIFs are supported, but only the first frame is shown when converted to a NumPy array (default behavior). To use GIFs correctly, set the `type` parameter to `"filepath"` or `"pil"`.
- **SVG**: SVG images are returned as file paths because they cannot be processed as a NumPy array or PIL Image object.

### **Example Code**
```python
import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(), "image")
if __name__ == "__main__":
    demo.launch()
```
In this example:
- The `sepia` function applies a sepia filter to the uploaded image.
- `gr.Image()` is used to upload and display the image.

### **Event Listeners**
The `gr.Image` component supports the following event listeners:
- **`Image.clear(fn, ...)`**: Triggered when the image is cleared (using the clear button).
- **`Image.change(fn, ...)`**: Triggered when the value of the image changes (due to user input or function update).
- **`Image.stream(fn, ...)`**: Triggered when the image is streamed.
- **`Image.select(fn, ...)`**: Triggered when the user selects or deselects the image.
- **`Image.upload(fn, ...)`**: Triggered when the user uploads an image.
- **`Image.input(fn, ...)`**: Triggered when the user changes the value of the image.

### **Event Parameters**
- **fn**: The function to call when the event is triggered.
- **inputs**: The input components that trigger the event.
- **outputs**: The output components that will receive the event’s result.
- **api_name**: The API name for the event (optional).
- **scroll_to_output**: Whether to scroll to the output after the event.
- **show_progress**: Progress indicator type (`'full'`, `'minimal'`, or `'hidden'`).
- **queue**: Whether to queue the event.
- **batch**: Whether to batch events together.
- **preprocess**: Whether to preprocess inputs before triggering the event.
- **postprocess**: Whether to postprocess outputs after the event.
- **cancels**: List of events to cancel.
- **trigger_mode**: Mode for triggering the event (`once`, `multiple`, `always_last`).
- **js**: Custom JavaScript to run with the event.
- **concurrency_limit**: Limit the number of concurrent events.
- **concurrency_id**: Unique ID for the concurrency group.
- **show_api**: Show the API details.
- **time_limit**: Time limit for processing the event.
- **stream_every**: Interval for streaming.
- **like_user_message**: Whether the event should behave like a user message.

### **Use Cases**
The Image component is ideal for:
- Uploading and processing images for tasks like classification, filtering, or transformation.
- Displaying images as part of a Gradio interface, such as for image generation models.
- Handling various image sources like file uploads, webcam capture, or clipboard paste.