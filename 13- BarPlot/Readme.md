
---

### **BarPlot**

`gradio.BarPlot(···)`

#### **Description:**
Creates a bar plot component to display data from a pandas DataFrame.

#### **Behavior:**
- **As input component:** The data to display in a bar plot. Your function should accept an `AltairPlotData`, which typically consists of a pandas DataFrame containing at least two columns — one for the x-axis and another for the y-axis.
  
  **Example function signature for input:**
  ```python
  def predict(value: AltairPlotData)
  ```

- **As output component:** Expects a pandas DataFrame containing the data to display in the bar plot. The DataFrame should contain at least two columns: one for the x-axis (`x`) and one for the y-axis (`y`).
  
  **Example function signature for output:**
  ```python
  def predict(···) -> pd.DataFrame | None
  ```
  
  The function should return a DataFrame or `None` if no output is to be shown.

#### **Initialization:**
- **Parameters:**
  - `value`: `pd.DataFrame | Callable | None` — The data to display (either as a pandas DataFrame or callable function).
  - `x`: `str | None` — The column name for the x-axis.
  - `y`: `str | None` — The column name for the y-axis.
  - `color`: `str | None` — The column name to color the bars.
  - `title`: `str | None` — The title of the plot.
  - `x_title`: `str | None` — The title for the x-axis.
  - `y_title`: `str | None` — The title for the y-axis.
  - `color_title`: `str | None` — The title for the color legend.
  - `x_bin`: `str | float | None` — Binning for the x-axis.
  - `y_aggregate`: `'sum', 'mean', 'median', 'min', 'max', 'count' | None` — The aggregation function for the y-axis.
  - `color_map`: `dict[str, str] | None` — A mapping of colors for categorical values.
  - `x_lim`: `list[float] | None` — The limits for the x-axis.
  - `y_lim`: `list[float] | None` — The limits for the y-axis.
  - `x_label_angle`: `float` — Angle of the x-axis labels.
  - `y_label_angle`: `float` — Angle of the y-axis labels.
  - `x_axis_labels_visible`: `bool` — Whether to show x-axis labels.
  - `caption`: `str | None` — An optional caption below the plot.
  - `sort`: `'x', 'y', '-x', '-y' | list[str] | None` — Sorting order for the bars.
  - `tooltip`: `'axis', 'none', 'all' | list[str]` — The type of tooltip to show.
  - `height`: `int | None` — Height of the plot.
  - `label`: `str | None` — Label for the component.
  - `show_label`: `bool | None` — Whether to show the label.
  - `container`: `bool` — Whether to wrap the component in a container.
  - `scale`: `int | None` — Scale of the plot.
  - `min_width`: `int` — Minimum width of the component.
  - `inputs`: `Component | list[Component] | set[Component] | None` — The inputs that trigger updates.
  - `visible`: `bool` — Whether the component is visible.
  - `elem_id`: `str | None` — Element ID for the component.
  - `elem_classes`: `list[str] | str | None` — CSS classes for the component.
  - `render`: `bool` — Whether to render the plot.
  - `key`: `int | str | None` — A unique identifier for the component.

#### **Shortcuts:**
- **Class**: `gradio.BarPlot`
- **Interface String**: `"barplot"`
- **Initialization**: Uses default values.

#### **Demos:**
- **Bar Plot Demo:**  
    An example of temperature vs. time, and cuisine rating vs. price.
  ```python
  import pandas as pd
  from random import randint, random
  import gradio as gr

  # Example data
  temp_sensor_data = pd.DataFrame(
      {
          "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
          "temperature": [randint(50 + 10 * (i % 2), 65 + 15 * (i % 2)) for i in range(200)],
          "humidity": [randint(50 + 10 * (i % 2), 65 + 15 * (i % 2)) for i in range(200)],
          "location": ["indoor", "outdoor"] * 100,
      }
  )

  with gr.Blocks() as bar_plots:
      temp_by_time = gr.BarPlot(
          temp_sensor_data,
          x="time",
          y="temperature",
      )
      temp_by_time_location = gr.BarPlot(
          temp_sensor_data,
          x="time",
          y="temperature",
          color="location",
      )
  if __name__ == "__main__":
      bar_plots.launch()
  ```

#### **Event Listeners:**
Event listeners allow you to respond to user interactions with the UI components you've defined in a Gradio Blocks app. When a user interacts with an element, such as changing a slider value or uploading an image, a function is called.

Supported Event Listeners for `BarPlot`:
- **`BarPlot.select(fn, ···)`**: Triggered when the user selects or deselects the plot.
- **`BarPlot.double_click(fn, ···)`**: Triggered when the plot is double-clicked.

#### **Event Parameters:**
- **fn**: Callable function to handle the event.
- **inputs**: Components that trigger the event.
- **outputs**: Components that will be updated as a result.
- **api_name**: The name of the API endpoint.
- **scroll_to_output**: Whether to scroll to the output.
- **show_progress**: Type of progress indication.
- **queue**: Whether to queue the event.
- **batch**: Whether to batch events together.
- **max_batch_size**: Maximum size for batching.
- **preprocess**: Whether to preprocess the input.
- **postprocess**: Whether to postprocess the output.
- **cancels**: A dictionary of events to cancel.
- **trigger_mode**: When to trigger the event.
- **js**: JavaScript code for handling the event.
- **concurrency_limit**: Limit for concurrent events.
- **time_limit**: Time limit for the event.
- **stream_every**: Interval for streaming events.
- **like_user_message**: Whether the event should behave like a user message.

#### **Helper Classes:**
- **WaveformOptions**:  
   A dataclass for specifying options for the waveform display in the BarPlot component (for visualizations involving audio data).

---

 