import tensorflow as tf
import numpy as np

# Path to the directory containing the saved model
MODEL_DIR = "C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1"

# Load the TensorFlow model
model = tf.saved_model.load(MODEL_DIR)

# Obtain the serving function (signature)
infer = model.signatures['serving_default']

# Prepare sample input data
# Assuming your model expects an input of shape (None, 160, 160, 3)
# Create a dummy input image of the correct shape
sample_image = np.random.random((1, 160, 160, 3)).astype(np.float32)

# Perform inference
# The input tensor name is 'inputs' as found from the inspection
result = infer(inputs=tf.convert_to_tensor(sample_image))

# Print the result
print("Model outputs:")
print(result)
