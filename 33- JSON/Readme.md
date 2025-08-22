
---

### **`gradio.JSON`**

#### **Description**
`gradio.JSON` is a component used to display arbitrary JSON data in a readable, prettified format. It is generally used to display output as JSON but rarely serves as an input component because it doesn’t accept user input directly. It is ideal for situations where you need to show JSON data in a clean, organized way.

#### **Behavior**
- **As Input:**
  - When used as an input, the component passes the JSON data as either a dictionary or a list, depending on the value.
  - Your function should accept one of these types:
    ```python
    def predict(value: dict | list | None):
        ...
    ```

- **As Output:**
  - When used as an output, the component expects a valid JSON string or a dictionary/list that can be serialized into a JSON string. The dictionary or list can also contain `numpy` arrays.
  - Your function should return one of these types:
    ```python
    def predict(...) -> dict | list | str | None:
        ...
    return value
    ```

---

#### **Initialization Parameters**
- **value**: The initial JSON data (either a string, dictionary, list, callable, or `None`).
- **label**: Optionally provides a label for the component.
- **show_label**: Whether to display the label.
- **height**, **min_height**, **max_height**: Define the height of the JSON output display.
- **show_indices**: Whether to show the indices of list items in the JSON.
- **visible**: Control the visibility of the component.
- **open**: Whether the JSON output is initially expanded or collapsed.
- **inputs**: Define the inputs for the component.
- **scale**: Adjusts the size of the component.
- **elem_id**: Assigns a custom ID to the element.
- **elem_classes**: Allows for custom CSS classes.
- **container**: Whether the component should be placed inside a container.
- **render**: Whether to render the component immediately.

---

#### **Shortcuts**
- **gr.JSON**: `"json"` (Uses default values).

---

#### **Demos**

- **Zip to JSON Example:**
    ```python
    from zipfile import ZipFile
    import gradio as gr

    def zip_to_json(file_obj):
        files = []
        with ZipFile(file_obj.name) as zfile:
            for zinfo in zfile.infolist():
                files.append(
                    {
                        "name": zinfo.filename,
                        "file_size": zinfo.file_size,
                        "compressed_size": zinfo.compress_size,
                    }
                )
        return files

    demo = gr.Interface(zip_to_json, "file", "json")

    if __name__ == "__main__":
        demo.launch()
    ```

In this example, a ZIP file is uploaded, and the details of the files within it are displayed in JSON format.

---

#### **Event Listeners**
Event listeners in Gradio allow you to respond to user actions within the app. The `gr.JSON` component supports the following event listener:

- **JSON.change(fn, ...)**: Triggered when the value of the JSON component changes, either from user input or a function update (e.g., updating the JSON data programmatically). This is similar to the `.input()` listener but can be triggered by changes made by functions as well.

---

#### **Event Parameters**
- **fn**: The function to handle the event.
- **inputs**: The components or blocks to be passed to the event.
- **outputs**: The components or blocks that will receive the output from the event handler.
- **api_name**: API name for the event (optional).
- **scroll_to_output**: Whether to scroll to the output after the event.
- **show_progress**: Defines the visibility of the progress (`'full'`, `'minimal'`, or `'hidden'`).
- **queue**: Whether to enable event queueing.
- **trigger_mode**: Defines the event trigger behavior (`'once'`, `'multiple'`, or `'always_last'`).
- **js**: JavaScript code to run for the event.
- **time_limit**: Limit the execution time for the event.
- **stream_every**: Interval for streaming data.

---

### **Summary**
`gradio.JSON` is a simple yet powerful component for displaying JSON data in a well-formatted way. It is primarily used to show structured data and is useful for scenarios where you need to present JSON output in a user-friendly manner. It supports event listeners that respond to changes in JSON values, enabling dynamic interactions within a Gradio app.