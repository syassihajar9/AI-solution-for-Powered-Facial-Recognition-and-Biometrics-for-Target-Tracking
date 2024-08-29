import os
import numpy as np
import tensorflow as tf
from PIL import Image
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Define model path and class labels
MODEL_PATH = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1'
DATA_DIR = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/data'
CLASS_LABELS = ['class1', 'class2']

# Load the model
model = tf.saved_model.load(MODEL_PATH)
infer = model.signatures['serving_default']

def preprocess_image(image_path):
    """Preprocess the image for the model."""
    img = Image.open(image_path).convert('RGB')
    img = img.resize((160, 160))  # Resize to model's expected input size
    img_array = np.array(img, dtype=np.float32) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

def analyze_images(directory):
    """Analyze images in a given directory and collect results."""
    y_true = []
    y_pred = []
    for class_dir in os.listdir(directory):
        class_path = os.path.join(directory, class_dir)
        if os.path.isdir(class_path):
            print(f"Processing images in directory: {class_path}")
            for file_name in os.listdir(class_path):
                file_path = os.path.join(class_path, file_name)
                if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Preprocess image
                    sample_image = preprocess_image(file_path)
                    
                    # Perform inference
                    result = infer(inputs=tf.convert_to_tensor(sample_image))
                    
                    # Extract results
                    predictions = result['output_0'].numpy().flatten()
                    predicted_class = CLASS_LABELS[np.argmax(predictions)]
                    
                    # Collect true and predicted labels
                    y_true.append(class_dir)
                    y_pred.append(predicted_class)
                    
                    print(f"Results for image {file_name} in {class_dir}:")
                    print(f"Predicted Class: {predicted_class}, Probabilities: {predictions}")
                    print()

    return y_true, y_pred

def plot_confusion_matrix(y_true, y_pred):
    """Plot confusion matrix."""
    cm = confusion_matrix(y_true, y_pred, labels=CLASS_LABELS)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=CLASS_LABELS, yticklabels=CLASS_LABELS)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

def print_classification_report(y_true, y_pred):
    """Print classification report."""
    report = classification_report(y_true, y_pred, labels=CLASS_LABELS, target_names=CLASS_LABELS)
    print("Classification Report:")
    print(report)

if __name__ == "__main__":
    # Process training images
    train_dir = os.path.join(DATA_DIR, 'train')
    y_true, y_pred = analyze_images(train_dir)
    
    # Print classification report and plot confusion matrix
    print_classification_report(y_true, y_pred)
    plot_confusion_matrix(y_true, y_pred)

    # Optionally, process validation images
    # val_dir = os.path.join(DATA_DIR, 'val')
    # y_true, y_pred = analyze_images(val_dir)
    # print_classification_report(y_true, y_pred)
    # plot_confusion_matrix(y_true, y_pred)
