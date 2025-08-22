### **`gradio.MultimodalTextbox`**

#### **Description**
The `gradio.MultimodalTextbox` component allows users to input text or display string output and simultaneously upload multimedia files. It combines traditional text input with the ability to handle files such as images, audio, and videos, offering a more versatile user interface for both text-based and multimedia content.

#### **Behavior**
- **As Input Component**:
  - Passes both the text value and a list of file(s) as a dictionary to the function.
  - Your function should accept the following type:
    ```python
    def predict(value: MultimodalValue | None):
        ...
    ```

- **As Output Component**:
  - Expects a dictionary with keys `"text"` and `"files"`. Both are optional. The `"files"` value is a list of file paths or URLs.
  - Your function should return one of these types:
    ```python
    def predict(...) -> MultimodalValue | None:
        ...
    return value
    ```

---

#### **Initialization Parameters**
- **value**: The initial string value, a dictionary with string values and file paths, or a callable that returns the value (optional).
- **sources**: A list of sources for multimedia input. Possible values are `'upload'` and `'microphone'`. You can choose one or both (optional).
- **file_types**: A list of accepted file types for upload (optional).
- **file_count**: Defines whether a single file, multiple files, or a directory can be uploaded. Possible values: `'single'`, `'multiple'`, or `'directory'` (optional).
- **lines**: The number of visible lines in the textarea (optional).
- **max_lines**: The maximum number of lines to be displayed (optional).
- **placeholder**: Placeholder text to be shown in the textbox (optional).
- **label**: Label to be displayed above the textbox (optional).
- **info**: Information to display alongside the textbox (optional).
- **every**: A timer value that triggers actions after a certain interval (optional).
- **inputs**: A list or set of components that will trigger the model’s update when interacted with (optional).
- **show_label**: A boolean to indicate if the label should be shown (optional).
- **container**: If `True`, wraps the component in a container (optional).
- **scale**: The scale for the component display (optional).
- **min_width**: The minimum width for the component (optional).
- **interactive**: If `True`, allows user interaction with the component (optional).
- **visible**: Whether the component is visible (optional).
- **elem_id**: HTML element ID for the component (optional).
- **autofocus**: If `True`, sets focus to the component when the app loads (optional).
- **autoscroll**: If `True`, automatically scrolls when the user is typing (optional).
- **elem_classes**: CSS classes to be applied to the component (optional).
- **render**: If `True`, renders the component immediately (optional).
- **key**: Unique key for identifying the component (optional).
- **text_align**: Aligns the text to `'left'` or `'right'` (optional).
- **rtl**: If `True`, sets the text flow to right-to-left (optional).
- **submit_btn**: Customizes the submit button's appearance or sets it to `False` (optional).
- **stop_btn**: Customizes the stop button's appearance or sets it to `False` (optional).
- **max_plain_text_length**: Maximum allowable text length in plain text (optional).

---

#### **Shortcuts**
- **Class**: `gr.MultimodalTextbox`
- **Interface String**: `"multimodaltextbox"`
- **Initialization**: Uses default values unless specified otherwise.

---

#### **Demos**
- **Chatbot Example**: A demo showcasing multimodal input (text, images, audio, etc.) in a chatbot-like interaction.
  - *Example Code Snippet*:
    ```python
    def add_message(history, message):
        for x in message["files"]:
            history.append({"role": "user", "content": {"path": x}})
        if message["text"] is not None:
            history.append({"role": "user", "content": message["text"]})
        return history, gr.MultimodalTextbox(value=None, interactive=False)

    with gr.Blocks() as demo:
        chatbot = gr.Chatbot(elem_id="chatbot")
        chat_input = gr.MultimodalTextbox(interactive=True, file_count="multiple", placeholder="Enter message or upload file...")
    ```

---

#### **Event Listeners**
Event listeners allow you to respond to user interactions with the `MultimodalTextbox` component. Below are the supported event listeners:

- **MultimodalTextbox.change(fn, ...)**:
  - Triggered when the value of the `MultimodalTextbox` changes, either due to user input (e.g., typing) or function updates (e.g., received values from other components).
  - Example use: Updating a model or triggering other components when the content of the textbox changes.

- **MultimodalTextbox.input(fn, ...)**:
  - Triggered when the user manually changes the value of the `MultimodalTextbox`.
  - Example use: Handling user input directly after each change.

- **MultimodalTextbox.select(fn, ...)**:
  - Triggered when the user selects or deselects the `MultimodalTextbox`. Uses `gradio.SelectData` to capture the selected state and label of the textbox.
  - Example use: Reacting when the user interacts with the textbox, either selecting or deselecting it.

- **MultimodalTextbox.submit(fn, ...)**:
  - Triggered when the user presses the Enter key while focused on the `MultimodalTextbox`.
  - Example use: Submitting the text content for further processing when the user hits "Enter."

- **MultimodalTextbox.focus(fn, ...)**:
  - Triggered when the `MultimodalTextbox` gains focus.
  - Example use: Performing actions when the user clicks into the textbox or navigates to it.

- **MultimodalTextbox.blur(fn, ...)**:
  - Triggered when the `MultimodalTextbox` loses focus.
  - Example use: Triggering events or validations after the user moves focus away from the textbox.

- **MultimodalTextbox.stop(fn, ...)**:
  - Triggered when media playback reaches the end in the `MultimodalTextbox`.
  - Example use: Notifying when a multimedia file (e.g., audio or video) finishes playing.

---

#### **Event Parameters**
- **fn**: The function or decorator to handle the event.
- **inputs**: The components or block contexts that trigger the event (optional).
- **outputs**: The components or block contexts that will receive the event output (optional).
- **api_name**: API name for the event (optional).
- **scroll_to_output**: If `True`, scrolls the page to the output after the event is triggered (optional).
- **show_progress**: Controls the visibility of the progress bar (`'full'`, `'minimal'`, `'hidden'`) (optional).
- **queue**: If `True`, event processing will be queued (optional).
- **batch**: If `True`, events are batched (optional).
- **max_batch_size**: Maximum number of events in one batch (optional).
- **preprocess**: If `True`, preprocessing is enabled (optional).
- **postprocess**: If `True`, postprocessing is enabled (optional).
- **cancels**: Defines events that can be canceled (optional).
- **trigger_mode**: Determines when the event is triggered (`'once'`, `'multiple'`, `'always_last'`) (optional).
- **js**: JavaScript code to execute during the event (optional).
- **concurrency_limit**: Limits the number of concurrent executions (optional).
- **show_api**: If `True`, shows API documentation for the event (optional).
- **time_limit**: Sets a time limit for the event (optional).
- **stream_every**: Defines how often data should be streamed during the event (optional).
- **like_user_message**: If `True`, mimics the behavior of user messages in event handling (optional).

---

### **Summary**
The `gradio.MultimodalTextbox` component enhances text input by allowing users to simultaneously input text and upload multimedia files (images, audio, video). It supports a variety of file upload options, such as accepting multiple files or entire directories. The component also includes multiple event listeners to respond to user interactions, such as text input, file uploads, or focus changes. These features make it a powerful component for building interactive applications where both text and multimedia data need to be processed together.