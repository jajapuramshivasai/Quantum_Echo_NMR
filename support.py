import nbformat
import os
import base64

# Create figures directory if it doesn't exist
os.makedirs('figures', exist_ok=True)

# Load the notebook
with open('Main.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

img_count = 0
for cell in nb.cells:
    if 'outputs' in cell:
        for output in cell['outputs']:
            if output.output_type == 'display_data':
                if 'image/png' in output.data:
                    img_data = output.data['image/png']
                    # Save each figure as a PNG in the figures folder
                    with open(f'figures/figure_{img_count}.png', 'wb') as img_file:
                        img_file.write(base64.b64decode(img_data))
                    img_count += 1