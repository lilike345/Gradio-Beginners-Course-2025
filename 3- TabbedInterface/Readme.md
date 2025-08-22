# Gradio TabbedInterface 

## Overview

The `gr.TabbedInterface` class in Gradio allows you to create an interface with multiple tabs. Each tab is linked to a separate `Interface` or `Block` that will be rendered individually. You can provide a list of interfaces or blocks that each correspond to a tab. This feature is useful when you want to organize your application into distinct sections, each with its own functionality, without cluttering the interface.

### Key Notes:
- Each interface or block gets its own tab in the layout.
- Only the components from the respective interface or block will be rendered in each tab.
- Certain high-level attributes (e.g., custom CSS, JavaScript, and head attributes) from the blocks or interfaces may not be applied to each individual tab.

## Example Usage

### Basic Example: Tabbed Interface with "Hello World" and "Bye World"

This simple example demonstrates how to use the `gr.TabbedInterface` with two separate interfaces: one that greets the user and another that bids them farewell.

```python
import gradio as gr

hello_world = gr.Interface(lambda name: "Hello " + name, "text", "text")
bye_world = gr.Interface(lambda name: "Bye " + name, "text", "text")

demo = gr.TabbedInterface([hello_world, bye_world], ["Hello World", "Bye World"])

if __name__ == "__main__":
    demo.launch()
```

In this example:
- `hello_world` is an interface where the user can enter their name, and the chatbot responds with a greeting.
- `bye_world` is another interface where the chatbot says goodbye to the user.
- These interfaces are wrapped in a `gr.TabbedInterface` with tabs labeled "Hello World" and "Bye World".

### Customizing Tab Names

You can customize the names of the tabs by providing a list of strings for the `tab_names` parameter.

```python
tab_names = ["Greetings", "Farewell"]
demo = gr.TabbedInterface([hello_world, bye_world], tab_names)
demo.launch()
```

This will display the tabs with custom names ("Greetings" and "Farewell") instead of the default names.

## Parameters

### Main Parameters

- **interface_list**: `list[Blocks]`  
  A list of Gradio interfaces or blocks that will be rendered in separate tabs. Each interface or block will correspond to one tab.

- **tab_names**: `list[str] | None`  
  A list of strings used to label the tabs. If not provided, the default labels (e.g., "Tab 1", "Tab 2") are used.

- **title**: `str | None`  
  The title of the tabbed interface, which is shown on the web page.

- **theme**: `Theme | str | None`  
  The theme of the tabbed interface (e.g., "dark", "light"). It controls the overall visual style.

- **analytics_enabled**: `bool | None`  
  Whether or not to collect analytics data from users interacting with the interface.

- **css**: `str | None`  
  Custom CSS to style the tabbed interface.

- **js**: `str | None`  
  Custom JavaScript to add interactivity or modify the behavior of the interface.

- **head**: `str | None`  
  Custom HTML or metadata to include in the header of the page.

### Example Use Cases

1. **Tabbed Layout for Multiple Functionalities**:
   - Use `gr.TabbedInterface` to organize your application into logical sections, where each section provides different functionalities. For example, you might have a "Text Classification" tab, a "Translation" tab, and a "Sentiment Analysis" tab.

2. **Organizing Visuals and Interactions**:
   - You can display separate charts, visualizations, or even models in different tabs to avoid overwhelming users with too much information in a single view.

3. **User Education**:
   - If you want to provide educational content or documentation alongside interactive tools, you could use tabs to separate guides, tutorials, and Q&A sections.

## Demos

- **tabbed_interface_lite**: A minimalistic example where two simple interfaces are shown in different tabs (e.g., "Hello World" and "Goodbye World").

## Conclusion

`gr.TabbedInterface` provides an excellent way to organize a complex Gradio interface into multiple tabs, allowing users to interact with distinct functionalities without cluttering the interface. By utilizing this component, you can create more structured and user-friendly interfaces for your machine learning models or web applications.