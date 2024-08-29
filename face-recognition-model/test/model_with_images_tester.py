import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Path to the saved model directory
MODEL_DIR = "C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1"
# Path to the data directory
DATA_DIR = "C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/data"

# Load the TensorFlow model
model = tf.saved_model.load(MODEL_DIR)

# Obtain the serving function (signature)
infer = model.signatures['serving_default']

# Function to preprocess images
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((160, 160))  # Resize to match model input shape
    image_array = np.array(image).astype(np.float32)
    if image_array.shape[-1] == 4:  # Remove alpha channel if present
        image_array = image_array[..., :3]
    image_array = image_array / 255.0  # Normalize pixel values to [0, 1]
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    return image_array

# Perform inference on images from both train and val directories
for split in ['train', 'val']:
    split_dir = os.path.join(DATA_DIR, split)
    for class_dir in os.listdir(split_dir):
        class_path = os.path.join(split_dir, class_dir)
        if os.path.isdir(class_path):
            print(f"Processing images in directory: {class_path}")
            for file_name in os.listdir(class_path):
                file_path = os.path.join(class_path, file_name)
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Preprocess image
                    sample_image = preprocess_image(file_path)
                    
                    # Perform inference
                    result = infer(inputs=tf.convert_to_tensor(sample_image))
                    
                    # Print the result
                    print(f"Results for image {file_name} in {class_dir}:")
                    print(result)
