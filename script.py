import json
import random
import re
from PIL import Image
# import cloudinary
# import cloudinary.uploader
# from cloudinary.utils import cloudinary_url
import os
# from dotenv import load_dotenv

with open('image_files.json','r') as file:
    data = json.load(file)

# print(len(data["images"]))

# index = int(input("Enten the index number 0 - 104: "))
index = random.randint(0, len(data["images"])-1)
# print("I generated index : ",index)

# print(data["images"][index])

selected_image = data["images"][index]

location = 'anime_women/'+selected_image

# print(location)

# Open the image and convert to JPG
image = Image.open(f"anime_women/{selected_image}")
rgb_im = image.convert("RGB")  # Ensure it's RGB format for JPEG
# Resize the image to 200x200
rgb_im = rgb_im.resize((200, 200), Image.LANCZOS)  # High-quality resizing
rgb_im.save("destination/anime.webp", "WEBP")  # Save as anime.jpg

# print(f"Converted {selected_image} to anime.jpg successfully!")

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


# load_dotenv()

# # Configuration       
# cloudinary.config( 
#     cloud_name = os.getenv('CLOUD_NAME'),
#     api_key = os.getenv("API_KEY"), 
#     api_secret = os.getenv("API_SECRET"), # Click 'View API Keys' above to copy your API secret
#     secure=True
# )

# # print(f"cloudinary api key: ",cloudinary.config().cloud_name)
# # print(f"cloudinary api key: ",cloudinary.config().api_key)
# # Upload an image
# upload_result = cloudinary.uploader.upload("destination/anime.jpg", public_id="anime",invalidate = True)
# print("Uploaded image url: ",upload_result["secure_url"])

# # Optimize delivery by resizing and applying auto-format and auto-quality
# optimize_url, _ = cloudinary_url("anime", fetch_format="auto", quality="auto")
# print("Optimized image url: ",optimize_url)

# # Transform the image: auto-crop to square aspect_ratio
# auto_crop_url, _ = cloudinary_url("anime", width=200, height=200, crop="scale")
# print("Optimized image url: ",auto_crop_url)