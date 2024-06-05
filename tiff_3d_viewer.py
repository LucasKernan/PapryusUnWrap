import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2

def load_tiff_stack(directory):
    """Load a stack of TIFF images from a directory."""
    tiff_stack = []
    for filename in sorted(os.listdir(directory), key=lambda x: int(os.path.splitext(x)[0])):
        if filename.endswith('.tiff') or filename.endswith('.tif'):
            img = Image.open(os.path.join(directory, filename))
            tiff_stack.append(np.array(img))
    return np.array(tiff_stack)

def enhance_contrast(image):
    """Enhance the contrast of the image."""
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return cv2.equalizeHist(image)

def visualize_slice(stack, index):
    """Visualize a specific slice from the 3D stack."""
    enhanced_slice = enhance_contrast(stack[index])
    plt.imshow(enhanced_slice, cmap='gray')
    plt.title(f'Slice {index}')
    plt.show()

def unwrap_papyrus(stack):
    """Unwrap the papyrus using a basic approach."""
    height, width = stack.shape[1], stack.shape[2]
    unwrapped_image = np.zeros((height, width * stack.shape[0]), dtype=np.uint8)

    for i in range(stack.shape[0]):
        enhanced_slice = enhance_contrast(stack[i])
        unwrapped_image[:, i * width:(i + 1) * width] = enhanced_slice

    return unwrapped_image

def save_unwrapped_image(unwrapped_image, output_path):
    """Save the unwrapped image as a JPEG file."""
    img = Image.fromarray(unwrapped_image)
    img.save(output_path)

# Directory within the repository containing the TIFF images
tiff_directory = 'ImageFiles'
tiff_stack = load_tiff_stack(tiff_directory)

# Visualize the middle slice
middle_slice = len(tiff_stack) // 2
visualize_slice(tiff_stack, middle_slice)

# Unwrap the papyrus and save the result
unwrapped_papyrus = unwrap_papyrus(tiff_stack)
output_path = 'unwrapped_papyrus.jpg'
save_unwrapped_image(unwrapped_papyrus, output_path)
print(f"Unwrapped papyrus saved to {output_path}")
