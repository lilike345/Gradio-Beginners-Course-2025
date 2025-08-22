Gradio-ScatterPlot
This repository provides a Gradio component for creating interactive scatter plots, designed for seamless integration into Gradio applications. The component, gradio.ScatterPlot, allows you to visualize data from a pandas DataFrame, making it ideal for exploratory data analysis and building dynamic dashboards.

Key Features
Interactive Visualization: Easily create scatter plots to visualize relationships between numerical variables.

Flexible Data Input: The component accepts a pandas DataFrame as input, making it compatible with a wide range of data sources.

Customization: Control plot aesthetics such as axis titles, colors, and labels.

Event Handling: The component supports event listeners like .select() and .double_click(), enabling you to build responsive applications that react to user interactions.

Usage
Installation
First, make sure you have gradio and pandas installed:

Bash

pip install gradio pandas
Basic Example
To create a simple scatter plot, you just need a pandas DataFrame and to specify the columns for the x and y axes.

Python

import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    "x_values": [1, 2, 3, 4, 5],
    "y_values": [10, 15, 7, 20, 12]
})

with gr.Blocks() as demo:
    gr.ScatterPlot(
        data=data,
        x="x_values",
        y="y_values",
        title="My Simple Scatter Plot",
        label="Data Visualization"
    )

demo.launch()
Advanced Example with Customization
You can customize the plot by specifying colors, titles, and other parameters. The color parameter allows you to add a third dimension to your plot.

Python

import pandas as pd
import gradio as gr
from random import randint, random

# Sample data with color dimension
food_rating_data = pd.DataFrame({
    "cuisine": [["Italian", "Mexican", "Chinese"][i % 3] for i in range(100)],
    "rating": [random() * 4 + 0.5 * (i % 3) for i in range(100)],
    "price": [randint(10, 50) + 4 * (i % 3) for i in range(100)],
    "wait": [random() for i in range(100)],
})

with gr.Blocks() as demo:
    gr.ScatterPlot(
        food_rating_data,
        x="rating",
        y="price",
        color="wait",
        title="Price vs. Rating by Wait Time",
        x_title="Rating",
        y_title="Price ($)",
        color_title="Wait Time (min)"
    )

demo.launch()
Component Reference
gradio.ScatterPlot(···)
Creates a scatter plot component to display data from a pandas DataFrame.

Parameter   Type    Description
value   pd.DataFrame | Callable | None  The data to display.
x   str | None  The name of the column for the x-axis.
y   str | None  The name of the column for the y-axis.
color   str | None  The name of the column for point colors.
title   str | None  The title of the plot.
x_title str | None  The title for the x-axis.
y_title str | None  The title for the y-axis.
tooltip Literal['axis', 'none', 'all'] | list[str]  The columns to show when hovering over a point.

Export to Sheets
For a full list of all parameters, see the official Gradio documentation for gradio.ScatterPlot.

Event Listeners
The ScatterPlot component supports event listeners to make your application more interactive.

.select(): Triggered when a user clicks or selects a data point on the plot. It provides event data about the selected point.

.double_click(): Triggered when the user double-clicks the plot.