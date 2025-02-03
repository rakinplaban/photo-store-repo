import os
import json

# Directory containing images
IMAGE_DIR = "anime_women"  # Change this to your actual directory
JSON_FILE = "image_files.json"  # Name of the JSON file

# Function to load existing filenames from JSON file
def load_existing_filenames(json_file):
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return empty list if JSON is corrupted
    return []

# Function to save filenames to JSON
def save_filenames(json_file, filenames):
    with open(json_file, "w") as file:
        json.dump(filenames, file, indent=4)

# Get existing filenames from JSON
existing_filenames = set(load_existing_filenames(JSON_FILE))

# Scan directory for image files
new_filenames = {f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))}

# Find new files not in the JSON
files_to_add = new_filenames - existing_filenames

if files_to_add:
    print(f"Adding {len(files_to_add)} new files to JSON.")
    existing_filenames.update(files_to_add)
    save_filenames(JSON_FILE, list(existing_filenames))
else:
    print("No new images found.")

print("Updated JSON file successfully!")
