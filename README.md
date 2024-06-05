# TIFF 3D Viewer

A simple Python script to interpret TIFF images as slices of a 3D object. This example uses a stack of TIFF images from a papyrus scan.

## Requirements

- Python 3.x
- Pillow
- numpy
- matplotlib

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/tiff_3d_viewer.git
    cd tiff_3d_viewer
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your TIFF images in a directory.
2. Update the `tiff_directory` variable in `tiff_3d_viewer.py` to point to your directory.
3. Run the script:
    ```bash
    python tiff_3d_viewer.py
    ```

## Example

```python
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
