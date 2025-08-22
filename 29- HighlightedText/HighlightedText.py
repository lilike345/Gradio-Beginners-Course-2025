'''
The HighlightedText component in Gradio is designed to display text where specific parts of the text are highlighted 
based on categories or numerical values. This can be particularly useful for tasks such as part-of-speech tagging, 
named entity recognition, or sentiment analysis where different words or phrases need to be visually categorized.
'''

# 1. Basic Usage as Output Component

import gradio as gr

def tag_text(text):
    tags = [("The", "ARTICLE"), ("quick", "ADJECTIVE"), ("brown", "ADJECTIVE"), 
            ("fox", "NOUN"), ("jumps", "VERB"), ("over", "PREPOSITION"), 
            ("the", "ARTICLE"), ("lazy", "ADJECTIVE"), ("dog", "NOUN")]
    return tags

demo = gr.Interface(
    fn=tag_text,
    inputs=gr.Textbox(label="Input Text", value="The quick brown fox jumps over the lazy dog."),
    outputs=gr.HighlightedText(label="Highlighted Text", show_legend=True, color_map={"ARTICLE": "blue", "ADJECTIVE": "green", "NOUN": "orange", "VERB": "red", "PREPOSITION": "purple"})
)
demo.launch()


# (-------------------------------------------------------------------------------------------------)

# 2. Using a Dictionary for Output

import gradio as gr

def tag_text_dict(text):
    entities = [
        {"entity": "ARTICLE", "start": 0, "end": 3},
        {"entity": "ADJECTIVE", "start": 4, "end": 9},
        {"entity": "ADJECTIVE", "start": 10, "end": 15},
        {"entity": "NOUN", "start": 16, "end": 19},
        {"entity": "VERB", "start": 20, "end": 25},
        {"entity": "PREPOSITION", "start": 26, "end": 30},
        {"entity": "ARTICLE", "start": 31, "end": 34},
        {"entity": "ADJECTIVE", "start": 35, "end": 39},
        {"entity": "NOUN", "start": 40, "end": 43}
    ]
    return {"text": text, "entities": entities}

demo = gr.Interface(
    fn=tag_text_dict,
    inputs=gr.Textbox(label="Input Text", value="The quick brown fox jumps over the lazy dog."),
    outputs=gr.HighlightedText(label="Highlighted Text", show_legend=True, color_map={"ARTICLE": "blue", "ADJECTIVE": "green", "NOUN": "orange", "VERB": "red", "PREPOSITION": "purple"})
)
demo.launch()

# (---------------------------------------------------------------------------------------------------)

# Example 3: Highlighting Differences Between Two Texts

from difflib import Differ
import gradio as gr

def diff_texts(text1, text2):
    d = Differ()
    return [
        (token[2:], token[0] if token[0] != " " else None)
        for token in d.compare(text1, text2)
    ]

demo = gr.Interface(
    fn=diff_texts,
    inputs=[
        gr.Textbox(value="The quick brown fox jumped over the lazy dogs.", label="Text 1"),
        gr.Textbox(value="The fast brown fox jumps over lazy dogs.", label="Text 2"),
    ],
    outputs=gr.HighlightedText(
        color_map={"+": "red", "-": "green"},
        show_legend=True,
        combine_adjacent=True,
    ),
    title="Text Diff",
    description="This demo highlights the differences between two input texts."
)

demo.launch()

# (---------------------------------------------------------------------------------------------------)

# Example 4: Named Entity Recognition (NER)

import gradio as gr

def named_entity_recognition(text):
    # Simulated named entity recognition
    return [
        ("The", None),
        ("quick", None),
        ("brown", None),
        ("fox", "ANIMAL"),
        ("jumps", None),
        ("over", None),
        ("the", None),
        ("lazy", None),
        ("dog", "ANIMAL"),
    ]

demo = gr.Interface(
    fn=named_entity_recognition,
    inputs=gr.Textbox(value="The quick brown fox jumps over the lazy dog."),
    outputs=gr.HighlightedText(
        color_map={"ANIMAL": "blue"},
        show_legend=True,
        combine_adjacent=True,
    ),
    title="Named Entity Recognition",
    description="This demo highlights named entities in the input text."
)

demo.launch()

# (-------------------------------------------------------------------------------------------------------)

# Example 5: Highlighting with Custom Colors

import gradio as gr

def pos_tagging(text):
    # Simulated part-of-speech tagging
    return [
        ("The", "ARTICLE"),
        ("quick", "ADJECTIVE"),
        ("brown", "ADJECTIVE"),
        ("fox", "NOUN"),
        ("jumps", "VERB"),
        ("over", "PREPOSITION"),
        ("the", "ARTICLE"),
        ("lazy", "ADJECTIVE"),
        ("dog", "NOUN"),
    ]

demo = gr.Interface(
    fn=pos_tagging,
    inputs=gr.Textbox(value="The quick brown fox jumps over the lazy dog."),
    outputs=gr.HighlightedText(
        color_map={"ARTICLE": "#0000FF", "ADJECTIVE": "#008000", "NOUN": "#FFA500", "VERB": "#FF0000", "PREPOSITION": "#800080"},
        show_legend=True,
        combine_adjacent=False,
    ),
    title="Part-of-Speech Tagging with Custom Colors",
    description="This demo highlights the part-of-speech tags in the input text with custom colors."
)

demo.launch()

# (---------------------------------------------------------------------------------------------------------)

