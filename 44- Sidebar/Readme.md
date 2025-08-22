
# 📚 `gradio.Sidebar` – Sidebar Layout Component

`gradio.Sidebar` is a collapsible panel in Gradio that allows developers to group interface components along the left (or right) side of the screen within a `gr.Blocks` layout. It enhances UI/UX by allowing optional or grouped controls (like filters, settings, or tools) to be neatly organized and hidden when not in use.

---

## 🧰 Basic Example

```python
import gradio as gr

with gr.Blocks() as demo:
    with gr.Sidebar():
        gr.Textbox(label="Your input")
        gr.Button("Submit")

demo.launch()
```

This code creates a sidebar with a textbox and a button on the left side of the screen.

---

## ⚙️ Initialization Parameters

| Parameter          | Type                                     | Default  | Description                                        |
| ------------------ | ---------------------------------------- | -------- | -------------------------------------------------- |
| `label`            | `str` \| `I18nData` \| `None`            | `None`   | Internal name of the sidebar (not shown to users). |
| `open`             | `bool`                                   | `True`   | Determines whether the sidebar is open by default. |
| `visible`          | `bool`                                   | `True`   | Controls visibility of the sidebar.                |
| `elem_id`          | `str` \| `None`                          | `None`   | Unique ID for targeting with CSS or JavaScript.    |
| `elem_classes`     | `str` \| `list[str]` \| `None`           | `None`   | Custom CSS classes for styling.                    |
| `render`           | `bool`                                   | `True`   | Whether to render this component immediately.      |
| `width`            | `int` \| `str`                           | `320`    | Width of the sidebar (e.g., `320`, `'20vw'`).      |
| `position`         | `'left'` \| `'right'`                    | `'left'` | Position of the sidebar in the layout.             |
| `key`              | `int` \| `str` \| `tuple[...]` \| `None` | `None`   | Identifies this component across re-renders.       |
| `preserved_by_key` | `str` \| `list[str]` \| `None`           | `None`   | List of attributes preserved during re-render.     |

---

## 🚀 Event Listeners

### 🔼 `.expand(...)`

Triggered when the sidebar is **expanded**.

```python
@sidebar.expand()
def on_expand():
    print("Sidebar expanded!")
```

| Parameter                   | Description                                                        |
| --------------------------- | ------------------------------------------------------------------ |
| `fn`                        | Function to trigger on expansion.                                  |
| `inputs` / `outputs`        | Optional components connected to the function.                     |
| `api_name`                  | Custom name for API docs or `False` to hide.                       |
| `scroll_to_output`          | If `True`, scrolls to output.                                      |
| `show_progress`             | `"full"` \| `"minimal"` \| `"hidden"` – progress bar display type. |
| `queue`                     | Enable event queuing.                                              |
| `batch`, `max_batch_size`   | Enable batching of inputs.                                         |
| `preprocess`, `postprocess` | Control auto-processing of data.                                   |
| `trigger_mode`              | `'once'`, `'multiple'`, `'always_last'` submission behavior.       |

---

### 🔽 `.collapse(...)`

Triggered when the sidebar is **collapsed**.

```python
@sidebar.collapse()
def on_collapse():
    print("Sidebar collapsed!")
```

The parameters for `.collapse()` are the same as `.expand()`.

---

## 💡 When to Use

* For optional settings or filters in a UI.
* For step-by-step workflows or grouped inputs.
* To reduce visual clutter by hiding rarely-used controls.

---

## 🔗 Related Links

* [Gradio Documentation](https://www.gradio.app/)
* [Gradio on GitHub](https://github.com/gradio-app/gradio)

---


