
---

### **`gradio.Label`**

#### **Description**
The `gradio.Label` component displays a classification label, and, if provided, the confidence scores of the top categories. It is mostly used to display output and rarely serves as an input component since it doesn't accept direct user input. This component is useful when you want to present results such as predicted class labels or regression outputs along with associated confidence scores.

#### **Behavior**
- **As Input:**
  - When used as an input, it expects the label (either a string, integer, float), or a dictionary containing labels with their respective confidence scores.
  - Your function should accept one of these types:
    ```python
    def predict(value: dict[str, float] | str | int | float | None):
        ...
    ```

- **As Output:**
  - When used as an output, the component expects:
    - A dictionary with labels and confidence scores (i.e., `dict[str, float]`).
    - A string representing just the class label.
    - A numeric value (int or float) for regression outputs.
    - Alternatively, a string path to a `.json` file containing a JSON dictionary in one of the above formats.
  - Your function should return one of these types:
    ```python
    def predict(...) -> dict[str, float] | str | int | float | None:
        ...
    return value
    ```

---

#### **Initialization Parameters**
- **value**: The initial value to be displayed (can be a dictionary, string, float, callable, or `None`).
- **num_top_classes**: The number of top classes to display (if confidence scores are provided).
- **label**: An optional label for the component.
- **show_label**: Whether or not to show the label of the component.
- **inputs**: The components that will be used as inputs for the event.
- **container**: Whether the component is placed inside a container or not.
- **scale**: Controls the scaling of the component.
- **visible**: Controls whether the component is visible.
- **elem_id**: Custom ID for the component's HTML element.
- **elem_classes**: Custom CSS classes for the component.
- **render**: Whether to render the component immediately.
- **color**: An optional color for the label text.
- **show_heading**: Whether to display a heading along with the label.

---

#### **Shortcuts**
- **gr.Label**: `"label"` (Uses default values).

---

#### **Event Listeners**
Event listeners allow for responding to user interactions or function updates. The `gr.Label` component supports the following event listeners:

- **Label.change(fn, ...)**: Triggered when the value of the label changes, either due to user input or a function update. This can be used to track changes to the label and trigger appropriate actions.
  
- **Label.select(fn, ...)**: Triggered when the user selects or deselects the label. It uses the event data (`gradio.SelectData`) to carry the value referring to the label and the selected state. This is useful when you want to capture user actions like selecting/deselecting a label in the UI.

---

#### **Event Parameters**
- **fn**: The function that will handle the event (can also be a decorator).
- **inputs**: The components or blocks that are passed to the event.
- **outputs**: The components or blocks that will receive the output from the event handler.
- **api_name**: The API name for the event (optional).
- **scroll_to_output**: Whether to automatically scroll to the output.
- **show_progress**: Controls the visibility of progress indicators (`'full'`, `'minimal'`, or `'hidden'`).
- **queue**: If enabled, event queueing is used.
- **trigger_mode**: Defines the event trigger behavior (`'once'`, `'multiple'`, or `'always_last'`).
- **js**: JavaScript code to execute for the event.
- **time_limit**: Limits the execution time for the event.
- **stream_every**: Defines the interval for streaming data.
- **cancels**: Specifies events to cancel.

---

### **Summary**
The `gradio.Label` component is primarily used to display classification labels and regression outputs, optionally showing confidence scores for the classes. It is typically used for output but can handle changes to the label or selection actions through event listeners. It is useful when you want to display a label, numerical value, or structured classification result in a clean and simple format. The component also supports event listeners that trigger when the label value changes or when it is selected/deselected.

