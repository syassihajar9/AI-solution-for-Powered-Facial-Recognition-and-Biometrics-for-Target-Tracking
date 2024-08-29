import tensorflow as tf

def evaluate_model(model_path, test_images, test_labels):
    # Load the model
    model = tf.keras.models.load_model(model_path)
    
    # Ensure the images match the input size expected by the model
    input_shape = model.input_shape[1:3]  # (height, width)
    
    # Resize test images to match the model's input shape
    test_images_resized = tf.image.resize(test_images, input_shape)
    
    # Evaluate the model on the resized test data
    loss, accuracy = model.evaluate(test_images_resized, test_labels, verbose=0)
    
    # Convert accuracy to percentage
    accuracy_percentage = accuracy * 100
    
    # Print the accuracy
    print(f"Model accuracy: {accuracy_percentage:.2f}%")
    return accuracy_percentage

# Example usage:
# Load CIFAR-10 data as an example
cifar10 = tf.keras.datasets.cifar10
(_, _), (test_images, test_labels) = cifar10.load_data()

# Normalize the test images
test_images = test_images.astype("float32") / 255.0

# Path to your saved model (.keras file)
model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/re_export_model/model.keras'

# Evaluate the model
evaluate_model(model_path, test_images, test_labels)
