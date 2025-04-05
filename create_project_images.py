from PIL import Image, ImageDraw, ImageFont
import os

# Create directory for project images
project_images_dir = '/home/ubuntu/portfolio_project/website/images'
os.makedirs(project_images_dir, exist_ok=True)

# Define colors for project images
colors = [
    (66, 133, 244),  # Blue
    (219, 68, 55),   # Red
    (244, 180, 0),   # Yellow
    (15, 157, 88),   # Green
    (98, 71, 170),   # Purple
    (66, 133, 244)   # Blue (repeated for 6th project)
]

# Project titles
project_titles = [
    "Dialogflow Weather API",
    "CRUD Operations",
    "Face Recognition",
    "MyOnlineStore",
    "Retail EDA",
    "Superstore Analysis"
]

# Create project placeholder images
for i in range(1, 7):
    # Create a colored image
    img = Image.new('RGB', (800, 400), colors[i-1])
    draw = ImageDraw.Draw(img)
    
    # Try to use a font, fall back to default if not available
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 40)
    except IOError:
        font = ImageFont.load_default()
    
    # Add project title
    title = project_titles[i-1]
    text_width = draw.textlength(title, font=font)
    position = ((800 - text_width) // 2, 180)
    draw.text(position, title, fill=(255, 255, 255), font=font)
    
    # Add project number
    draw.text((20, 20), f"Project {i}", fill=(255, 255, 255), font=font)
    
    # Save the image
    img.save(f"{project_images_dir}/project{i}.jpg")

print("Project placeholder images created successfully!")
