
### **Description**
The `gradio.HighlightedText` component is used to display text with specific parts highlighted based on a category or numerical value. This is particularly useful for tasks like visualizing changes in text (e.g., differences between two texts).

### **Behavior**
- **As an input component**: You pass a list of tuples, each containing a substring of the text and its associated label, which can be a string (category), float (confidence score), or `None` (if no label is provided).
  
  Example of input:
  ```python
  def predict(value: list[tuple[str, str | float | None]] | None):
      ...
  ```

- **As an output component**: Your function should return either a list of `(word, category)` tuples or a dictionary containing `"text"` and `"entities"`. The entities list consists of dictionaries with keys `"entity"`, `"start"`, and `"end"`, marking the part of the text that was highlighted.

  Example of output:
  ```python
  def predict(...) -> list[tuple[str, str | float | None]] | dict | None:
      ...
      return value
  ```

### **Initialization Parameters**
- **value**: The text or function to process (list of `(str, str | float | None)` tuples, dictionary, or callable).
- **color_map**: A dictionary that maps categories to colors for highlighting.
- **show_legend**: Boolean to show a legend for the categories.
- **show_inline_category**: Boolean to show the category next to each word.
- **combine_adjacent**: If set to `True`, adjacent text spans with the same category will be merged.
- **adjacent_separator**: The separator for combining adjacent spans (if `combine_adjacent` is `True`).
- **label**: Optional label for the component.
- **every**: A timer value for periodic updates (optional).
- **inputs**: The component(s) to provide as input.
- **show_label**: Whether to show the label for the component.
- **container**: Whether the component should be a container for other components.
- **scale**: Scaling factor for the component.
- **min_width**: Minimum width of the component.
- **visible**: Boolean indicating if the component is visible.
- **elem_id**: Element ID for custom styling.
- **elem_classes**: CSS classes for styling.
- **render**: Whether the component should be rendered.
- **key**: Unique key for the component.
- **interactive**: If `True`, allows user interaction.

### **Example Code**
```python
from difflib import Differ
import gradio as gr

def diff_texts(text1, text2):
    d = Differ()
    return [
        (token[2:], token[0] if token[0] != " " else None)
        for token in d.compare(text1, text2)
    ]

demo = gr.Interface(
    diff_texts,
    [
        gr.Textbox(
            label="Text 1",
            info="Initial text",
            lines=3,
            value="The quick brown fox jumped over the lazy dogs.",
        ),
        gr.Textbox(
            label="Text 2",
            info="Text to compare",
            lines=3,
            value="The fast brown fox jumps over lazy dogs.",
        ),
    ],
    gr.HighlightedText(
        label="Diff",
        combine_adjacent=True,
        show_legend=True,
        color_map={"+": "red", "-": "green"}
    ),
    theme=gr.themes.Base()
)

if __name__ == "__main__":
    demo.launch()
```

### **Event Listeners**
`gradio.HighlightedText` supports the following event listeners:

- **`HighlightedText.change(fn, ...)`**: Triggered when the value of the `HighlightedText` component changes (e.g., due to user input or function update).
- **`HighlightedText.select(fn, ...)`**: Triggered when a user selects or deselects a part of the text.

### **Event Parameters**
- **fn**: Callable function to handle the event.
- **inputs**: Component(s) to use as input.
- **outputs**: Component(s) to use as output.
- **api_name**: The name of the API endpoint (optional).
- **scroll_to_output**: Scroll to the output after event.
- **show_progress**: Show progress indicator during event processing.
- **queue**: If `True`, queues the event.
- **batch**: Whether to process in batches.
- **max_batch_size**: The maximum number of items to process in one batch.
- **preprocess**: Whether to preprocess inputs before the event.
- **postprocess**: Whether to postprocess outputs after the event.
- **cancels**: List of events to cancel during this event.
- **trigger_mode**: Mode for triggering the event (`once`, `multiple`, or `always_last`).
- **js**: JavaScript code for custom client-side functionality.
- **concurrency_limit**: Limit the number of concurrent calls.
- **concurrency_id**: Unique identifier for concurrent calls.
- **show_api**: Show API details.
- **time_limit**: Time limit for the event.
- **stream_every**: Streaming interval.
- **like_user_message**: Whether the event is like a user message.

This component is useful for visualizing differences, highlighting key entities, or emphasizing specific parts of text based on their categories or scores.