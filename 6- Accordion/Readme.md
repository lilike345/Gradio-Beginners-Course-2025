# Gradio `Accordion`  

## Overview

`Accordion` is a layout element in Gradio that allows you to group content inside a collapsible and expandable container. It is useful for organizing content and providing an interactive, space-saving way to display information. Users can toggle the accordion to show or hide the content inside.

## Key Features:
- **Collapsible/Expandable**: Accordion content can be hidden or revealed by the user.
- **Space-Saving**: Ideal for large amounts of content or optional details that should only be visible when needed.
- **Dynamic Layout**: Can be used in conjunction with other components to create interactive and organized layouts.

## Basic Usage

```python
import gradio as gr

with gr.Blocks() as demo:
    with gr.Accordion("See Details"):
        gr.Markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

demo.launch()
```

### Key Components:
- **Accordion**: The container that groups content and can be toggled open/closed.
- **Label**: The label for the accordion that the user clicks to open or close the content.

In this example:
- The accordion label is "See Details".
- The content inside the accordion is a Markdown component displaying some text.

## Parameters for `gr.Accordion`

- **`label`**: `str | None`
  - The label displayed for the accordion. This is the clickable element that the user interacts with to expand or collapse the content.
  
- **`open`**: `bool`
  - Controls whether the accordion is initially open or closed. By default, it’s `False` (closed). Set it to `True` to make it open by default.

- **`visible`**: `bool`
  - Controls the visibility of the accordion. If set to `False`, the accordion will not be rendered in the UI.

- **`elem_id`**: `str | None`
  - An optional ID to assign to the accordion element. Useful for styling or targeting the element in JavaScript.

- **`elem_classes`**: `list[str] | str | None`
  - One or more CSS classes that can be applied to the accordion element for custom styling.

- **`render`**: `bool`
  - A flag that determines whether the accordion should render. This is useful for conditional rendering based on user interactions or other factors.

## Accordion Methods

### `gr.Accordion.expand`

#### Description
This listener is triggered when the accordion is expanded (opened). You can attach actions to this event, such as showing additional information or triggering functions when the accordion is opened.

#### Example Usage
```python
import gradio as gr

def on_expand():
    return "Accordion Expanded!"

with gr.Blocks() as demo:
    with gr.Accordion("See Details") as accordion:
        gr.Markdown("Lorem ipsum dolor sit amet.")
    
    accordion.expand(fn=on_expand)

demo.launch()
```

#### Parameters
- **`fn`**: `Callable | None | Literal['decorator']`
  - A function to run when the accordion is expanded.
  
- **`inputs`**: `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None`
  - Components whose states will be passed as inputs to the function.
  
- **`outputs`**: `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None`
  - Components to update based on the function’s outputs.

- **Additional parameters**: Similar to those in the `gr.render` decorator for controlling concurrency, triggering modes, etc.

---

### `gr.Accordion.collapse`

#### Description
This listener is triggered when the accordion is collapsed (closed). It can be used to perform actions or reset components when the accordion is closed.

#### Example Usage
```python
import gradio as gr

def on_collapse():
    return "Accordion Collapsed!"

with gr.Blocks() as demo:
    with gr.Accordion("See Details") as accordion:
        gr.Markdown("Lorem ipsum dolor sit amet.")

    accordion.collapse(fn=on_collapse)

demo.launch()
```

#### Parameters
- **`fn`**: `Callable | None | Literal['decorator']`
  - A function to run when the accordion is collapsed.
  
- **`inputs`**: `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None`
  - Components whose states will be passed as inputs to the function.

- **`outputs`**: `Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None`
  - Components to update based on the function’s outputs.

- **Additional parameters**: Similar to those in the `gr.render` decorator for controlling concurrency, triggering modes, etc.

---

## Use Cases for `gr.Accordion`

1. **Show/Hide Details**: Perfect for showing additional details on user request, such as extended descriptions, troubleshooting tips, or hidden options.
  
2. **Organizing Content**: Accordion can be used to group related information and hide or show sections of content, reducing clutter on the page.

3. **Forms with Multiple Sections**: Useful for creating multi-step forms or long forms with collapsible sections, allowing users to expand only the sections they are interested in.

4. **Interactive Tutorials**: You can show additional hints or step-by-step instructions in an accordion, which expands when the user asks for help.

## Conclusion

The `gr.Accordion` component in Gradio provides an easy way to organize content in a collapsible layout. It is useful when you need to display large or optional information that should only be visible when the user wants to see it. With the ability to expand and collapse dynamically, it enhances the user experience by keeping the interface clean and interactive. By integrating `expand` and `collapse` listeners, you can trigger custom actions when the accordion state changes, adding even more flexibility to your app’s behavior.