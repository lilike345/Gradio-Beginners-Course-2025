
---

### **`gradio.ImageEditor`**

#### **Description**
`gradio.ImageEditor` is a component used for uploading and editing images. The editor offers basic tools for modifying the uploaded image, including cropping, drawing, and applying brushes or strokes, as well as managing layers. The component can either be used as an input (for uploading and editing images) or as an output (to display edited images).

#### **Behavior**
- **As Input:**
  - When used as an input, the component passes an image in the form of an `EditorValue`, which is a dictionary containing:
    - `'background'`: The background image (type: PIL.Image, np.array, or file path).
    - `'layers'`: A list of images representing the editable layers.
    - `'composite'`: The final composite image (type: PIL.Image, np.array, or file path).
  - Your function should accept this dictionary as input:
    ```python
    def predict(value: EditorValue | None):
        ...
    ```

- **As Output:**
  - When used as an output, the component expects an `EditorValue` dictionary with the same structure as described above or a single image that will be used as the background.
  - Your function should return an `EditorValue` or a single image:
    ```python
    def predict(...) -> EditorValue | ImageType | None:
        ...
    return value
    ```

---

#### **Initialization Parameters**
- **value**: The initial value (image or `EditorValue` dictionary).
- **height**, **width**: Define the size of the editor.
- **image_mode**: Specify the image mode (e.g., `RGB`, `L`).
- **sources**: List of possible image sources, such as `upload`, `webcam`, or `clipboard`.
- **type**: Specifies the type of image input (e.g., `numpy`, `pil`, or `filepath`).
- **show_label**: Optionally show a label for the component.
- **show_download_button**: Enable or disable the download button.
- **canvas_size**: Set the size of the editing canvas.
- **crop_size**: Defines the aspect ratio for cropping.
- **brush**: Define brush settings for drawing.
- **eraser**: Define eraser settings for editing.

---

#### **Shortcuts**
- **gr.ImageEditor**: `"imageeditor"` (Uses default values).
- **gr.Sketchpad**: `"sketchpad"` (Uses brush settings).
- **gr.Paint**: `"paint"` (Uses default settings).
- **gr.ImageMask**: `"imagemask"` (Uses brush settings).

---

#### **Demos**

- **Image Editor Example:**
    ```python
    import gradio as gr
    import time

    def sleep(im):
        time.sleep(5)
        return [im["background"], im["layers"][0], im["layers"][1], im["composite"]]

    def predict(im):
        return im["composite"]

    with gr.Blocks() as demo:
        with gr.Row():
            im = gr.ImageEditor(type="numpy", crop_size="1:1")
            im_preview = gr.Image()
        n_upload = gr.Number(0, label="Number of upload events", step=1)
        n_change = gr.Number(0, label="Number of change events", step=1)
        n_input = gr.Number(0, label="Number of input events", step=1)

        im.upload(lambda x: x + 1, outputs=n_upload, inputs=n_upload)
        im.change(lambda x: x + 1, outputs=n_change, inputs=n_change)
        im.input(lambda x: x + 1, outputs=n_input, inputs=n_input)
        im.change(predict, outputs=im_preview, inputs=im, show_progress="hidden")

    if __name__ == "__main__":
        demo.launch()
    ```

---

#### **Event Listeners**
Event listeners allow you to respond to user actions in the `gr.ImageEditor` component, such as when a user uploads an image, applies changes, or selects parts of the image. Here are the supported listeners:

- **ImageEditor.clear(fn, ...)**: Triggered when the user clears the editor (e.g., pressing the clear button).
- **ImageEditor.change(fn, ...)**: Triggered when the value of the image changes, either from user input or programmatically.
- **ImageEditor.input(fn, ...)**: Triggered when the value of the image is modified.
- **ImageEditor.select(fn, ...)**: Triggered when the user selects or deselects an image.
- **ImageEditor.upload(fn, ...)**: Triggered when the user uploads an image.
- **ImageEditor.apply(fn, ...)**: Triggered when the user applies changes to the image.

---

#### **Event Parameters**
- **fn**: Callable function to handle the event.
- **inputs**: Components or blocks to pass to the event.
- **outputs**: Components or blocks to receive output from the event handler.
- **scroll_to_output**: Whether to scroll to the output after the event.
- **show_progress**: Specify the progress display style (`'full'`, `'minimal'`, or `'hidden'`).
- **queue**: Enable or disable event queueing.
- **trigger_mode**: Defines when the event should be triggered (`'once'`, `'multiple'`, or `'always_last'`).
- **js**: JavaScript code to run for the event.
- **time_limit**: Limit the time for the event.
- **stream_every**: Specify the interval for streaming data.

---

#### **Helper Classes**

- **Brush**: A class for defining the brush tool in the ImageEditor.
    - Parameters:
        - `default_size`: Default brush size.
        - `colors`: List of brush colors.
        - `default_color`: Default brush color.
        - `color_mode`: Defines how colors are applied (e.g., `fixed`, `defaults`).

- **Eraser**: A class for defining the eraser tool in the ImageEditor.
    - Parameters:
        - `default_size`: Default size of the eraser.

---
 