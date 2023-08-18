import tifffile as tf
import os
import numpy as np
import matplotlib.pyplot as plt
import re

# Current directory containing your TIFF images
directory_path = '.'

# Get a list of all tiff images in the directory
tiff_files = [f for f in os.listdir(directory_path) if f.startswith('image') and (f.endswith('.tif') or f.endswith('.tiff'))]

# Sort files based on the XXX number
def sort_key(filename):
    match = re.search(r"image(\d+)-scan", filename)
    if match:
        return int(match.group(1))
    return 0  # Default if not found

tiff_files = sorted(tiff_files, key=sort_key)

# Lists to hold the extracted rows and columns
extracted_rows = []
extracted_columns = []

# Loop through each tiff file
for tiff_file in tiff_files:
    # Construct full path
    full_path = os.path.join(directory_path, tiff_file)
    
    # Read the tiff image
    image = tf.imread(full_path)
    
    # Find the row and column indices with the maximum pixel value
    row_index, col_index = np.unravel_index(image.argmax(), image.shape)
    
    print(f"Image: {tiff_file} | Max Pixel Row Index: {row_index} | Max Pixel Column Index: {col_index}")

    # Append this row and column to their respective lists
    extracted_rows.append(image[row_index])
    extracted_columns.append(image[:, col_index])

# Stack the extracted rows and columns to form new images
combined_rows_image = np.vstack(extracted_rows)
combined_columns_image = np.vstack([col.T for col in extracted_columns])

# Save the combined rows and columns images as .npy files
np.save('combined_rows_image.npy', combined_rows_image)
np.save('combined_columns_image.npy', combined_columns_image)

print("Data evaluation completed. Please execute display_evaluation.py to see the results.")