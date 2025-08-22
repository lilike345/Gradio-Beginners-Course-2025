import gradio as gr
import pandas as pd
from random import randint

temp_sensor_data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
    "temperature": [randint(50 + 10 * (i % 2), 65 + 15 * (i % 2)) for i in range(200)],
})

def plot_temperature(dataframe):
    return dataframe

with gr.Blocks() as demo:
    gr.Markdown("## Temperature Data Over Time")
    plot = gr.BarPlot(temp_sensor_data, x="time", y="temperature", title="Temperature Over Time")

demo.launch()

# (-----------------------------------------------------------------------------------------------)

import gradio as gr
import pandas as pd
from random import random

food_rating_data = pd.DataFrame({
    "cuisine":[["Italian", "Mexican", "Chinese"][i%3] for i in range(100)],
    "rating": [random() * 4 + 0.5 * (i%3) for i in range(100)],
})

def plot_ratings(dataframe):
    return dataframe

with gr.Blocks() as demo:
    gr.Markdown("## Food Ratings by Cuisine")
    plot = gr.BarPlot(food_rating_data, x = "cuisine", y="rating", title="Food Ratings")

demo.launch()

# (-----------------------------------------------------------------------------------------------)

import pandas as pd
import gradio as gr

temp_sensor_data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
    "temperature": [randint(50 + 10 * (i % 2), 65 + 15 * (i % 2)) for i in range(200)],
    "location": ["indoor", "outdoor"] * 100,
})

def plot_temperature(dataframe):
    return dataframe

with gr.Blocks() as demo:
    gr.Markdown("## Temperature Data Over Time by Location")
    plot = gr.BarPlot(temp_sensor_data, x="time", y="temperature", color="location", title="Temperature Over Time by Location")

demo.launch()

# (-------------------------------------------------------------------------------------------------)

import gradio as gr
import pandas as pd

temp_sensor_data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
    "temperature": [randint(50 + 10 *(i%2), 65 + 15 *(i%2)) for i in range(200)],
})

def plot_temperature(dataframe):
    return dataframe

with gr.Blocks() as demo:
    gr.Markdown("## Temperature Data Over Time")
    plot = gr.BarPlot(temp_sensor_data, x="time", y="temperature", title="Temperature Data Over Time", x_title="Date", y_title="Temperature (F)")

demo.launch()

# (-------------------------------------------------------------------------------------------------)

import gradio as gr
import pandas as pd

temp_sensor_data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
    "temperature": [randint(50 + 10*(i%2), 65 + 15 *(i%2)) for i in range(200)],
    "location":["indoor", "outdoor"] * 100,
})

def plot_temperature(dataframe):
    return dataframe

with gr.Blocks() as demo:
    color_map = {"indoor": "green", "outdoor": "red"}
    gr.Markdown("## Temperature Data Over Time by Location")
    plot = gr.BarPlot(temp_sensor_data, x="time", y="temperature", color="location", color_map=color_map, title="Temperature Over Time by Location")

demo.launch()

# (-------------------------------------------------------------------------------------------------)

import gradio as gr
import pandas as pd

temp_sensor_data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
    "temperature":[randint(50 + 10 *(i%2), 65 + 15 *(i%2)) for i in range(200)],
})

def plot_temperature(dataframe):
    return dataframe

with gr.Blocks() as demo:
    gr.Markdown("## Temperature Data Over Time")
    plot = gr.BarPlot(temp_sensor_data, x="time", y="temperature", y_lim=[50, 80], title="Temperature Over Time")

demo.launch()

# (----------------------------------------------------------------------------------------------------)


import gradio as gr
import pandas as pd

temp_sensor_data = pd.DataFrame({
    "time": pd.date_range("2021-01-01", end="2021-01-05", periods=200),
    "temperature":[randint(50 + 10 *(i%2), 65 + 15 *(i%2)) for i in range(200)],
})

def plot_temperature(dataframe):
    return dataframe

with gr.Blocks() as demo:
    gr.Markdown("## Temperature Data Over Time")
    plot = gr.BarPlot(temp_sensor_data, x="time",x_label_angle=45, y_label_angle=45, y="temperature", y_lim=[50, 80], title="Temperature Over Time")

demo.launch()


# (---------------------------------------------------------------------------------------------------)


































































