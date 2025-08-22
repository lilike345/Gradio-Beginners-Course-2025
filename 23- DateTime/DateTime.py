'''
The DateTime component in Gradio is a versatile tool for selecting dates and times within a user interface. 
It allows users to pick a specific date and optionally a time. The DateTime component can be used both as an 
input and output component in your Gradio interface.

'''

# Example 1: Basic input/output

import gradio as gr
from datetime import datetime

def get_date_label(date):
    return date

demo = gr.Interface(
    fn=get_date_label,
    inputs=gr.DateTime(label="Select a date"),
    outputs=gr.DateTime(label="Selected date"),
    title="Date Label"
)
demo.launch()



# (------------------------------------------------------------------------------)



# Example 2: DateTime Output

import gradio as gr
from datetime import datetime

def get_current_time():
    return datetime.now()

demo = gr.Interface(
    fn=get_current_time,
    inputs=[],
    outputs=gr.DateTime(),
    title="Current Time"
)
demo.launch()


# (-------------------------------------------------------------------------------)

# Example 3: DateTime with Timezone

import gradio as gr
from datetime import datetime
import pytz

def get_timezone_date(timezone):
    return datetime.now(pytz.timezone(timezone))

demo = gr.Interface(
    fn=get_timezone_date,
    inputs=gr.Dropdown(["US/Pacific", "US/Eastern", "Europe/London"]),
    outputs=gr.DateTime(timezone="US/Pacific"),
    title="Timezone Date"
)
demo.launch()

# (-------------------------------------------------------------------------------)

# Example 4: DateTime with Show Label

import gradio as gr
from datetime import datetime

def get_date_show_label(date):
    return date

demo = gr.Interface(
    fn=get_date_show_label,
    inputs=gr.DateTime(show_label=False),
    outputs=gr.DateTime(show_label=True),
    title="Date Show Label"
)
demo.launch()

# (-------------------------------------------------------------------------------)

# Example 5: DateTime with Info

import gradio as gr
from datetime import datetime

def get_date_info(date):
    return date

demo = gr.Interface(
    fn=get_date_info,
    inputs=gr.DateTime(info="Select a date in the format YYYY-MM-DD"),
    outputs=gr.DateTime(info="Selected date in the format YYYY-MM-DD"),
    title="Date Info"
)
demo.launch()


# (-------------------------------------------------------------------------------)

# Example 6: DateTime with Interactive

import gradio as gr
from datetime import datetime

def get_date_interactive(date):
    return date

demo = gr.Interface(
    fn=get_date_interactive,
    inputs=gr.DateTime(interactive=True),
    outputs=gr.DateTime(),
    title="Date Interactive"
)
demo.launch()

# (-------------------------------------------------------------------------------)


