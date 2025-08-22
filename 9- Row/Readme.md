# Gradio `Row`  

## Overview

`Row` is a layout element in Gradio's Blocks API that arranges child components horizontally, making it useful for creating side-by-side layouts. It automatically handles the spacing between components and ensures that all children are displayed on a single horizontal line.

## Key Features:
- **Horizontal Layout**: Renders all child components in a horizontal row.
- **Flexible Sizing**: You can control the layout using parameters like `scale` and `max_width` for each child component.
- **Custom Styling**: You can use CSS classes and IDs to apply custom styles to the row or individual components.

## Basic Usage

```python
import gradio as gr

with gr.Blocks() as demo:
    with gr.Row():
        gr.Image("lion.jpg", scale=2)
        gr.Image("tiger.jpg", scale=1)

demo.launch()
```

### Explanation:
- **Row**: Creates a horizontal row layout.
- **Image Components**: Two images are placed in the `Row` container. The `scale` parameter adjusts the width of each image. In this case, the first image (`lion.jpg`) will take up twice the width of the second image (`tiger.jpg`).

## Parameters for `gr.Row`

- **`variant`**: `Literal['default', 'panel', 'compact']`
  - Controls the style of the row container.
    - `default`: Standard row layout.
    - `panel`: A panel-style layout, often used for grouping content.
    - `compact`: A tighter layout with reduced padding and margins.

- **`visible`**: `bool`
  - Controls whether the row and its child components are visible. If set to `False`, the entire row (and its components) will be hidden from the layout. The default is `True`.

- **`elem_id`**: `str | None`
  - The optional ID for the row element. This can be used for targeting the row with CSS or JavaScript.

- **`elem_classes`**: `list[str] | str | None`
  - A list or single string of CSS classes to apply to the row element. This allows for custom styling of the row container.

- **`render`**: `bool`
  - Determines whether the row should be rendered in the final layout. If set to `False`, the row will not appear. The default is `True`.

- **`height`**: `int | str | None`
  - Specifies the height of the row. This can be given as a fixed value (in pixels or percentage) or left as `None` for auto-sizing based on content.

- **`max_height`**: `int | str | None`
  - Defines the maximum height of the row. If the content exceeds this height, it will be clipped or overflowed.

- **`min_height`**: `int | str | None`
  - Defines the minimum height of the row. The row will always be at least this height, even if its content is smaller.

- **`equal_height`**: `bool`
  - If set to `True`, all components within the row will have equal height, regardless of their content. This is useful for uniform-looking layouts. The default is `False`.

- **`show_progress`**: `bool`
  - If set to `True`, a progress indicator will be shown for the row during data processing. The default is `False`.

## Use Cases for `gr.Row`

1. **Horizontal Layouts**: Use `Row` when you need to display multiple components side by side, such as images, textboxes, or buttons.
   
2. **Flexible Component Widths**: By adjusting the `scale` parameter of each child component, you can create layouts with varying component widths. For instance, one component can take up more space than others in the row.

3. **Custom Styling**: The `elem_id` and `elem_classes` parameters allow you to apply custom CSS styles to the row, making it easier to integrate into existing web designs.

4. **Responsive Layouts**: With parameters like `height`, `max_height`, and `min_height`, you can create responsive layouts that adjust to different screen sizes or content amounts.

## Example with `elem_classes`, `max_height`, and `equal_height`

```python
import gradio as gr

with gr.Blocks() as demo:
    with gr.Row(elem_classes="my-custom-row", max_height="400px", equal_height=True):
        gr.Image("lion.jpg", scale=2)
        gr.Image("tiger.jpg", scale=1)

demo.launch()
```

In this example:
- **`elem_classes="my-custom-row"`**: Adds a custom CSS class to the row for styling purposes.
- **`max_height="400px"`**: Limits the maximum height of the row to 400 pixels.
- **`equal_height=True`**: Ensures that both images will have the same height, even if their content varies.

## Conclusion

`gr.Row` is an essential layout element in Gradio's Blocks API for creating horizontal layouts. It provides a straightforward way to display components side by side, while offering flexibility in terms of component sizing, visibility, and custom styling. By using parameters like `scale`, `equal_height`, and `elem_classes`, you can easily control the appearance and layout of rows in your app.