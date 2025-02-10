import os
import json

# Directory containing images
IMAGE_DIR = "anime_women"  # Change this to your actual directory

# Scan directory for image files
new_filenames = {f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp'))}

# Read the existing JSON data
with open('image_files.json', 'r') as f:
    data = json.load(f)

# Initialize 'images' key if not present
if 'images' not in data:
    data['images'] = []

images = data['images']

# Add new files that aren't already in the list
for filename in new_filenames:
    if filename not in images:
        images.append(filename)

# Save the updated data back to the JSON file
with open('image_files.json', 'w') as f:
    json.dump(data, f, indent=4)

print(f"Total images: {len(images)}")
