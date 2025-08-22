'''
The gr.Plot component in Gradio is designed to display various types of plots generated using popular plotting libraries 
such as Matplotlib, Plotly, Altair, and Bokeh. This component is primarily used as an output component to visualize data 
interactively. Although it can technically accept user input, it's rarely used in that context. Here are some key points 
about the gr.Plot component:
'''

# Example 1: Basic Matplotlib Plot
import matplotlib.pyplot as plt
import gradio as gr

def plot_function():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    return fig

demo = gr.Interface(fn=plot_function, inputs=None, outputs="plot")
demo.launch()

#(-------------------------------------------------------------------------------------------)

# Example 2: Line Plot with Labels and Title
import matplotlib.pyplot as plt
import gradio as gr

def plot_function():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6], label='Line 1')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Simple Line Plot')
    ax.legend()
    return fig

demo = gr.Interface(fn=plot_function, inputs=None, outputs="plot")
demo.launch()

# (-------------------------------------------------------------------------------------------)

# Example 3: Bar Chart
import matplotlib.pyplot as plt
import gradio as gr

def plot_function():
    fig, ax = plt.subplots()
    categories = ['A', 'B', 'C']
    values = [3, 1, 2]
    ax.bar(categories, values, color='blue')
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    ax.set_title('Bar Chart')
    return fig

demo = gr.Interface(fn=plot_function, inputs=None, outputs="plot")
demo.launch()

# (--------------------------------------------------------------------------------------------)

# Example 4: Plot with Multiple Lines
import matplotlib.pyplot as plt
import gradio as gr

def plot_function():
    fig, ax = plt.subplots()
    x = [0.1 * i for i in range(100)]
    y1 = [x_val for x_val in x]
    y2 = [x_val ** 2 for x_val in x]
    ax.plot(x, y1, label='Linear')
    ax.plot(x, y2, label='Quadratic')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Multiple Lines')
    ax.legend()
    return fig

demo = gr.Interface(fn=plot_function, inputs=None, outputs="plot")
demo.launch()

# (---------------------------------------------------------------------------------------------)

# Example 5: Plot with Annotations

import matplotlib.pyplot as plt
import gradio as gr

def plot_function():
    fig, ax = plt.subplots()
    x = [0.1 * i for i in range(100)]
    y = [x_val ** 2 for x_val in x]
    ax.plot(x, y)
    ax.annotate('Start', xy=(0, 0), xytext=(0.5, 10),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.annotate('End', xy=(10, 100), xytext=(5, 80),
                arrowprops=dict(facecolor='black', shrink=0.05))
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Annotated Plot')
    return fig

demo = gr.Interface(fn=plot_function, inputs=None, outputs="plot")
demo.launch()


# (------------------------------------------------------------------------------------------------)

# Example 6: Interactive Sine Wave Plot
import matplotlib.pyplot as plt
import numpy as np
import gradio as gr

def plot_sine_wave(frequency, amplitude, phase_shift, offset):
    # Create a figure with multiple subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    
    # Generate x values
    x = np.linspace(0, 2 * np.pi, 100)
    
    # Calculate y values for the sine wave
    y = amplitude * np.sin(frequency * x + phase_shift) + offset
    
    # Plot the sine wave
    axs[0, 0].plot(x, y, label=f'Amplitude: {amplitude}\nFrequency: {frequency}\nPhase Shift: {phase_shift}\nOffset: {offset}')
    axs[0, 0].set_title('Sine Wave')
    axs[0, 0].set_xlabel('X-axis')
    axs[0, 0].set_ylabel('Y-axis')
    axs[0, 0].legend()
    
    # Plot the sine wave with annotations
    axs[0, 1].plot(x, y, label='Sine Wave')
    axs[0, 1].annotate('Peak', xy=(np.pi / 2, amplitude + offset), xytext=(np.pi / 2, amplitude + offset + 1),
                       arrowprops=dict(facecolor='black', shrink=0.05))
    axs[0, 1].annotate('Trough', xy=(3 * np.pi / 2, -amplitude + offset), xytext=(3 * np.pi / 2, -amplitude + offset - 1),
                       arrowprops=dict(facecolor='black', shrink=0.05))
    axs[0, 1].set_title('Sine Wave with Annotations')
    axs[0, 1].set_xlabel('X-axis')
    axs[0, 1].set_ylabel('Y-axis')
    axs[0, 1].legend()
    
    # Plot the sine wave with a different style
    axs[1, 0].plot(x, y, color='green', linestyle='--', marker='o')
    axs[1, 0].set_title('Styled Sine Wave')
    axs[1, 0].set_xlabel('X-axis')
    axs[1, 0].set_ylabel('Y-axis')
    
    # Plot the sine wave with subplots
    axs[1, 1].plot(x, y, label='Sine Wave')
    axs[1, 1].set_title('Subplot of Sine Wave')
    axs[1, 1].set_xlabel('X-axis')
    axs[1, 1].set_ylabel('Y-axis')
    axs[1, 1].legend()
    
    # Adjust layout
    plt.tight_layout()
    return fig

# Define the Gradio interface
demo = gr.Interface(
    fn=plot_sine_wave,
    inputs=[
        gr.Slider(1, 10, value=1, step=0.1, label="Frequency"),
        gr.Slider(0.1, 2, value=1, step=0.1, label="Amplitude"),
        gr.Slider(0, 2 * np.pi, value=0, step=0.1, label="Phase Shift"),
        gr.Slider(-1, 1, value=0, step=0.1, label="Offset")
    ],
    outputs="plot",
    live=True  # Enable live updates
)

# Launch the Gradio app
demo.launch()
























