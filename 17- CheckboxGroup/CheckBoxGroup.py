'''

The CheckboxGroup component in Gradio is a versatile input/output component that allows users to select multiple options from a list. 
It is particularly useful in scenarios where you need to gather multiple selections from a set of predefined options. For instance, 
it can be used to select multiple countries, interests, or activities from a list. The CheckboxGroup component can be used both as 
an input to pass a set of values to a function and as an output to display pre-selected values.

'''

# Example 1: Basic CheckboxGroup Usage

import gradio as gr

def select_countries(countries):
    return f"You selected: {', '.join(countries)}"

demo = gr.Interface(
    fn=select_countries,
    inputs=gr.CheckboxGroup(choices=["USA", "Japan", "Pakistan"], label="Select Countries"),
    outputs="text"
)

demo.launch()

# (------------------------------------------------------------------------------------------)

# Example 2: Using Indices

import gradio as gr

def select_countries(countries_indices):
    countries = ["USA", "Japan", "Pakistan"]
    selected_countries = [countries[i] for i in countries_indices]
    return f"You selected: {', '.join(selected_countries)}"

demo = gr.Interface(
    fn=select_countries,
    inputs=gr.CheckboxGroup(choices=["USA", "Japan", "Pakistan"], type="index", label="Select Countries"),
    outputs="text"
)

demo.launch()

# (------------------------------------------------------------------------------------------)


# Example 3: Pre-selected Values

import gradio as gr

def select_countries(countries):
    return f"You selected: {', '.join(countries)}"

demo = gr.Interface(
    fn=select_countries,
    inputs=gr.CheckboxGroup(choices=["USA", "Japan", "Pakistan"], value=["USA", "Japan"], label="Select Countries"),
    outputs="text"
)

demo.launch()

# (------------------------------------------------------------------------------------------)

# Example 4: Using Tuples for Choices

import gradio as gr

def select_countries(countries):
    return f"You selected: {', '.join(countries)}"

demo = gr.Interface(
    fn=select_countries,
    inputs=gr.CheckboxGroup(choices=[("USA", "United States"), ("JP", "Japan"), ("PK", "Pakistan")], label="Select Countries"),
    outputs="text"
)

demo.launch()


# (-------------------------------------------------------------------------------------------)


# Example 5: Combining with Other Components

import gradio as gr

def sentence_builder(quantity, animal, countries, place, activity_list, morning):
    return f"""The {quantity} {animal}s from {" and ".join(countries)} went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}"""

demo = gr.Interface(
    sentence_builder,
    [
        gr.Slider(2, 20, value=4, label="Count"),
        gr.Dropdown(["cat", "dog", "bird"], label="Animal"),
        gr.CheckboxGroup(["USA", "Japan", "Pakistan"], label="Countries"),
        gr.Radio(["park", "zoo", "road"], label="Location"),
        gr.Dropdown(["ran", "swam", "ate", "slept"], value=["swam", "slept"], multiselect=True, label="Activity"),
        gr.Checkbox(label="Morning"),
    ],
    "text",
    examples=[
        [2, "cat", ["Japan", "Pakistan"], "park", ["ate", "swam"], True],
        [4, "dog", ["Japan"], "zoo", ["ate", "swam"], False],
        [10, "bird", ["USA", "Pakistan"], "road", ["ran"], False],
        [8, "cat", ["Pakistan"], "zoo", ["ate"], True],
    ]
)

demo.launch()


# (------------------------------------------------------------------------------------------)

# Example 6: CheckboxGroup with Conditional Logic for Recommendations

# In this example, the CheckboxGroup is used to gather user preferences, and based on those preferences, recommendations are generated.

import gradio as gr

def generate_recommendations(preferences):
    recommendations = {
        "music": ["Rock", "Pop", "Jazz", "Classical"],
        "movies": ["Action", "Comedy", "Drama", "Horror"],
        "books": ["Fiction", "Non-Fiction", "Science", "History"]
    }
    
    selected_recommendations = []
    for pref in preferences:
        if pref in recommendations:
            selected_recommendations.extend(recommendations[pref])
    
    return f"Recommended genres: {', '.join(selected_recommendations)}"

with gr.Blocks() as demo:
    preference_checkbox_group = gr.CheckboxGroup(
        choices=["music", "movies", "books"],
        label="Select Your Preferences"
    )
    recommendation_textbox = gr.Textbox(label="Recommendations")

    preference_checkbox_group.change(fn=generate_recommendations, inputs=preference_checkbox_group, outputs=recommendation_textbox)

demo.launch()


























