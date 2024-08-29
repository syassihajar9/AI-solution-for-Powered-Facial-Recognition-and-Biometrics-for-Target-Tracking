import tensorflow as tf
import numpy as np

# Path to the Keras model file
model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/1.keras'

def load_model(path):
    try:
        model = tf.keras.models.load_model(path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Failed to load the model: {e}")
        raise

def check_weights(model):
    try:
        weights = model.get_weights()
        print(f"Number of weight arrays: {len(weights)}")
        for i, weight in enumerate(weights):
            print(f"Weight array {i}: shape {weight.shape}")
    except Exception as e:
        print(f"Failed to get weights: {e}")
        raise

def main():
    model = load_model(model_path)
    check_weights(model)

if __name__ == "__main__":
    main()
