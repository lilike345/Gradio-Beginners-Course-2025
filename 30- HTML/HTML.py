'''
The gradio.HTML component is used to display arbitrary HTML content within a Gradio interface. It is primarily used 
as an output component to render HTML content dynamically based on user interactions or other events in the Gradio app. 
Since it does not accept user input, it is rarely used as an input component.
'''

# Example 1: Basic HTML Content

import gradio as gr

def display_html():
    return "<p><h1>Hello, Gradio!</h1></p>"

demo = gr.Interface(
    fn=display_html,
    inputs=None,
    outputs=gr.HTML()
)

demo.launch()

# (---------------------------------------------------------------------------------------------)

# Example 2: Embedding an Image

import gradio as gr

def display_image():
    return "<img src='https://cdn.pixabay.com/photo/2016/11/22/23/55/car-1851299_1280.jpg' alt='Placeholder Image'>"

demo = gr.Interface(
    fn=display_image,
    inputs=None,
    outputs=gr.HTML()
)

demo.launch()

# (------------------------------------------------------------------------------------------------)

# Example 3: Embedding a YouTube Video

import gradio as gr

def display_video():
    return "<iframe width='560' height='315' src='https://www.youtube.com/embed/98_cpngbUv0' frameborder='0' allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>"

demo = gr.Interface(
    fn=display_video,
    inputs=None,
    outputs=gr.HTML()
)

demo.launch()

# (-------------------------------------------------------------------------------------------------)

# Example 4: Creating a Responsive Layout with CSS Grid
import gradio as gr

def display_grid_layout():
    return """
    <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;'>
        <div style='background-color: lightblue; padding: 20px;'>Column 1</div>
        <div style='background-color: lightgreen; padding: 20px;'>Column 2</div>
        <div style='background-color: lightcoral; padding: 20px;'>Column 3</div>
        <div style='background-color: lightyellow; padding: 20px;'>Column 4</div>
        <div style='background-color: lightpink; padding: 20px;'>Column 5</div>
        <div style='background-color: lightgray; padding: 20px;'>Column 6</div>
    </div>
    """

demo = gr.Interface(
    fn=display_grid_layout,
    inputs=None,
    outputs=gr.HTML()
)

demo.launch()

# (-------------------------------------------------------------------------------------------------)

# Example 5: Using Advance CSS for Styling

import gradio as gr

def display_styled_html():
    return """
    <style>
      @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
      }

      @keyframes borderGlow {
        0% { box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.5); }
        50% { box-shadow: 0px 0px 30px rgba(0, 255, 255, 1); }
        100% { box-shadow: 0px 0px 10px rgba(0, 255, 255, 0.5); }
      }

      @keyframes textPulse {
        0% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
        100% { transform: scale(1); opacity: 0.8; }
      }

      .styled-content {
        background: linear-gradient(45deg, #ff416c, #ff4b2b, #1fddff, #23d5ab);
        background-size: 300% 300%;
        animation: gradientMove 6s infinite alternate ease-in-out;
        padding: 20px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: white;
        border-radius: 15px;
        border: 3px solid #ffffff;
        animation: borderGlow 3s infinite alternate ease-in-out;
      }

      .styled-content:hover {
        animation: textPulse 1.5s infinite ease-in-out;
      }
    </style>
    <div class="styled-content">Styled HTML Content</div>
    """

demo = gr.Interface(
    fn=display_styled_html,
    inputs=None,
    outputs=gr.HTML()
)

demo.launch()


# (---------------------------------------------------------------------------------------------------)

# Example 6 : Creating an Interactive Slider with JavaScript

import gradio as gr

def display_slider_html():
    return """
    <div>
        <input type="range" id="slider" min="0" max="100" value="50" oninput="updateValue()">
        <p id="sliderValue">Value: 50</p>
        <script>
        function updateValue() {
            var slider = document.getElementById('slider');
            var valueDisplay = document.getElementById('sliderValue');
            valueDisplay.innerHTML = 'Value: ' + slider.value;
        }
        </script>
    </div>
    """

demo = gr.Interface(
    fn=display_slider_html,
    inputs=None,
    outputs=gr.HTML()
)

demo.launch()