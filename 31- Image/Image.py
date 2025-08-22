'''
The gr.Image component in Gradio is versatile and can be used both for input and output of images. 
It supports various image formats and allows customization through parameters such as type, format, 
height, width, and more. As an input, it can accept images as numpy.ndarray, PIL.Image.Image, or 
file paths, depending on the type parameter. For output, it can display images in similar formats.
'''

# Example 1: Basic Image Upload and Display

import gradio as gr

def display_image(image):
    return image

demo = gr.Interface(
    fn=display_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil")
)

demo.launch()

# (------------------------------------------------------------------------)

# Example 2: Image Processing - Sepia Filter

import numpy as np
import gradio as gr

def sepia(input_img):
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img

demo = gr.Interface(sepia, gr.Image(type="numpy"), "image")
demo.launch()

# (-------------------------------------------------------------------------)

# Example 3: Image Rotation

from PIL import Image
import gradio as gr

def rotate_image(image: Image.Image, angle: int) -> Image.Image:
    """Rotate the given PIL image by the specified angle."""
    return image.rotate(angle, expand=True)  # `expand=True` prevents cropping

# Create Gradio interface
demo = gr.Interface(
    fn=rotate_image,
    inputs=[
        gr.Image(type="pil"),  # Ensures the input is a PIL Image
        gr.Slider(0, 360, step=1, label="Rotation Angle")
    ],
    outputs=gr.Image(type="pil")  # Ensures the output remains a PIL Image
)

demo.launch()


# (--------------------------------------------------------------------------)

# Example 4: Image Resizing

from PIL import Image
import gradio as gr

def resize_image(image: Image.Image, width: int, height: int) -> Image.Image:
    resized_image = image.resize((width, height))
    return resized_image

demo = gr.Interface(
    fn=resize_image,
    inputs=[
        gr.Image(type="pil"),
        gr.Slider(10, 1000, step=1, label="Width"),
        gr.Slider(10, 1000, step=1, label="Height")
    ],
    outputs=gr.Image(type="pil")
)

demo.launch(share=True)

# (---------------------------------------------------------------------------)

# Example 5: Image Grayscale Conversion

from PIL import Image
import gradio as gr

def grayscale(image: Image.Image) -> Image.Image:
    return image.convert("L")  # Convert to grayscale

demo = gr.Interface(
    fn=grayscale,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil")
)

demo.launch()

# (-----------------------------------------------------------------------------)

# Example 6: Image Inversion

from PIL import Image, ImageOps
import gradio as gr

def invert_image(image: Image.Image) -> Image.Image:
    if image.mode == "RGBA":
        r, g, b, a = image.split()
        rgb_image = Image.merge("RGB", (r, g, b))  # Remove alpha channel
        inverted_rgb = ImageOps.invert(rgb_image)  # Invert only RGB
        return Image.merge("RGBA", (*inverted_rgb.split(), a))  # Add alpha back
    else:
        return ImageOps.invert(image)  # Directly invert RGB or grayscale images

demo = gr.Interface(
    fn=invert_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil")
)

demo.launch()

# (-------------------------------------------------------------------------------)

# Example 7: Image Cropping

from PIL import Image
import gradio as gr

def crop_image(image: Image.Image, left: int, top: int, right: int, bottom: int) -> Image.Image:
    width, height = image.size
    
    # Ensure the crop coordinates are within the valid range
    left = max(0, min(left, width - 1))
    top = max(0, min(top, height - 1))
    right = max(left + 1, min(right, width))  # Ensure right > left
    bottom = max(top + 1, min(bottom, height))  # Ensure bottom > top

    return image.crop((left, top, right, bottom))

demo = gr.Interface(
    fn=crop_image,
    inputs=[
        gr.Image(type="pil"),
        gr.Slider(0, 500, step=1, label="Left"),  # Adjusted max value for practical use
        gr.Slider(0, 500, step=1, label="Top"),
        gr.Slider(0, 500, step=1, label="Right"),
        gr.Slider(0, 500, step=1, label="Bottom")
    ],
    outputs=gr.Image(type="pil")
)

demo.launch()

# (---------------------------------------------------------------------------------)

# Example 8: Image Filtering - Blur

from PIL import Image, ImageFilter
import gradio as gr

def blur_image(image: Image.Image) -> Image.Image:
    return image.filter(ImageFilter.BLUR)

demo = gr.Interface(
    fn=blur_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil")
)

demo.launch()
