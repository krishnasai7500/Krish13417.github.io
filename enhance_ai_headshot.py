from PIL import Image, ImageEnhance, ImageFilter
import os

# Create directory for enhanced images
os.makedirs('/home/ubuntu/portfolio_project/images/enhanced', exist_ok=True)

# Select the new image for enhancement
image_path = '/home/ubuntu/portfolio_project/images/new_headshot.jpg'
output_path = '/home/ubuntu/portfolio_project/images/enhanced/ai_professional_headshot.jpg'

# Open the image
img = Image.open(image_path)

# Apply professional enhancements
# 1. Slightly increase contrast
contrast_enhancer = ImageEnhance.Contrast(img)
img = contrast_enhancer.enhance(1.15)

# 2. Slightly increase brightness
brightness_enhancer = ImageEnhance.Brightness(img)
img = brightness_enhancer.enhance(1.05)

# 3. Slightly increase color saturation
color_enhancer = ImageEnhance.Color(img)
img = color_enhancer.enhance(1.1)

# 4. Apply subtle sharpening
img = img.filter(ImageFilter.SHARPEN)

# 5. Save the enhanced image with high quality
img.save(output_path, 'JPEG', quality=95)

print(f"Enhanced AI professional headshot saved to {output_path}")

# Copy to website images directory
website_image_path = '/home/ubuntu/portfolio_project/website/images/professional_headshot.jpg'
img.save(website_image_path, 'JPEG', quality=95)
print(f"Enhanced headshot also copied to website directory at {website_image_path}")
