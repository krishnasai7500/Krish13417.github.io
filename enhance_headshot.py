from PIL import Image, ImageEnhance, ImageFilter
import os

# Create directory for enhanced images
os.makedirs('/home/ubuntu/portfolio_project/images/enhanced', exist_ok=True)

# Select the best image for enhancement (image 3)
image_path = '/home/ubuntu/portfolio_project/images/3.jpeg'
output_path = '/home/ubuntu/portfolio_project/images/enhanced/professional_headshot.jpg'

# Open the image
img = Image.open(image_path)

# Apply professional enhancements
# 1. Slightly increase contrast
contrast_enhancer = ImageEnhance.Contrast(img)
img = contrast_enhancer.enhance(1.2)

# 2. Slightly increase brightness
brightness_enhancer = ImageEnhance.Brightness(img)
img = brightness_enhancer.enhance(1.1)

# 3. Slightly increase color saturation
color_enhancer = ImageEnhance.Color(img)
img = color_enhancer.enhance(1.1)

# 4. Apply subtle sharpening
img = img.filter(ImageFilter.SHARPEN)

# 5. Save the enhanced image with high quality
img.save(output_path, 'JPEG', quality=95)

print(f"Enhanced professional headshot saved to {output_path}")
