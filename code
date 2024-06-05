import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

def load_tiff_stack(directory):
    """Load a stack of TIFF images from a directory."""
    tiff_stack = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.tiff') or filename.endswith('.tif'):
            img = Image.open(os.path.join(directory, filename))
            tiff_stack.append(np.array(img))
    return np.array(tiff_stack)

def visualize_slice(stack, index):
    """Visualize a specific slice from the 3D stack."""
    plt.imshow(stack[index], cmap='gray')
    plt.title(f'Slice {index}')
    plt.show()

# Replace 'path_to_tiff_directory' with the actual path to your TIFF images
tiff_directory = 'path_to_tiff_directory'
tiff_stack = load_tiff_stack(tiff_directory)

# Visualize the middle slice
middle_slice = len(tiff_stack) // 2
visualize_slice(tiff_stack, middle_slice)
