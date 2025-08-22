
### `gradio.AnnotatedImage` Component

#### Purpose:
The `gradio.AnnotatedImage` component is used to display a base image and overlay colored annotations on top of it. These annotations can represent various tasks such as object detection or image segmentation. It is not typically used as an input component, but rather as an output component to display annotated images.

#### Key Behavior:
- **Input:** Accepts a tuple consisting of a string (filepath to the base image) and a list of annotations. Each annotation is a tuple of a mask (either an image or bounding box) and a string label.
  
  Example of input format:
  ```python
  def predict(value: tuple[str, list[tuple[str, str]]] | None):
      ...
  ```

- **Output:** Expects a tuple containing:
  1. A base image (which can be a filepath, `numpy.ndarray`, or `PIL.Image`).
  2. A list of annotations, where each annotation is a tuple consisting of:
     - A mask, either a bounding box (4 integers: x1, y1, x2, y2) or a 0-1 confidence mask in the form of `numpy.ndarray`.
     - A string label for the annotation.

  Example of output format:
  ```python
  def predict(···) -> tuple[np.ndarray | PIL.Image.Image | str, list[tuple[np.ndarray | tuple[int, int, int, int], str]]] | None:
      return value
  ```

#### Initialization Parameters:
- **`value`:** The tuple (base image, list of annotations) to be displayed.
- **`format`:** The image format to use.
- **`show_legend`:** Whether to display the legend for the annotations (default `False`).
- **`height` / `width`:** The height and width of the component.
- **`color_map`:** A dictionary to map each annotation label to a specific color.
- **`label`:** Label for the component (optional).
- **`every`:** A float or timer for intervals.
- **`inputs` / `show_label` / `container`:** Various configurations for input components, labels, and container settings.
- **`scale`, `min_width`, `visible`, `elem_id`:** Settings related to scaling, minimum width, and visibility.

#### Example Code:
```python
import gradio as gr
import numpy as np
import random

# Define section labels
section_labels = [
    "apple", "banana", "carrot", "donut", "eggplant", "fish", "grapes", "hamburger", "ice cream", "juice"
]

# Set up Blocks layout
with gr.Blocks() as demo:
    with gr.Row():
        num_boxes = gr.Slider(0, 5, 2, step=1, label="Number of boxes")
        num_segments = gr.Slider(0, 5, 1, step=1, label="Number of segments")
    
    with gr.Row():
        img_input = gr.Image()
        img_output = gr.AnnotatedImage(color_map={"banana": "#a89a00", "carrot": "#ffae00"})

    section_btn = gr.Button("Identify Sections")
    selected_section = gr.Textbox(label="Selected Section")

    # Function to create random sections and segments on image
    def section(img, num_boxes, num_segments):
        sections = []
        for a in range(num_boxes):
            x = random.randint(0, img.shape[1])
            y = random.randint(0, img.shape[0])
            w = random.randint(0, img.shape[1] - x)
            h = random.randint(0, img.shape[0] - y)
            sections.append(((x, y, x + w, y + h), section_labels[a]))
        for b in range(num_segments):
            x = random.randint(0, img.shape[1])
            y = random.randint(0, img.shape[0])
            r = random.randint(0, min(x, y, img.shape[1] - x, img.shape[0] - y))
            mask = np.zeros(img.shape[:2])
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    dist_square = (i - y) ** 2 + (j - x) ** 2
                    if dist_square < r**2:
                        mask[i, j] = round((r**2 - dist_square) / r**2 * 4) / 4
            sections.append((mask, section_labels[b + num_boxes]))
        return (img, sections)

    section_btn.click(section, [img_input, num_boxes, num_segments], img_output)

    def select_section(evt: gr.SelectData):
        return section_labels[evt.index]

    img_output.select(select_section, None, selected_section)

if __name__ == "__main__":
    demo.launch()
```

#### Event Listeners:
- **`select(fn, ...)`**: Listens for when a user selects or deselects an annotation in the `AnnotatedImage` component. The event data includes the label and selection state.

#### Example Use Case:
- **Image Segmentation:** Display an image with various segmented regions, where each region is represented by a different color or bounding box, and users can select specific regions.

### Summary:
`gradio.AnnotatedImage` is used for displaying images with annotations such as object detection or image segmentation. It takes both bounding boxes and confidence masks as annotations and displays them on top of a base image. This component is particularly useful for visualizing machine learning results like object detection models or segmentation tasks, where annotations help to interpret model predictions.