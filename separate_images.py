import tifffile as tf
import os

# Current directory containing your TIFF images and the script
directory_path = '.'

# Create folders for the left and right images if they don't exist
left_folder = os.path.join(directory_path, 'left')
right_folder = os.path.join(directory_path, 'right')

if not os.path.exists(left_folder):
    os.makedirs(left_folder)

if not os.path.exists(right_folder):
    os.makedirs(right_folder)

# Get a list of all tiff images in the directory
tiff_files = [f for f in os.listdir(directory_path) if f.endswith('.tif') or f.endswith('.tiff')]

# Loop through each tiff file, split it, and save the halves
for tiff_file in tiff_files:
    # Construct full path
    full_path = os.path.join(directory_path, tiff_file)
    
    # Read the tiff image
    image = tf.imread(full_path)
    
    # Find the center column
    center_col = image.shape[1] // 2
    
    # Split the image into left and right halves
    left_half = image[:, :center_col]
    right_half = image[:, center_col:]
    
    # Save the two halves in the respective folders
    tf.imwrite(os.path.join(left_folder, tiff_file), left_half)
    tf.imwrite(os.path.join(right_folder, tiff_file), right_half)
