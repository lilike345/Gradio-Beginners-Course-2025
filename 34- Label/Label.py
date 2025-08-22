'''
The Label component in Gradio is used to display classification labels and their corresponding confidence scores. 
It is primarily used as an output component, showing the results of classification tasks or regression outputs. 
The Label component does not accept user input directly but can be dynamically updated through event listeners.
'''

# Example 1: Basic Label Display

import gradio as gr

def predict():
    return "Positive"

iface = gr.Interface(
    fn=predict,
    inputs=None,
    outputs=gr.Label(),
    title="Basic Label Example"
)
iface.launch()

# (-------------------------------------------------------------------------)

# Example 2: Label with Confidence Scores


import gradio as gr

def predict():
    return {"Positive": 0.85, "Negative": 0.15}

iface = gr.Interface(
    fn=predict,
    inputs=None,
    outputs=gr.Label(num_top_classes=2),
    title="Label with Confidence Scores"
)
iface.launch()

# (--------------------------------------------------------------------------)

# Example 3: Update label based on condition

import gradio as gr

def predict(text):
    if "positive" in text.lower():
        return "Positive"
    else:
        return "Negative"

iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.Label(),
    title="Dynamic Label Update"
)
iface.launch()

# (----------------------------------------------------------------------------)

# Example 4: Label with Custom Appearance

import gradio as gr

def predict():
    return {"Positive": 0.85, "Negative": 0.15}

custom_css = """
@import url('https://cdn.tailwindcss.com');

.custom-label {
    @apply text-xl font-bold text-white text-center p-4 rounded-lg shadow-lg 
    bg-gradient-to-r from-purple-600 via-pink-500 to-yellow-500;
    animation: fadeIn 0.8s ease-in-out, colorShift 6s infinite linear;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes colorShift {
    0% { background: linear-gradient(90deg, #6a11cb, #2575fc); }
    25% { background: linear-gradient(90deg, #ff0080, #ff8c00); }
    50% { background: linear-gradient(90deg, #00ff99, #00ccff); }
    75% { background: linear-gradient(90deg, #ffdd00, #ff5500); }
    100% { background: linear-gradient(90deg, #6a11cb, #2575fc); }
}
"""

iface = gr.Interface(
    fn=predict,
    inputs=None,
    outputs=gr.Label(elem_classes=["custom-label"]),
    title="Custom Appearance Label",
    css=custom_css
)

iface.launch()

# (------------------------------------------------------------------------------)

# Example 5: Label with Multiple Outputs
Display multiple labels based on different conditions.

import gradio as gr

def predict(text):
    if "positive" in text.lower():
        return {"Positive": 0.85, "Negative": 0.15}
    elif "negative" in text.lower():
        return {"Positive": 0.15, "Negative": 0.85}
    else:
        return {"Positive": 0.5, "Negative": 0.5}

iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Enter Text"),
    outputs=gr.Label(num_top_classes=2),
    title="Label with Multiple Outputs"
)
iface.launch()