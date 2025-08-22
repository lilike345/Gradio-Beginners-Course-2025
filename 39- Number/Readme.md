### Number Component

#### gradio.Number(···)

##### Description
The `gradio.Number` component is used to create a numeric input field for users to enter a numeric value (either integer or float). It can also be used to display numeric output in your Gradio interface.

##### Behavior
- **As an Input Component**: It passes the field value as a float or int to the function, depending on the precision defined for the field.
  
    Your function should accept one of these types:
    ```python
    def predict(value: float | int | None):
        ...
    ```

- **As an Output Component**: It expects an integer or float returned from the function and sets the field value to it.
  
    Your function should return one of these types:
    ```python
    def predict(···) -> float | int | None:
        ...
        return value
    ```

##### Initialization Parameters
- `value`: (float | Callable | None) – The initial value to display.
- `label`: (str | None) – Label for the field.
- `info`: (str | None) – Information or description to display with the component.
- `every`: (Timer | float | None) – Interval between updates.
- `inputs`: (Component | list[Component] | set[Component] | None) – Inputs for the component.
- `show_label`: (bool | None) – Whether to show the label.
- `container`: (bool) – Whether the component is placed inside a container.
- `scale`: (int | None) – Scale factor for the component.
- `min_width`: (int) – Minimum width of the component.
- `interactive`: (bool | None) – Whether the field is interactive.
- `visible`: (bool) – Whether the field is visible.
- `elem_id`: (str | None) – Custom HTML element ID.
- `elem_classes`: (list[str] | str | None) – Custom classes for the element.
- `render`: (bool) – Whether to render the component.
- `key`: (int | str | None) – Key to associate the component with.
- `precision`: (int | None) – Number of decimal places to display.
- `minimum`: (float | None) – Minimum value allowed in the field.
- `maximum`: (float | None) – Maximum value allowed in the field.
- `step`: (float) – Step size for adjusting the value.

##### Shortcuts
- Class: `gradio.Number`
- Interface String Shortcut: `"number"`
- Initialization Uses Default Values

##### Demos
- **Tax Calculator**: Example of using a `Number` field to input income and other related data.
- **Simple Squares**: Demonstrates numeric input and output functionality.

##### Example Code
```python
import gradio as gr

def tax_calculator(income, marital_status, assets):
    tax_brackets = [(10, 0), (25, 8), (60, 12), (120, 20), (250, 30)]
    total_deductible = sum(assets["Cost"])
    taxable_income = income - total_deductible

    total_tax = 0
    for bracket, rate in tax_brackets:
        if taxable_income > bracket:
            total_tax += (taxable_income - bracket) * rate / 100

    if marital_status == "Married":
        total_tax *= 0.75
    elif marital_status == "Divorced":
        total_tax *= 0.8

    return round(total_tax)

demo = gr.Interface(
    tax_calculator,
    [
        gr.Number(),  # Numeric input for income
        gr.Radio(["Single", "Married", "Divorced"]),  # Marital status
        gr.Dataframe(  # Assets DataFrame input
            headers=["Item", "Cost"],
            datatype=["str", "number"],
            label="Assets Purchased this Year",
        ),
    ],
    "number",  # Numeric output for tax calculation
    examples=[  # Example inputs for the demo
        [10000, "Married", [["Suit", 5000], ["Laptop", 800], ["Car", 1800]]],
        [80000, "Single", [["Suit", 800], ["Watch", 1800], ["Car", 800]]],
    ],
)
```

##### Event Listeners
Event listeners in the `Number` component allow you to respond to user interactions.

- `Number.change(fn, ···)`: Triggered when the value of the `Number` changes (either via user input or a function update).
- `Number.input(fn, ···)`: Triggered when the user changes the value.
- `Number.submit(fn, ···)`: Triggered when the user presses the "Enter" key.
- `Number.focus(fn, ···)`: Triggered when the `Number` field is focused.

##### Event Parameters
- `fn`: (Callable | None | Literal['decorator']) – The function to be triggered.
- `inputs`: (Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None) – The input components for the event listener.
- `outputs`: (Component | BlockContext | list[Component | BlockContext] | Set[Component | BlockContext] | None) – The output components for the event listener.
- `api_name`: (str | None | Literal[False]) – API name for the event.
- `scroll_to_output`: (bool) – Whether to scroll to the output after the event.
- `show_progress`: (Literal['full', 'minimal', 'hidden']) – Progress display for the event.
- `queue`: (bool) – Whether to queue the event for processing.
- `batch`: (bool) – Whether to batch the event.
- `max_batch_size`: (int) – Maximum number of events to process in one batch.
- `preprocess`: (bool) – Whether to preprocess input before triggering the event.
- `postprocess`: (bool) – Whether to postprocess output after triggering the event.

