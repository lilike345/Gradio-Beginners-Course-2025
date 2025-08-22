'''

The Gradio Dataframe component is a versatile tool for displaying and interacting with tabular data within a Gradio interface. 
It can be used both as an input component to collect data from users and as an output component to display data. The Dataframe 
supports various data types, including pandas.DataFrame, numpy.array, polars.DataFrame, and native 2D Python lists.


'''


# Example 1: Dataframe with Dropdown Filter

import gradio as gr
import pandas as pd

def filter_data(df, gender):
    return df[df["Gender"] == gender]

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Gender": ["F", "M", "M", "M"]
})

demo = gr.Interface(
    filter_data,
    [
        gr.Dataframe(value=data, headers=["Name", "Age", "Gender"], datatype=["str", "number", "str"], row_count=4, col_count=3),
        gr.Dropdown(["F", "M"], label="Select Gender")
    ],
    gr.Dataframe(type="pandas")
)

demo.launch()

# (------------------------------------------------------------------------------------------------------)

# Example 2: Dataframe with Markdown and HTML Support

import gradio as gr
import pandas as pd

data = pd.DataFrame({
    'Name': ['<b>Alice</b>', '<i>Bob</i>', '<u>Charlie</u>'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

def display_data(df):
    return df

demo = gr.Interface(
    fn=display_data,
    inputs=gr.Dataframe(value=data, datatype=["html", "number", "str"]),
    outputs="dataframe",
    description="Dataframe with markdown and HTML support."
)

demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 3: Dataframe with Search and Filter

import gradio as gr
import pandas as pd

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

def display_data(df):
    return df

demo = gr.Interface(
    fn=display_data,
    inputs=gr.Dataframe(value=data, show_search="filter"),
    outputs="dataframe",
    description="Dataframe with search and filter."
)

demo.launch()

# (-------------------------------------------------------------------------------------------------)

# Example 4: Dataframe with Custom Column Widths

import gradio as gr
import pandas as pd

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

def display_data(df):
    return df

demo = gr.Interface(
    fn=display_data,
    inputs=gr.Dataframe(value=data, column_widths=[100, 50, 150]),
    outputs="dataframe",
    description="Dataframe with custom column widths."
)

demo.launch()

