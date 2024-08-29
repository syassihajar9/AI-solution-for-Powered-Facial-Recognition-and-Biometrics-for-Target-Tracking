import tensorflow as tf

# Load the model
model = tf.saved_model.load('C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1')

# Print the available signatures
print("Signatures:", list(model.signatures.keys()))

# Access the 'serving_default' signature
signature = model.signatures['serving_default']

# Print input and output tensor specs
print("Inputs:", signature.structured_input_signature)
print("Outputs:", signature.structured_outputs)
