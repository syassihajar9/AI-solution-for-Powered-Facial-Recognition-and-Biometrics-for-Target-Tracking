import tensorflow as tf

# Define paths
keras_model_path = '/app/model/model.keras'
saved_model_path = '/app/saved_model'

# Load and convert the model
model = tf.keras.models.load_model(keras_model_path)
tf.saved_model.save(model, saved_model_path)

print(f"Model successfully saved to: {saved_model_path}")
