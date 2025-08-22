### **`gradio.Model3D`**

#### **Description**
The `gradio.Model3D` component allows users to upload or view 3D model files in formats such as `.obj`, `.glb`, `.stl`, `.gltf`, `.splat`, or `.ply`. It offers an interactive environment for visualizing and manipulating 3D models directly in a Gradio interface.

#### **Behavior**
- **As Input Component**:
  - Accepts an uploaded 3D model file and passes the file path (as a string) to the function.
  - Your function should accept the following types:
    ```python
    def predict(value: str | None):
        ...
    ```

- **As Output Component**:
  - Expects the function to return a string or `pathlib.Path` object representing the file path of the 3D model to be rendered. This could be any of the supported 3D model formats (`.obj`, `.glb`, `.stl`, `.gltf`).
  - Your function should return one of these types:
    ```python
    def predict(...) -> str | Path | None:
        ...
    return value
    ```

---

#### **Initialization Parameters**
- **value**: The path to the 3D model file, or a callable returning the file path (optional).
- **display_mode**: The mode used to display the 3D model. It could be:
  - `'solid'` (default): A solid model rendering.
  - `'point_cloud'`: Displays the model as a collection of points.
  - `'wireframe'`: Displays the model as a wireframe (optional).
- **clear_color**: A tuple of RGBA values defining the background color for the 3D scene (optional).
- **camera_position**: A tuple specifying the camera position in the 3D space. It contains values for the x, y, and z positions (optional).
- **zoom_speed**: Controls the speed of zooming in and out on the model (optional).
- **pan_speed**: Controls the speed of panning the 3D model (optional).
- **height**: The height of the 3D component (optional).
- **label**: A label to display alongside the 3D model (optional).
- **show_label**: A boolean indicating whether to show the label (optional).
- **every**: A timer value (optional).
- **inputs**: A list or set of components that will trigger the model's update when interacted with (optional).
- **container**: If `True`, the component is contained in a wrapper (optional).
- **scale**: Defines the scale for the 3D model display (optional).
- **min_width**: The minimum width of the component (optional).
- **interactive**: Whether the model can be interactively manipulated (optional).
- **visible**: If `True`, the component will be visible (optional).
- **elem_id**: The HTML element ID for the 3D model (optional).
- **elem_classes**: CSS classes to apply to the component (optional).
- **render**: If `True`, renders the model immediately (optional).
- **key**: A unique identifier for the component (optional).

---

#### **Shortcuts**
- **Class**: `gr.Model3D`
- **Interface String**: `"model3d"`
- **Initialization**: Uses default values unless specified otherwise.

---

#### **Event Listeners**
Event listeners enable the application to respond to user interactions with the `Model3D` component. Below are the supported event listeners for this component:

- **Model3D.change(fn, ...)**:
  - Triggered when the value of the 3D model changes due to user input (e.g., changing the model's view) or function updates (e.g., model is updated programmatically).
  - Example use: Updating a 3D model view when a user adjusts a slider.

- **Model3D.upload(fn, ...)**:
  - Triggered when the user uploads a new 3D model file.
  - Example use: Automatically update the model view when a user uploads a new model.

- **Model3D.edit(fn, ...)**:
  - Triggered when the user edits the 3D model (e.g., using built-in editing tools).
  - Example use: Responding to a user modifying the model with a tool.

- **Model3D.clear(fn, ...)**:
  - Triggered when the user clears the model using the built-in "clear" button.
  - Example use: Resetting any changes made to the 3D model when cleared.

---

#### **Event Parameters**
- **fn**: A callable function or decorator to execute when the event is triggered.
- **inputs**: Components or block contexts that trigger the event (optional).
- **outputs**: Components or block contexts that will receive the output of the event (optional).
- **api_name**: The API name for the event (optional).
- **scroll_to_output**: If `True`, scrolls the page to the output (optional).
- **show_progress**: Controls the progress display mode: `'full'`, `'minimal'`, or `'hidden'` (optional).
- **queue**: If `True`, enables queuing for events (optional).
- **batch**: If `True`, events are batched together (optional).
- **max_batch_size**: Maximum number of events in a batch (optional).
- **preprocess**: If `True`, input preprocessing is enabled (optional).
- **postprocess**: If `True`, output postprocessing is enabled (optional).
- **cancels**: Defines events that can be canceled (optional).
- **trigger_mode**: Defines when the event is triggered (`'once'`, `'multiple'`, `'always_last'`) (optional).
- **js**: JavaScript code to execute during the event (optional).
- **concurrency_limit**: Limits the number of concurrent executions (optional).
- **concurrency_id**: Custom identifier to manage concurrency (optional).
- **show_api**: If `True`, the API documentation for the event will be shown (optional).
- **time_limit**: Sets a time limit for the event (optional).
- **stream_every**: Defines how often the event should stream data (optional).
- **like_user_message**: If `True`, mimics user messages in event behavior (optional).

---

### **Summary**
The `gradio.Model3D` component allows users to upload, view, and interact with 3D models directly in a Gradio interface. It supports popular 3D model file formats and enables interactive manipulation through various display modes (solid, point cloud, wireframe). Additionally, the component can trigger event listeners based on user actions such as uploading, editing, or clearing the model. With customization options for camera position, zoom, pan speed, and scale, it provides a flexible solution for integrating 3D models into Gradio apps. The event listeners allow you to handle specific interactions with the models, while the available parameters offer control over the component's appearance and behavior.