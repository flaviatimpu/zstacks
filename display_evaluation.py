import numpy as np
import matplotlib.pyplot as plt
import os

# New subfolder name
subfolder_name = '2021_11_08_729nm_70um_addr0_3_6Vpp/right'

# Create the new directory path by joining the current directory and the subfolder name
directory_path = os.path.join('.', subfolder_name)

full_path = directory_path

# Get the last part of the path
parent_folder, last_folder = os.path.split(full_path)
# Get the second to last part of the path
_, second_to_last_folder = os.path.split(parent_folder)
# Combine them into one string
figure_name = f"{second_to_last_folder}_{last_folder}"

# Check for the existence of the .npy files
if not (os.path.exists('combined_rows_image.npy') and os.path.exists('combined_columns_image.npy')):
    print("The combined image files do not exist. Please execute zstack_evaluation.py first.")
    exit()

# Load the saved .npy files
combined_rows_image = np.load('combined_rows_image.npy')
combined_columns_image = np.load('combined_columns_image.npy')

# Plotting the two images side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Displaying the combined columns image with a colorblind friendly colormap
im1 = ax1.imshow(combined_columns_image, cmap='viridis', aspect='auto')
ax1.set_title(figure_name+"_XZ")

# Displaying the combined rows image with a colorblind friendly colormap
im2 = ax2.imshow(combined_rows_image, cmap='viridis', aspect='auto')
ax2.set_title(figure_name+"_YZ")

# Adding the axis labels
ax1.set_ylabel("z-axis (um)")
ax1.set_xlabel("x-axis (a.u.) - along waveguide")
ax2.set_ylabel("z-axis (um)")
ax2.set_xlabel("y-axis (a.u.) - across waveguide")

# Turn on axis for the bottom and left side to display labels
ax1.tick_params(left=True, labelleft=True, bottom=True, labelbottom=True, right=False, top=False)
ax2.tick_params(left=True, labelleft=True, bottom=True, labelbottom=True, right=False, top=False)

cbar1 = fig.colorbar(im1, ax=ax1, orientation='vertical')
cbar1.set_label('Counts', rotation=270, labelpad=15)

cbar2 = fig.colorbar(im2, ax=ax2, orientation='vertical')
cbar2.set_label('Counts', rotation=270, labelpad=15)

plt.tight_layout(pad=3.0)
plt.show()

fig.savefig(f"{figure_name}.png", bbox_inches='tight')
