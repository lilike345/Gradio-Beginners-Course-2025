'''
Gradio's LinePlot component is a powerful tool for visualizing data in the form of line plots. It is particularly useful when 
you have time-series data or any data that can be meaningfully plotted on a line graph. The LinePlot component can be used both 
as an input and output component in a Gradio app. When used as an output, it expects a pandas DataFrame with at least two columns, 
one for the x-axis and another for the y-axis.
'''

#Example 1: Basic Line Plot

import pandas as pd
import gradio as gr

# Create a DataFrame
data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", periods=100),
    "temperature": [i % 10 + 20 for i in range(100)]
})

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    gr.LinePlot(data, x="time", y="temperature", title="Temperature Over Time")

demo.launch()

# (------------------------------------------------------------------------------------)

# Example 2: Line Plot with Color Coding

import pandas as pd
import gradio as gr

# Create a DataFrame
data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", periods=100),
    "temperature": [i % 10 + 20 for i in range(100)],
    "location": ["indoor"] * 50 + ["outdoor"] * 50
})

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    gr.LinePlot(data, x="time", y="temperature", color="location", title="Temperature Over Time by Location")

demo.launch()

# (-------------------------------------------------------------------------------------)

# Example 3: Basic Line Plot with NumPy Data

import numpy as np
import pandas as pd
import gradio as gr

# Generate NumPy data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a DataFrame
data = pd.DataFrame({
    "x": x,
    "y": y
})

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    gr.Markdown("## Sine Wave Line Plot")
    plot = gr.LinePlot(data, x="x", y="y", title="Sine Wave Over Time")

demo.launch()

# (----------------------------------------------------------------------------------------)

# Example 4: Line Plot with Custom Color Map

import pandas as pd
import gradio as gr

# Create a DataFrame
data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", periods=100),
    "temperature": [i % 10 + 20 for i in range(100)],
    "location": ["indoor"] * 50 + ["outdoor"] * 50
})

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    gr.LinePlot(data, x="time", y="temperature", color="location", color_map={"indoor": "blue", "outdoor": "red"}, title="Temperature Over Time by Location")

demo.launch()

# (-----------------------------------------------------------------------------------------)

# Example 5: Line Plot with Custom X-Axis Angles

import pandas as pd
import gradio as gr

# Create a DataFrame
data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", periods=100),
    "temperature": [i % 10 + 20 for i in range(100)]
})

# Create a Gradio Blocks app
with gr.Blocks() as demo:
    gr.LinePlot(data, x="time", y="temperature", x_label_angle=45, x_axis_labels_visible=True, title="Temperature Over Time with Custom X-Axis Labels")

demo.launch()

# (-------------------------------------------------------------------------------------------)

