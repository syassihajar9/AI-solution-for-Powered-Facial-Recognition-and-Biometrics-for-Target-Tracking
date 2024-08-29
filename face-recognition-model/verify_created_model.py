import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('model.keras')

# Print the model summary
model.summary()
