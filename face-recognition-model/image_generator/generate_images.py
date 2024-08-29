import os
from PIL import Image, ImageDraw

# Set up directories
base_dir = 'C:/Users/anass/RiderProjects/dronesurveillanceapi/face-recognition-model/data'
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# Define classes
classes = ['class1', 'class2']

# Create directories
for split_dir in [train_dir, val_dir]:
    for cls in classes:
        os.makedirs(os.path.join(split_dir, cls), exist_ok=True)

# Function to generate a simple image
def generate_image(save_path, color, shape):
    image = Image.new('RGB', (160, 160), color='white')
    draw = ImageDraw.Draw(image)

    if shape == 'circle':
        draw.ellipse((40, 40, 120, 120), fill=color)
    elif shape == 'square':
        draw.rectangle((40, 40, 120, 120), fill=color)

    image.save(save_path)

# Generate images for training
for i in range(100):  # 100 images per class
    generate_image(os.path.join(train_dir, 'class1', f'class1_img_{i}.jpg'), 'red', 'circle')
    generate_image(os.path.join(train_dir, 'class2', f'class2_img_{i}.jpg'), 'blue', 'square')

# Generate images for validation
for i in range(25):  # 25 images per class
    generate_image(os.path.join(val_dir, 'class1', f'class1_img_{i}.jpg'), 'red', 'circle')
    generate_image(os.path.join(val_dir, 'class2', f'class2_img_{i}.jpg'), 'blue', 'square')
