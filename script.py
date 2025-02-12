import json
import random
import re
from PIL import Image

with open('image_files.json','r') as file:
    data = json.load(file)

# print(len(data["images"]))

# index = int(input("Enten the index number 0 - 104: "))
index = random.randint(0, len(data["images"])-1)
print("I generated index : ",index)

print(data["images"][index])

selected_image = data["images"][index]

location = 'anime_women/'+selected_image

print(location)

# Open the image and convert to JPG
image = Image.open(f"anime_women/{selected_image}")
rgb_im = image.convert("RGB")  # Ensure it's RGB format for JPEG
rgb_im.save("anime.jpg", "JPEG")  # Save as anime.jpg

print(f"Converted {selected_image} to anime.jpg successfully!")

# Read the original Markdown file
# with open("README.md", "r", encoding='utf-8', errors='ignore') as f:
#     markdown_content = f.read()

# # Regex pattern to find the <img> tag with id="updatable"
# img_pattern = r'<img[^>]*id=["\']updatable["\'][^>]*>'

# # Search for the tag
# match = re.search(img_pattern, markdown_content)

# if match:
#     original_img_tag = match.group(0)

#     # Regex to update the src attribute within the <img> tag
#     updated_img_tag = re.sub(
#         r'src=["\'][^"\']*["\']',  # Match src="current_link"
#         f'src="{"anime_women/"+selected_image}"',  # Replace with new link
#         original_img_tag
#     )

#     # Replace the original <img> tag with the updated one in the Markdown content
#     updated_markdown_content = markdown_content.replace(original_img_tag, updated_img_tag)

#     # Write the updated content back to the file
#     with open("README.md", "w", encoding='utf-8', errors='ignore') as f:
#         f.write(updated_markdown_content)

#     print("Image link updated successfully!")
#     print("Original tag:", original_img_tag)
#     print("Updated tag:", updated_img_tag)
# else:
#     print("No <img> tag with id='updatable' found in the Markdown file.")