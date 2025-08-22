
---

### **`gradio.LinePlot`**

#### **Description**
The `gradio.LinePlot` component is used to create a line plot that displays data from a pandas DataFrame. It visualizes data by plotting points connected with lines. The component is designed for showing trends over time or other continuous variables, making it useful for time-series data or data with a clear sequence.

#### **Behavior**
- **As Input Component:**
  - The input should be an `AltairPlotData` object or `None`. Typically, you'll provide the plot data as a pandas DataFrame, which includes at least two columns—one for the x-axis (the independent variable) and one for the y-axis (the dependent variable).
  - Your function should accept:
    ```python
    def predict(value: AltairPlotData | None):
        ...
    ```

- **As Output Component:**
  - Expects a pandas DataFrame containing the data to display in the line plot. The DataFrame must have at least two columns—one for the x-axis (`x`) and one for the y-axis (`y`).
  - Your function should return one of these types:
    ```python
    def predict(...) -> pd.DataFrame | dict | None:
        ...
    return value
    ```

---

#### **Initialization Parameters**
- **value**: A pandas DataFrame or callable (optional), used to provide the data for the line plot.
- **x**: The name of the column in the DataFrame to be used for the x-axis (optional).
- **y**: The name of the column in the DataFrame to be used for the y-axis (optional).
- **color**: A column name for color coding the data points (optional).
- **title**: The title of the plot (optional).
- **x_title**: The title for the x-axis (optional).
- **y_title**: The title for the y-axis (optional).
- **color_title**: The title for the color legend (optional).
- **x_bin**: Bin size for the x-axis, which can be a string or float (optional).
- **y_aggregate**: Aggregation method for the y-axis (options include `'sum'`, `'mean'`, `'median'`, `'min'`, `'max'`, `'count'`) (optional).
- **color_map**: A dictionary mapping color values to labels (optional).
- **x_lim**: The limits for the x-axis (optional).
- **y_lim**: The limits for the y-axis (optional).
- **x_label_angle**: The angle at which x-axis labels are rotated (optional).
- **y_label_angle**: The angle at which y-axis labels are rotated (optional).
- **x_axis_labels_visible**: Whether to show x-axis labels (optional).
- **caption**: A caption for the plot (optional).
- **sort**: Sorting order for the plot (`'x'`, `'y'`, `'-x'`, `'-y'`, or a list of sorting methods) (optional).
- **tooltip**: Defines which tooltips to show (`'axis'`, `'none'`, `'all'`, or a list of strings) (optional).
- **height**: The height of the plot (optional).
- **label**: The label for the plot (optional).
- **show_label**: Whether to display the label (optional).
- **inputs**: The input components to trigger plot updates (optional).
- **container**: Whether the component should be placed inside a container (optional).
- **scale**: Scaling factor for the plot (optional).
- **min_width**: The minimum width of the plot (optional).
- **visible**: Whether the plot is visible (optional).
- **elem_id**: Custom ID for the component's HTML element (optional).
- **elem_classes**: Custom CSS classes for the component (optional).
- **render**: Whether to immediately render the plot (optional).
- **key**: A custom key for identifying the plot (optional).

---

#### **Shortcuts**
- **gr.LinePlot**: `"lineplot"` (Uses default values).

---

#### **Event Listeners**
Event listeners allow you to respond to user interactions with the plot. The `gr.LinePlot` component supports the following event listeners:

- **LinePlot.select(fn, ...)**: Triggered when the user selects or deselects the line plot. It uses `gradio.SelectData` to carry the value referring to the label of the plot and the selected state. This is useful for capturing user selection actions.
  
- **LinePlot.double_click(fn, ...)**: Triggered when the plot is double-clicked, allowing you to execute a function in response to this interaction.

---

#### **Event Parameters**
- **fn**: The function that will handle the event (can also be a decorator).
- **inputs**: The components or blocks that are passed to the event.
- **outputs**: The components or blocks that will receive the output from the event handler.
- **api_name**: The API name for the event (optional).
- **scroll_to_output**: Whether to automatically scroll to the output.
- **show_progress**: Controls the visibility of progress indicators (`'full'`, `'minimal'`, or `'hidden'`).
- **queue**: If enabled, event queueing is used.
- **trigger_mode**: Defines the event trigger behavior (`'once'`, `'multiple'`, or `'always_last'`).
- **js**: JavaScript code to execute for the event.
- **time_limit**: Limits the execution time for the event.
- **stream_every**: Defines the interval for streaming data.
- **cancels**: Specifies events to cancel.

---

### **Summary**
The `gradio.LinePlot` component is ideal for visualizing data trends, particularly with time-series or sequential data. It accepts a pandas DataFrame as input, where at least two columns represent the x and y axes. It supports a range of customization options for labels, axis titles, aggregation methods, color coding, and tooltips. Event listeners allow for user interactions such as selecting or double-clicking on the plot, making it interactive for a more dynamic user experience.