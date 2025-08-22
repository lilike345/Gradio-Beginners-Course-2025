'''
The ScatterPlot component in Gradio is designed to create interactive scatter plots from a pandas DataFrame. 
It can be used to visualize relationships between two continuous variables, with additional options for coloring 
points based on a categorical variable, setting axis limits, and more.
'''

# Example 1: Basic Scatter Plot
import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    'x': range(100),
    'y': [x**2 for x in range(100)]
})

# Gradio interface
with gr.Blocks() as demo:
    scatter_plot = gr.ScatterPlot(data, x='x', y='y', title="Basic Scatter Plot")

demo.launch()

# (--------------------------------------------------------------------------------------------------)

# Example 2: Scatter Plot with Color Coding
import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    'x': range(100),
    'y': [x**2 for x in range(100)],
    'category': ['A' if i < 50 else 'B' for i in range(100)]
})

# Gradio interface
with gr.Blocks() as demo:
    scatter_plot = gr.ScatterPlot(data, x='x', y='y', color='category', title="Color Coded Scatter Plot")

demo.launch()

# (--------------------------------------------------------------------------------------------------)

# Example 3: Setting Axis Limits
import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    'x': range(100),
    'y': [x**2 for x in range(100)]
})

# Gradio interface
with gr.Blocks() as demo:
    scatter_plot = gr.ScatterPlot(data, x='x', y='y', x_lim=[0, 50], y_lim=[0, 2500], title="Axis Limits")

demo.launch()

# (----------------------------------------------------------------------------------------------------)

# Example 4: Rotating Axis Labels
import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    'x': range(100),
    'y': [x**2 for x in range(100)]
})

# Gradio interface
with gr.Blocks() as demo:
    scatter_plot = gr.ScatterPlot(data, x='x', y='y', x_label_angle=45, y_label_angle=45, title="Rotated Axis Labels")

demo.launch()

# (------------------------------------------------------------------------------------------------------)

# Example 5: Using Binning
import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    'x': range(100),
    'y': [x**2 for x in range(100)],
    'category': ['A' if i < 50 else 'B' for i in range(100)]
})

# Gradio interface
with gr.Blocks() as demo:
    scatter_plot = gr.ScatterPlot(data, x='x', y='y', x_bin=5, color='category', title="Binning and Aggregation")

demo.launch()

# (-----------------------------------------------------------------------------------------------------------)

# Example 6: Custom Color Mapping
import pandas as pd
import gradio as gr

# Sample data
data = pd.DataFrame({
    'x': range(100),
    'y': [x**2 for x in range(100)],
    'category': ['A' if i < 50 else 'B' for i in range(100)]
})

# Custom color map
color_map = {'A': 'red', 'B': 'blue'}

# Gradio interface
with gr.Blocks() as demo:
    scatter_plot = gr.ScatterPlot(data, x='x', y='y', color='category', color_map=color_map, title="Custom Color Map")

demo.launch()

# (-------------------------------------------------------------------------------------------------------------)


