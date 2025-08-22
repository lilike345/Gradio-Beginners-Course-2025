### **Plot Component in Gradio**

#### **`gradio.Plot(···)`**

##### **Description**
The `gradio.Plot` component is used to display various types of plots, supporting **Matplotlib**, **Plotly**, **Altair**, and **Bokeh** visualizations. Since it does not accept user input, it is **rarely used as an input component**.

##### **Behavior**
- **As an Input Component** (Rarely Used):
  - Passes the displayed plot data as a `PlotData` **dataclass**, which includes:
    - The **plot information** as a JSON string.
    - The **chart type**.
    - The **plotting library**.

  **Example function signature:**
  ```python
  def predict(value: PlotData | None):
      ...
  ```

- **As an Output Component**:
  - Accepts the following types of plots:
    - **Matplotlib** → `matplotlib.Figure`
    - **Bokeh** → `bokeh.Model`
    - **Plotly** → `plotly.Figure`
    - **Altair** → `altair.Chart`

  **Example function signature:**
  ```python
  def predict(···) -> Any:
      ...
      return value
  ```

---

### **Initialization Parameters**

| Parameter       | Type                                            | Description |
|----------------|-------------------------------------------------|-------------|
| `value`        | `Any | None`                                    | The initial plot to display (optional). |
| `format`       | `str`                                           | The format of the plot data. |
| `label`        | `str | None`                                    | Label for the plot. |
| `every`        | `Timer | float | None`                          | Interval for automatic updates. |
| `inputs`       | `Component | list[Component] | set[Component] | None` | Inputs for the component. |
| `show_label`   | `bool | None`                                   | Whether to show the label. |
| `container`    | `bool`                                          | Whether to wrap the component in a container. |
| `scale`        | `int | None`                                    | Scaling factor for the component size. |
| `min_width`    | `int`                                           | Minimum width of the plot. |
| `visible`      | `bool`                                          | Whether the component is visible. |
| `elem_id`      | `str | None`                                    | Custom ID for the component. |
| `elem_classes` | `list[str] | str | None`                        | CSS classes for styling. |
| `render`       | `bool`                                          | Whether to render the component. |
| `key`          | `int | str | None`                              | Unique identifier for referencing the component. |

---

### **Shortcuts**
- **Class:** `gradio.Plot`
- **Interface String Shortcut:** `"plot"`
- **Initialization:** Uses default values.

---

### **Example Usage**

#### **Example 1: Displaying a Matplotlib Plot**
```python
import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

def generate_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, label="Sine Wave")
    ax.legend()
    
    return fig

demo = gr.Interface(
    fn=generate_plot,
    inputs=[],
    outputs=gr.Plot(label="Sine Wave Plot")
)

demo.launch()
```

---

#### **Example 2: Interactive Projectile Motion Plot using Plotly**
```python
import gradio as gr
import plotly.graph_objects as go
import numpy as np

def projectile_motion(v, a):
    g = 9.81  # Gravity (m/s²)
    theta = np.radians(a)
    t_max = (2 * v * np.sin(theta)) / g
    t = np.linspace(0, t_max, num=50)

    x = v * np.cos(theta) * t
    y = (v * np.sin(theta) * t) - (0.5 * g * t**2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Projectile Path"))
    fig.update_layout(
        title="Projectile Motion",
        xaxis_title="Distance (m)",
        yaxis_title="Height (m)",
        template="plotly_dark"
    )

    return fig

with gr.Blocks() as demo:
    gr.Markdown("### Projectile Motion Simulator")
    with gr.Row():
        speed = gr.Slider(1, 50, 25, label="Speed (m/s)")
        angle = gr.Slider(0, 90, 45, label="Angle (°)")
    output = gr.Plot()
    button = gr.Button("Simulate")

    button.click(fn=projectile_motion, inputs=[speed, angle], outputs=output)

demo.launch()
```

---

### **Event Listeners**
Event listeners allow you to trigger functions based on user interactions with the `Plot` component.

| Listener              | Description |
|-----------------------|-------------|
| `Plot.change(fn, ···)`  | Triggered when the plot value changes (e.g., due to a function update). |
| `Plot.clear(fn, ···)`   | Triggered when the user clears the plot. |

---

### **Event Parameters**

| Parameter         | Type  | Description |
|------------------|------------------------------------------------------|-------------|
| `fn`            | `Callable | None | Literal['decorator']`              | The function to be triggered by the event. |
| `inputs`        | `Component | BlockContext | list[Component | BlockContext] | set[Component | BlockContext] | None` | The input components. |
| `outputs`       | `Component | BlockContext | list[Component | BlockContext] | set[Component | BlockContext] | None` | The output components. |
| `api_name`      | `str | None | Literal[False]`                        | Name of the API for the event. |
| `scroll_to_output` | `bool`                                           | Whether to scroll to the output after the event. |
| `show_progress` | `Literal['full', 'minimal', 'hidden']`               | Progress bar display setting. |
| `queue`         | `bool`                                              | Whether to queue the event. |
| `batch`         | `bool`                                              | Whether to batch process the event. |
| `max_batch_size` | `int`                                              | Maximum number of items in a batch. |
| `preprocess`    | `bool`                                              | Whether to preprocess inputs before triggering. |
| `postprocess`   | `bool`                                              | Whether to postprocess outputs after triggering. |

---

### **Summary**
- `gradio.Plot` is used to **display** plots from **Matplotlib, Plotly, Altair, and Bokeh**.
- **Not commonly used as an input component**.
- Accepts a variety of visualization libraries as output.
- Supports **event listeners** (`change`, `clear`).
- Can be used interactively with **sliders, buttons, and other UI elements**.

Would you like an example integrating `gradio.Plot` with **real-time data updates**? 🚀